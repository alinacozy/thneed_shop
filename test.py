import sqlite3

from app import app
from database_connection import create_tables_if_not_exist, DATABASE_PATH
from product_queries import Order, find_order_by_id

with app.app_context():
    a = find_order_by_id(1)
    print(a.name)
    #print(a.get_ordered_products())
