import sqlite3


class DatabaseConnector:

    def __init__(self, db_name: str):
        self.__bd_name = db_name
        self.__con = sqlite3.connect(self.__bd_name)
        self.__cur = self.__con.cursor()
        self.er = sqlite3.Error

    def db_commit(self):
        self.__con.commit()

    def db_close(self):
        self.__con.close()

    def db_execute(self, sql_statement: str):
        return self.__cur.execute(sql_statement)

    # option for fetch one or all
    def db_fetch(self, sql_statement: str, fetch_one: bool = None):
        execute = self.db_execute(sql_statement)
        if fetch_one:
            return execute.fetchone()
        else:
            return execute.fetchall()

    # handles sqlite3 errors
    def db_exceptions(self):
        return self.er


dc = DatabaseConnector("sqlite_exercises.db")

# create and populate the tables needed for the exercises
# dc.db_execute("CREATE TABLE IF NOT EXISTS employees(id integer primary key, employee, salary)")
# dc.db_execute("""INSERT INTO employees VALUES
#                                 (1, 'Kim', 3500),
#                                 (2, 'Sara', 6600),
#                                 (3, 'Ivan', 4750),
#                                 (4, 'Sam', 7000)
#                                 """)
#
# dc.db_execute("""CREATE TABLE IF NOT EXISTS products(id integer primary key,ProductName text, UnitPrice real,
# suppliedID integer,weight real, CategoryID integer)""")
# dc.db_execute("""INSERT INTO products VALUES
#                             (1, 'Laptop Asus HJ', 1350.00, 1, 2, 3),
#                             (2, 'Laptop HP YG', 1800.00, 1, 2.5, 3),
#                             (3, 'USB hub', 35.00, 1, 0.5, 2)
#                             """)
#
# dc.db_execute("""CREATE TABLE IF NOT EXISTS orders (id integer primary key, product text, ordered_on text)""")
# dc.db_execute("""INSERT INTO orders VALUES
#                             (1, 'bananas', '2007-01-01 10:00:00'),
#                             (2, 'apples', '2022-11-05 09:00:00'),
#                             (3, 'oranges', '2023-07-04 07:30:00')
#                             """)
# dc.db_commit()
