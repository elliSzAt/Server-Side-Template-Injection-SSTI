Có nhiều cách để tấn công và bypass SSTI, và phụ thuộc vào cách mà ứng dụng của bạn được thiết kế và triển khai. Dưới đây là một số cách chi tiết khi mà SSTI có thể bị bypass:

  -  Sử dụng các ký tự đặc biệt để tránh việc phân tích cú pháp SSTI: Kẻ tấn công có thể sử dụng các ký tự đặc biệt như ``|, ;, &, &&`` để chuyển đổi các biểu thức Jinja2 sang các lệnh shell tương ứng, chẳng hạn như ``{{ 'cat /etc/passwd' | system }}``. Kẻ tấn công cũng có thể sử dụng các ký tự như ``{{, }}, [[, ]], ((, ))`` để đánh lừa bộ phân tích cú pháp SSTI. Trong một số trường hợp, kẻ tấn công cũng có thể sử dụng các ký tự Unicode tương đương để tránh các hàm an toàn.

  -  Sử dụng các hàm an toàn không chính thức hoặc không được tài liệu: Kẻ tấn công có thể tìm kiếm các hàm an toàn không chính thức, ví dụ như ``__import__('os').popen('cat /etc/passwd').read()`` để thực thi mã shell từ xa. Kẻ tấn công có thể sử dụng các hàm an toàn như ``safe, e, escape, striptags, urlencode`` để tránh các hàm an toàn được tài liệu.

  -  Sử dụng các kỹ thuật phức tạp hơn để bypass các hàm an toàn: Kẻ tấn công có thể viết lại các hàm an toàn để bỏ qua các giới hạn an toàn, chẳng hạn như sử dụng hàm ``eval()`` để thực thi các biểu thức Jinja2 không an toàn. Kẻ tấn công cũng có thể sử dụng các kỹ thuật như truy cập đến các biến toàn cục hoặc các đối tượng không an toàn để thực thi mã.

  -  Sử dụng các lỗ hổng trong các thư viện và phần mềm được sử dụng: Kẻ tấn công có thể tìm kiếm các lỗ hổng trong các thư viện và phần mềm được sử dụng để triển khai ứng dụng của bạn, chẳng hạn như việc sử dụng các phiên bản thư viện cũ hoặc không được bảo mật. Kẻ tấn công cũng có thể sử dụng các lỗ hổng trong các ứng dụng bên thứ ba được tích hợp trong ứng dụng của bạn.

  -  Sử dụng các lỗ hổng trong các framework: Kẻ tấn công có thể tìm kiếm các lỗ hổng trong các framework để triển khai ứng dụng của bạn, chẳng hạn như việc sử dụng các phiên bản framework cũ hoặc không được bảo mật. Kẻ tấn công cũng có thể sử dụng các lỗ hổng trong các tính năng framework như ``session, cookie, authentication`` để thực hiện các cuộc tấn công.



  -  Sử dụng các kỹ thuật khai thác lỗ hổng phụ thuộc vào kiểu: Kẻ tấn công có thể sử dụng các lỗ hổng phụ thuộc vào kiểu (type juggling) để thực hiện các cuộc tấn công SSTI. Ví dụ, kẻ tấn công có thể sử dụng các giá trị kiểu chuỗi để thay đổi kiểu dữ liệu của biến và thực hiện các phép tính không mong muốn.

  -  Sử dụng các kỹ thuật khai thác lỗ hổng serialization: Kẻ tấn công có thể sử dụng các lỗ hổng serialization để tạo ra các đối tượng độc hại và thực hiện các cuộc tấn công SSTI. Ví dụ, kẻ tấn công có thể tạo ra một đối tượng Python độc hại và truyền nó vào một biểu thức Jinja2 để thực thi mã độc.

  -  Sử dụng các kỹ thuật khai thác lỗ hổng template injection khác: Template injection không chỉ giới hạn ở SSTI, mà còn có thể được sử dụng để khai thác các lỗ hổng khác như template injection trong các framework khác như AngularJS, Vue.js, và React. Kẻ tấn công có thể sử dụng các lỗ hổng này để thực hiện các cuộc tấn công XSS, RCE và các cuộc tấn công khác.

  -  Kết hợp các kỹ thuật khác nhau để tấn công: Kẻ tấn công có thể kết hợp nhiều kỹ thuật khác nhau để tấn công và bypass SSTI. Ví dụ, kẻ tấn công có thể sử dụng kỹ thuật type juggling để thay đổi kiểu dữ liệu của biến và sử dụng kỹ thuật đánh lừa bộ phân tích cú pháp để thực hiện các cuộc tấn công SSTI.

  -  Sử dụng các kỹ thuật khai thác lỗ hổng XPath: Trong trường hợp SSTI được sử dụng trong các ứng dụng web sử dụng XML hoặc XPath, kẻ tấn công có thể sử dụng các lỗ hổng XPath để thực hiện các cuộc tấn công SSTI.

  -  Sử dụng các kỹ thuật khai thác lỗ hổng SQL: Trong trường hợp SSTI được sử dụng trong các ứng dụng web sử dụng SQL, kẻ tấn công có thể sử dụng các lỗ hổng SQL để thực hiện các cuộc tấn công SSTI.

  -  Sử dụng các kỹ thuật khai thác lỗ hổng XML Injection: Kẻ tấn công có thể sử dụng các lỗ hổng XML Injection để thực hiện các cuộc tấn công SSTI trong các ứng dụng sử dụng XML.

  -  Sử dụng các kỹ thuật khai thác lỗ hổng Server-Side Request Forgery (SSRF): Kẻ tấn công có thể sử dụng các lỗ hổng SSRF để thực hiện các cuộc tấn công SSTI bằng cách đưa ra các yêu cầu HTTP không an toàn.

  -  Sử dụng các kỹ thuật khai thác lỗ hổng Remote File Inclusion (RFI): Kẻ tấn công có thể sử dụng các lỗ hổng RFI để thực hiện các cuộc tấn công SSTI bằng cách tải mã độc từ xa và thực thi nó trong ứng dụng.

