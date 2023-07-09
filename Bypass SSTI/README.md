Có nhiều cách để tấn công và bypass SSTI, và phụ thuộc vào cách mà ứng dụng của bạn được thiết kế và triển khai. Dưới đây là một số cách chi tiết khi mà SSTI có thể bị bypass:

  -  Sử dụng các ký tự đặc biệt để tránh việc phân tích cú pháp SSTI: Kẻ tấn công có thể sử dụng các ký tự đặc biệt như ``|, ;, &, &&`` để chuyển đổi các biểu thức Jinja2 sang các lệnh shell tương ứng, chẳng hạn như ``{{ 'cat /etc/passwd' | system }}``. Kẻ tấn công cũng có thể sử dụng các ký tự như ``{{, }}, [[, ]], ((, ))`` để đánh lừa bộ phân tích cú pháp SSTI. Trong một số trường hợp, kẻ tấn công cũng có thể sử dụng các ký tự Unicode tương đương để tránh các hàm an toàn.

  -  Sử dụng các hàm an toàn không chính thức hoặc không được tài liệu: Kẻ tấn công có thể tìm kiếm các hàm an toàn không chính thức, ví dụ như ``__import__('os').popen('cat /etc/passwd').read()`` để thực thi mã shell từ xa. Kẻ tấn công có thể sử dụng các hàm an toàn như ``safe, e, escape, striptags, urlencode`` để tránh các hàm an toàn được tài liệu.

  -  Sử dụng các kỹ thuật phức tạp hơn để bypass các hàm an toàn: Kẻ tấn công có thể viết lại các hàm an toàn để bỏ qua các giới hạn an toàn, chẳng hạn như sử dụng hàm ``eval()`` để thực thi các biểu thức Jinja2 không an toàn. Kẻ tấn công cũng có thể sử dụng các kỹ thuật như truy cập đến các biến toàn cục hoặc các đối tượng không an toàn để thực thi mã.

  -  Sử dụng các lỗ hổng trong các thư viện và phần mềm được sử dụng: Kẻ tấn công có thể tìm kiếm các lỗ hổng trong các thư viện và phần mềm được sử dụng để triển khai ứng dụng của bạn, chẳng hạn như việc sử dụng các phiên bản thư viện cũ hoặc không được bảo mật. Kẻ tấn công cũng có thể sử dụng các lỗ hổng trong các ứng dụng bên thứ ba được tích hợp trong ứng dụng của bạn.

  -  Sử dụng các lỗ hổng trong các framework: Kẻ tấn công có thể tìm kiếm các lỗ hổng trong các framework để triển khai ứng dụng của bạn, chẳng hạn như việc sử dụng các phiên bản framework cũ hoặc không được bảo mật. Kẻ tấn công cũng có thể sử dụng các lỗ hổng trong các tính năng framework như ``session, cookie, authentication`` để thực hiện các cuộc tấn công.
