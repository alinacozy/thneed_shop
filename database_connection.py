import sqlite3
from sqlite3 import Error
from flask import g

from app import app

DATABASE_PATH = "products.db"


def create_tables_if_not_exist(connection):
    create_products_sql = """
    CREATE TABLE IF NOT EXISTS products (
        eng_name text PRIMARY KEY,
        rus_name text NOT NULL,
        count integer NOT NULL,
        price integer NOT NULL
    );
    """
    create_orders_sql = """CREATE TABLE IF NOT EXISTS orders (
        order_id integer PRIMARY KEY,
        name text NOT NULL,
        phone text NOT NULL,
        email text NOT NULL
    );
    """
    create_order_product_sql = """CREATE TABLE order_product(
    order_id integer,
    product_name text,
    PRIMARY KEY (order_id, product_name),
    FOREIGN KEY (order_id) 
        REFERENCES orders (order_id) 
            ON DELETE CASCADE 
            ON UPDATE NO ACTION,
    FOREIGN KEY (product_name) 
        REFERENCES products (eng_name) 
            ON DELETE CASCADE 
            ON UPDATE NO ACTION
    );
    """
    try:
        c = connection.cursor()
        c.execute(create_products_sql)
        c.execute(create_orders_sql)
        c.execute(create_order_product_sql)
    except Error as e:
        print(e)


def get_connection():
    connection = getattr(g, '_database', None)
    if connection is None:
        connection = sqlite3.connect(DATABASE_PATH)
        create_tables_if_not_exist(connection)
        g._database = connection
    return connection


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
