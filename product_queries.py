from flask import abort

from database_connection import get_connection


class Product:
    def __init__(self, eng_name: str, rus_name: str, count: int, price: int):
        self.eng_name = eng_name
        self.rus_name = rus_name
        self.count = count
        self.price = price

    def decrease_product_count(self):
        get_connection().execute(
            f"update products set count={self.count - 1} where eng_name='{self.eng_name}'")
        get_connection().commit()


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


class Order:
    def __init__(self, order_id: int, name: str, phone: int, email: int):
        self.order_id = order_id
        self.name = name
        self.phone = phone
        self.email = email

    def get_ordered_products(self) -> list[Product]:
        get_products_sql = f"""SELECT
            products.eng_name,
            products.rus_name,
            products.count,
            products.price
            
            FROM products
            INNER JOIN order_product
            ON products.eng_name = order_product.product_name
            WHERE order_id = '{self.order_id}'
        """
        rows = get_connection().execute(get_products_sql).fetchall()
        result = []
        for row in rows:
            result.append(Product(*row))
        return result


def find_order_by_id(id: int) -> Order:
    row = get_connection().execute(f"select * from orders where order_id='{id}'").fetchone()
    if row == None:
        abort(404)
    return Order(*row)