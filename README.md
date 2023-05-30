# Server-Side Template Injection – SSTI là gì?

**Server-Side Template Injection – SSTI** là phương án tấn công dựa vào **template syntax** (có thể hiểu đại khái là cú pháp của khuôn mẫu mà mục tiêu đang sử dụng để dựng web page). Với phương án này, attacker sẽ “chích” các payload độc hại vào cái template từ đó thực thi payload ngay trên phía server.

**Template** có thể tạm dịch là “khuôn mẫu” theo tiếng Việt. Nhưng tôi thấy từ tiếng Việt này có vẻ cồng kềnh quá. Ngoài ra, khi muốn tìm hiểu thêm các vấn đề liên quan thì có thể bạn cũng sẽ gặp khó khăn với từ khóa tiếng Việt. Do vậy, tôi chốt dùng luôn từ gốc tiếng Anh – **Template** luôn cho lành.

Rồi, quay lại vấn đề chính. Cái **template** này muốn hoạt động sẽ cần một thứ gọi là **engine**. **Engine** này đóng vai trò tổng hợp các yếu tố cố định trên template với các dữ liệu được đưa vào tại thời điểm đó để **render** (tôi tạm dịch là dựng) ra phiên bản web page tương ứng.

Và đây chính là vị trí mà vấn đề phát sinh. Cụ thể, **SSTI attack** sẽ xuất hiện khi dữ liệu nhập liệu của người dùng được kết hợp trực tiếp vào **template** thay vì đẩy vào như dữ liệu đơn thuần. Khi đó, attacker sẽ có thể đút vào các **template directive** (tôi tạm dịch là các câu lệnh chỉ đạo cho **template** hành động) nhằm thao túng **template engine** từ đó có thể chiếm trọn quyền điều khiển server.

Như đề cập ở trên, với **SSTI**, attacker có thể triển **Remote Code Execution – RCE** (thực thi code từ xa) và chiếm trọn quyền điều khiển con server liên quan cũng như mở rộng tấn công sang các đối tượng khác trong hệ thống. Kể cả khi không thể triển “full service” **RCE**, attacker vẫn có thể dùng **SSTI** làm bàn đạp cho các phi vụ khác như đọc dữ liệu nhạy cảm trên server.

# Server-Side Template Injection – SSTI diễn ra như thế nào?

**Template** dạng **static** (tức là dạng “tĩnh”) sẽ chỉ cung cấp các **placeholder** (tạm hiểu là chỗ trống) để **engine** hốt các dữ liệu liên quan điền vào rồi render ra web page tương ứng. Ví dụ, **Twig template** sau đây sẽ hốt cái dữ liệu đẩy vào cái **placeholder {first_name}** để tạo ra nội dung chào hỏi người dùng theo kiểu:

```
$output = $twig->render("Dear {first_name},", array("first_name" => $user.first_name) );
```

Và với kiểu này thì **SSTI** sẽ không có đất diễn vì thông tin đưa vào **placeholder {first_name}** chỉ là dữ liệu đơn thuần.

Tuy nhiên, với **template** dạng string cho phép kết hợp trực tiếp thông tin nhập liệu của người dùng vào trước khi xuất bản ra web page như ví dụ sau đây thì mọi chuyện lại khác.

```
$output = $twig->render("Dear " . $_GET['name']);
```

Trong tình huống này, một phần của **template** đã không còn **static** mà đã chuyển sang **dynamic** (động) tùy thuộc vào **GET parameter name**.

Vì lẽ đó, nếu gặp user chèn payload độc hại vô bên trong **parameter name** (ví dụ thông qua việc chạy request với URL ``http://vulnerable-website.com/?name={{bad-stuff-here}}``) thì khi xử lý **template syntax**, server sẽ gặp vấn đề với cái **bad-stuff-here**.

# Các bước triển khai SSTI attack

Nhìn chung, **SSTI attack** sẽ diễn ra qua các bước bao gồm **Detect** (Phát hiện), **Identify** (Nhận diện) và **Exploit** (khai thác).

![](https://hackmd.io/_uploads/SJXmp17Un.png)

## Detect

Ở bước này, phương án thử nghiệm đơn giản ban đầu là **fuzzing** (tôi không biết tạm dịch bằng từ gì nhưng có thể hiểu là quá trình thử nghiệm với nhiều dạng thông tin đầu vào và quan sát đầu ra để đánh giá). Với phương án này, tôi sẽ thử chèn vào chuỗi các ký tự đặc biệt (ví dụ như ``${{<%[%'”}}%\``) thường dùng của các **template expression**. Lúc này, quan sát kết quả đầu ra, nếu ghi nhận có kết quả khác thường thì khả năng cao là server đã gặp vấn đề. Đây là dấu hiệu cho thấy tôi nên nghiên cứu tiến hành các thử nghiệm chi tiết hơn.

Cũng cần nhấn mạnh việc dò tìm phát hiện **SSTI vulnerabilities** sẽ phụ thuộc vào **context** (ngữ cảnh) cụ thể. Tức là đôi khi việc **fuzzing** không cho thấy dấu hiệu gì khác thường nhưng khi xem xét thử nghiệm theo **context** cụ thể, có thể tôi sẽ vẫn thu lượm được các kết quả thú vị.

Tóm lại, quá trình **Detect** sẽ bao gồm **fuzzing test** để thăm dò sơ bộ và sau đó là thử nghiệm theo các **context** để xác nhận hoặc phân tích sâu hơn nhằm phục vụ cho các bước tiếp theo. Hai dạng **context** cần được xem xét thử nghiệm bao gồm:

### Plaintext context

**Plaintext context** có thể tạm dịch là ngữ cảnh text đơn thuần khi **template language** cho phép tôi nhập liệu trực tiếp thông qua **HTML tag** hoặc thông qua **template syntax** tương ứng. Minh họa đơn giản cho plaintext context với **Freemaker template engine** như sau:

```
render('Hello ' + username)
```

Tôi có thể thử nghiệm **SSTI** bằng cách thiết lập các phép toán (7*7 trong trường hợp bên dưới) trong parameter rồi chạy request kiểu.

```
http://vulnerable-website.com/?username=${7*7}
```

Lúc này, nếu tôi quan sát thấy xuất hiện “Hello 49” ở đâu đó thì chứng tỏ cái phép toán “*” (toán tử nhân) đã được server xử lý. Và đây là dấu hiệu cho thấy tôi có thể khai thác server với **SSTI**.

Vấn đề ở đây là chỉ với **syntax** phù hợp, **template engine** mới xử lý thông tin (ví dụ cái phép toán nhân nói trên). Và tôi sẽ cần ghi nhận lại để phân tích kỹ hơn ở bước **Identify**.

### Code context

Với ngữ cảnh này, dữ liệu tôi đưa vào sẽ được đẩy vào trong **template expression**. Ví dụ như tình huống có một **variable** (biến số) mà tôi có thể kiểm soát (**greeting** trong trường hợp bên dưới) được đặt vào bên trong của một **parameter** như sau:

```
greeting = getQueryParameter('greeting')

engine.render("Hello {{"+greeting+"}}", data)
```

Và URL tương ứng theo kiểu:

```
http://vulnerable-website.com/?greeting=data.username
```

Thì kết quả xuất ra sẽ có dạng “Hello {username}“.

Lúc này, tôi có thể thử nghiệm **SSTI** theo kiểu sử dụng **templating syntax** phổ biến là “}}” để chèn một **HTML** tùy ý vào sau đấy.

```
http://vulnerable-website.com/?greeting=data.username}}<tag>
```

Nếu output cho thấy kết quả có kèm theo cái **HTML** tôi đưa vào bên dưới thì tôi có thể tiếp tục với **SSTI**.

```
Hello {username}<tag>
```

**Lưu ý**: Trường hợp không nhận được kết quả như trên thì tôi có thể kiểm tra lại xem có dùng sai cú pháp hay không. Nếu đã kiểm kỹ mà kết quả vẫn thế thì khả năng tôi sẽ không làm được gì với **SSTI**.

## Identify

Sau khi xác nhận khả năng khai thác với **SSTI**, ở bước này, tôi sẽ tập trung nhận diện **template engine**. Dù đám **templating language** khá nhiều nhưng đa phần chúng có nhiều điểm tương đồng về mặt **syntax**. Ngoài ra, đôi khi server “dễ dãi” cũng sẽ cho ra thông tin **template engine** đang được sử dụng trong thông báo lỗi khi tôi sử dụng sai **syntax**.

Ví dụ, với syntax ``<%=foobar%>`` sẽ làm phát sinh thông báo lỗi cho biết **Ruby-based ERB engine** đang được sử dụng như bên dưới:

```
(erb):1:in `<main>': undefined local variable or method `foobar' for main:Object (NameError)

from /usr/lib/ruby/2.5.0/erb.rb:876:in `eval'

from /usr/lib/ruby/2.5.0/erb.rb:876:in `result'

from -e:4:in `<main>'
```

Với tình huống này, công việc chuẩn bị payload để thăm dò **template engine** của tôi sẽ nhẹ nhàng hơn.

Trường hợp xấu, không được server thông qua thông báo lỗi, tôi sẽ cần kiểm tra thủ công với các thể loại payload theo các ngôn ngữ khác nhau và quan sát kết quả để đánh giá **template engine** thông qua phương án loại trừ.

Nhìn chung, tôi có thể sử dụng các phép toán theo syntax khác nhau của các dạng **template engine** rồi nghiên cứu kết quả đầu ra coi phương án nào thành công. Để dễ thực hiện, tôi có thể nghiên cứu và dựng lên một cái **decision tree** tương tự như sau để tiện bề xử lý.

![](https://hackmd.io/_uploads/rkjHrlXUn.png)

Lưu ý: Một payload có thể chạy được với nhiều **template engine** nên tôi sẽ cần làm hết các nhánh của **decission tree**.

## Exploit

Với việc đã phát hiện **SSTI vulnerability** tồn tại và nhận diện được **template engine** tương ứng, tôi sẽ có thể triển tiếp phần **exploit** bao gồm các bước **read** (đọc chi tiết về **template syntax**, thông tin về phương án triển khai bao mật và phương án **exploit** mà giang hồ đã triển khai), **explore** (khám phá môi trường tác nghiệp và các đối tượng liên quan) và attack (triển khai tấn công).
