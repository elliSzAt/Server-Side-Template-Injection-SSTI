# Java - Server-side Template Injection

![](https://hackmd.io/_uploads/SkJrk4-Yn.png)


Mục tiêu của ta ở challenge này là phải truy cập vào file SECRET_FLAG.txt.

![](https://hackmd.io/_uploads/HJbtyNbY3.png)

Bước vào challenge thì ta thấy có phần điền thông tin, như đề bài của challenge lần này là Java nên ta sẽ đi theo hướng khai thác lỗi SSTI của Java.

![](https://hackmd.io/_uploads/HJrJx4-F2.png)

Mình đã thử kiểm tra với ``${7*7}`` và kết quả nó đúng như mong đợi. Tiếp theo ta chỉ cần tìm payload sao cho phù hợp thui ^^

![](https://hackmd.io/_uploads/HJ5aeNWK3.png)


Ở đây mình sử dụng payload là ``<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("id")}``. Để test trước, sau khi nó thành công thì mình tiếp tục list toàn bộ các file ra bằng lệnh ``ls -la``.

![](https://hackmd.io/_uploads/rkyfWV-K2.png)


Và chúng ta đã tìm ra được file cần tìm rùi, tiếp theo chỉ cần truy cập vào nó là xong.

![](https://hackmd.io/_uploads/rJc4-EbYh.png)

Nhẹ nhàng lấy 30d thui !!
