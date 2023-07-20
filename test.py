import sqlite3

from database_connection import create_tables_if_not_exist, DATABASE_PATH
from product_queries import Order, find_order_by_id

connection = sqlite3.connect(DATABASE_PATH)
create_tables_if_not_exist(connection)

a = find_order_by_id(1)
print (a)
#print(a.get_ordered_products())