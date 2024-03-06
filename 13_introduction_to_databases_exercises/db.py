import sqlite3


class DatabaseConnector:

    def __init__(self, db_name: str):
        self.__bd_name = db_name
        self.__con = sqlite3.connect(self.__bd_name)
        self.er = sqlite3.Error

    def db_commit(self):
        with self.__con as conn:
            conn.commit()

    def db_execute_insert(self, sql_statement: str, values: tuple):
        with self.__con as conn:
            cur = conn.cursor()
            return cur.execute(sql_statement, values)

    def db_execute_update(self, sql_statement: str):
        with self.__con as conn:
            cur = conn.cursor()
        return cur.execute(sql_statement)

    # option for fetch one or all
    def db_fetch(self, sql_statement: str, fetch_one: bool = None):
        with self.__con as conn:
            cur = conn.cursor()
            execute = cur.execute(sql_statement)
            if fetch_one:
                return execute.fetchone()
            else:
                return execute.fetchall()

    # handles sqlite3 errors
    def db_exceptions(self):
        return self.er


dc = DatabaseConnector("sqlite_exercises.db")

# create and populate the tables needed for the exercises
# dc.db_execute_update("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, employee TEXT, salary REAL)")
# dc.db_execute_update("""INSERT INTO employees VALUES
#                                 (1, 'Kim', 3500),
#                                 (2, 'Sara', 6600),
#                                 (3, 'Ivan', 4750),
#                                 (4, 'Sam', 7000)
#                                 """)
#
# dc.db_execute_update("""CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY,ProductName TEXT, UnitPrice REAL,
# suppliedID INTEGER,weight REAL, CategoryID INTEGER)""")
# dc.db_execute_update("""INSERT INTO products VALUES
#                             (1, 'Laptop Asus HJ', 1350.00, 1, 2, 3),
#                             (2, 'Laptop HP YG', 1800.00, 1, 2.5, 3),
#                             (3, 'USB hub', 35.00, 1, 0.5, 2)
#                             """)
#
# dc.db_execute_update("""CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, product TEXT, ordered_on TEXT)""")
# dc.db_execute_update("""INSERT INTO orders VALUES
#                             (1, 'bananas', date('2007-01-01 10:00:00')),
#                             (2, 'apples', date('2022-11-05 09:00:00')),
#                             (3, 'oranges', date('2023-07-04 07:30:00'))
#                             """)
# dc.db_commit()
