Source code:

```
@app.route('/')
def index():
    posts = [
        {'title': 'New blog post', 'content': 'This is my latest blog post.'},
        {'title': 'Another post', 'content': 'This is another blog post.'},
        {'title': 'Third post', 'content': 'This is the third post on my blog.'},
    ]
    template = """
        <html>
            <body>
                <h1>My Blog</h1>
                {% for post in posts %}
                    <h2>{{ post.title }}</h2>
                    <p>{{ post.content }}</p>
                {% endfor %}
            </body>
        </html>
    """
    return render_template_string(template, posts=posts)
```

Giả sử mình có một ứng dụng web Flask sử dụng Jinja2 để hiển thị các trang web. Tuy nhiên, ứng dụng trên chưa có các biện pháp để chống lại lỗ hổng SSTI. Do đó kẻ tấn công có thể sử dụng deep payload để tấn công vào.

Deep payload SSTI có thể giúp kẻ tấn công đọc tệp trên máy chủ hoặc thực thi mã từ xa.

Chẳng hạn như:

```http://localhost:5000/?post={{''.__class__.__mro__[1].__subclasses__()[414].__init__.__globals__['os'].popen('ls').read()}}```

Nó có thể thực thi lệnh ls trên máy chủ và trả về danh sách các tệp trên máy chủ. Điều này cho thấy rằng deep payload SSTI có tính phức tạp và nguy hiểm cao hơn so với các payload thông thường.
