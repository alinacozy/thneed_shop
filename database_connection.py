import sqlite3
from sqlite3 import Error
from flask import g

from app import app

DATABASE_PATH = "products.db"


def create_tables_if_not_exist(connection):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS products (
        end_name text PRIMARY KEY,
        rus_name text NOT NULL,
        count integer NOT NULL,
        price integer NOT NULL
    );
    """
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
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
