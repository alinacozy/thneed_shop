import sqlite3

from database_connection import get_connection, DATABASE_PATH, create_tables_if_not_exist

connection = sqlite3.connect(DATABASE_PATH)
create_tables_if_not_exist(connection)

# connection.execute("""
# insert into products values
# ('pin',	'Значок',	19,	300),
# ('tree',	'Дерево',	0,	5),
# ('stray_kids',	'Стрей Кидс',	7,	99999),
# ('lorax',	'Лоракс',	1,	1000),
# ('thneed',	'Всемнужка',	3170,	500)
# """)
connection.execute("""
insert into products values
('kitten',	'Котёнок',	20,	699),
('mouse',	'Мышь',	0,	70),
('banana',	'Банан',	1000,	10),
('jax',	'Джекс',	1,	1),
('money', 'Деньги',	289177,	100000)
""")
connection.commit()
