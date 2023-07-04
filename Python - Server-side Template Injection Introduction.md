# Python - Server-side Template Injection Introduction

![](https://hackmd.io/_uploads/SJnI6X-t2.png)

Bước vào challenge thì mình thấy có 2 chỗ để điền thông tin vào, do đó mình sẽ thử inject vào 2 chỗ trên, và mình nhận ra là có thể đưa payload vào phần ``page content``.

![](https://hackmd.io/_uploads/SkAGR7WY3.png)

Tiếp theo mình tìm payload phù hợp để gắn vào. Ở đây mình sử dụng payload sau: ``{{ cycler.__init__.__globals__.os.popen('id').read() }}``

Như ảnh trên thì trang web đã hiện ra id của nó. Tiếp theo mình sẽ list ra các file của trang web với payload sau: ``{{ cycler.__init__.__globals__.os.popen('ls -la').read() }}``

![](https://hackmd.io/_uploads/rkqqA7bYh.png)

Ở đây mình thấy có 1 file ``passwd`` khá là khả nghi nên truy cập thử xem sao.

![](https://hackmd.io/_uploads/By4p0X-tn.png)

Sau khi truy cập thì ta đã có được flag. Submit 25d thui !!!
