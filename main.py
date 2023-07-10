from flask import Flask, render_template, abort, request


class Product:
    def __init__(self, eng_name: str, rus_name: str, count: int):
        self.eng_name = eng_name
        self.rus_name = rus_name
        self.count = count


list_of_products = [
    Product("thneed", "Всемнужка", 3214545),
    Product("lorax", "Лоракс", 1),
    Product("tree", "Дерево", 0),
    Product("stray_kids", "Стрей Кидс", 8),
    Product("alina", "Алина", 1),
]

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main_page.html", list_of_products=list_of_products)


def find_product_by_eng_name(product_name: str) -> Product:
    for product in list_of_products:
        if product.eng_name == product_name:
            return product
    abort(404)


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
    product.count -= 1  # вынести в отдельную функцию
    return render_template("order_product_page.html", product=product)


app.run(debug=True)

