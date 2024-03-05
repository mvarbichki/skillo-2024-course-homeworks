from db_manipulations import get_employees_and_salary, db_execute_statements_insert, db_execute_statements_update

"""Problem 0: Select
Write a SQL query to retrieve the names and salaries of all employees in the "Employees" table."""

# print(get_employees_and_salary("""SELECT * FROM employees"""))


"""Problem 1: Insert Add a new product to the "Products" table. The product details are as follows: ProductName is 
"Laptop Mitsubishi XS200" UnitPrice is 999.99, supplied ID is 3, quantity per unit is 3 kg package, and CategoryID is 
2."""

# print(db_execute_statements_insert("""INSERT INTO products VALUES
#                              (?, ?, ? ,? ,? ,?)
#                              """, (4, 'Laptop Mitsubishi XS200', 999.99, 3, 3, 2)))

"""Problem 2: Update
Update the price of all products in the "Products" table with CategoryID 3 to be 10% higher."""

# print(db_execute_statements_update("""UPDATE products
#                             SET UnitPrice = UnitPrice + (UnitPrice * 0.1)
#                             WHERE CategoryID = 3"""))

"""Problem 3: Delete
Delete all orders from the "Orders" table that were placed before January 1, 2023."""

"""Problem 4: Select with WHERE
Retrieve the names and prices of products in the "Products" table with a price higher than $50."""