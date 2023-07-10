from flask import abort

from database_connection import get_connection


class Product:
    def __init__(self, eng_name: str, rus_name: str, count: int, price: int):
        self.eng_name = eng_name
        self.rus_name = rus_name
        self.count = count
        self.price = price


def get_list_of_products() -> list[Product]:
    rows = get_connection().execute("select * from products").fetchall()
    result = []
    for row in rows:
        result.append(Product(*row))
    return result


def find_product_by_eng_name(product_name: str) -> Product:
    row = get_connection().execute(f"select * from products where eng_name='{product_name}'").fetchone()
    if row == None:
        abort(404)
    return Product(*row)


def decrease_product_count(product: Product):
    get_connection().execute(f"update products set count={product.count - 1} where eng_name='{product.eng_name}'")
    get_connection().commit()
