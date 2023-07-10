from flask import Flask, render_template, abort, request

from product_queries import get_list_of_products, find_product_by_eng_name, decrease_product_count

from app import app


@app.route("/")
def main_page():
    return render_template("main_page.html", list_of_products=get_list_of_products())


@app.route("/product/<product_name>")
def product_page(product_name: str):
    product = find_product_by_eng_name(product_name)
    return render_template("product_page.html", product=product)


@app.route("/order/<product_name>", methods=['POST'])
def order_product_page(product_name: str):
    print(request.form)
    print(request.form.get('phone'))
    product = find_product_by_eng_name(product_name)
    if product.count < 1:  # вынести в отдельный метод
        abort(403)
    decrease_product_count(product)
    return render_template("order_product_page.html", product=product)


app.run(debug=True)
