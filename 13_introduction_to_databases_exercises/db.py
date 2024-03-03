import sqlite3


class DatabaseConnector:

    def __init__(self, db_name: str):
        self.__bd_name = db_name
        self.__con = sqlite3.connect(self.__bd_name)
        self.__cur = self.__con.cursor()

    def db_commit(self):
        self.__con.commit()
        return "Committed"

    def db_close(self):
        self.__con.close()
        return "Closed"

    def db_execute(self, table_statement: str):
        self.__cur.execute(table_statement)
        return "Executed"


# different obj tables for each exercises
employees_table = DatabaseConnector("sqlite_exercises.db")
products_table = DatabaseConnector("sqlite_exercises.db")
orders_table = DatabaseConnector("sqlite_exercises.db")

# creates, insert and commit the tables
employees_table.db_execute("CREATE TABLE IF NOT EXISTS employees(id integer primary key, employee, salary)")
employees_table.db_execute("""INSERT INTO employees VALUES
                                (1, 'Kim', 3500),
                                (2, 'Sara', 6600),
                                (3, 'Ivan', 4750),
                                (4, 'Sam', 7000)
                                """)
employees_table.db_commit()

products_table.db_execute("""CREATE TABLE IF NOT EXISTS products(id integer primary key,ProductName text, UnitPrice real, 
suppliedID integer,weight real, CategoryID integer)""")
products_table.db_execute("""INSERT INTO products VALUES
                            (1, 'Laptop Asus HJ', 1350.00, 1, 2, 3),
                            (2, 'Laptop HP YG', 1800.00, 1, 2.5, 3),
                            (3, 'USB hub', 35.00, 1, 0.5, 2)
                            """)
products_table.db_commit()

orders_table.db_execute("""CREATE TABLE IF NOT EXISTS orders (id integer primary key, product text, ordered_on text)""")
orders_table.db_execute("""INSERT INTO orders VALUES
                            (1, 'bananas', '2007-01-01 10:00:00'),
                            (2, 'apples', '2022-11-05 09:00:00'),
                            (3, 'oranges', '2023-07-04 07:30:00')
                            """)
orders_table.db_commit()
