"""Problem 0:
Complete the following function so that it returns the sum of the elements in the list passed as an argument:

def sum_elements(arr):
result = 0
#insert code here
return result

# Tests
print(sum_elements([1,2,3,4])
print(sum_elements([0])
print(sum_elements([])
print(sum_elements([-1, 1])
"""


def sum_elements(arr):
    # sum array elements
    result = sum(arr)
    return result


"""Problem 1: Simple Calculator Function Define a function called `simple_calculator` that takes two numbers and an 
operator ('+', '-', '*', or '/') as arguments and returns the result of the operation."""
# imports our module
import operator


def simple_calculator(a, b, given_operator):
    # adds the needed operators in dict
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    # assigns the desired operator funct (the dict value) via the dict key (the given_operator argument)
    operator_funct = operators[given_operator]
    # returns the executed operator function
    return operator_funct(a, b)


print(simple_calculator(5, 2, "/"))

"""Problem 2: Area of Shapes: Create a module named `geometry` with functions to calculate the area of common shapes 
like a square, rectangle, triangle, and circle. Import this module and use it to calculate the areas of different 
shapes."""
# imports everything from geometry module
from geometry import *

print(area_of_square(5))
print(area_of_rectangle(4, 6))
print(area_of_triangle(6, 5.5))
print(area_of_circle(9))

"""Problem 3: Temperature Conversion: Write a program that converts temperatures between Celsius and Fahrenheit. 
Create two functions, one for each conversion, and use them in a program to convert temperatures provided by the 
user."""


def celsius_to_fahrenheit(celsius):
    # checks user input type
    try:
        # calculates Fahrenheit
        result = (float(celsius) * 9 / 5) + 32
        # returns the result formatted to one digit after the decimal
        return f"{'%.1f' % result} ºF"
    except ValueError:
        return "Wrong input type"


print(celsius_to_fahrenheit(input("Enter Celsius for conversion to Fahrenheit: ")))


def fahrenheit_to_celsius(fahrenheit):
    # checks user input type
    try:
        # calculates Celsius
        result = (float(fahrenheit) - 32) * 5 / 9
        # return the result formatted to one digit after decimal
        return f"{'%.1f' % result} °C"
    except ValueError:
        return "Wrong input type"


print(fahrenheit_to_celsius(input("Enter Fahrenheit for conversion to Celsius: ")))


"""Problem 4: Online Shopping Cart: Create a Python program that simulates an online shopping cart using a global 
dictionary variable. Every customer has unique id as a key. Define functions to add items to the cart, remove items, 
calculate the total price, and display the contents of the cart. Allow the user to interact with the cart by adding 
and removing items."""

# customers dict
customers = {
    "customer_one":
        {
            "milk": 4,
            "eggs": 6
        },

    "customer_two":
        {
            "bananas": 2,
            "meat": 15
        }

}


# sets the first argument as dict since we expect such data type
def add_item(customers_dict: dict, customer_id, item, price):
    # checks for wrong customer id and bad price type
    # item is left unchecked for bad input since there is no specific list of items to check for
    try:
        # gets customer cart
        customer = customers_dict[str(customer_id)]
        # adds the desired item to the cart with the expected data types
        customer.update({str(item): float(price)})
        return f"{item} added successfully to the {customer_id} cart: {customer}"
    # handles  wrong key and types
    except (KeyError, ValueError):
        return "Wrong arguments"


print(add_item(customers, "customer_one", "oranges", 7))


def remove_item(customers_dict: dict, customer_id, item):
    try:
        customer = customers_dict[str(customer_id)]
        customer.pop(str(item))
        return f"{item} removed successfully from {customer_id} cart: {customer}"
    except (KeyError, ValueError):
        return "Wrong arguments"


print(remove_item(customers, "customer_two", "meat"))


def calculate_item_price(customers_dict: dict, customer_id):
    try:
        customer = customers_dict[str(customer_id)]
        # returns the formatted sum of the customer items
        return f"{customer_id} has total items price: {'%.2f' % sum(customer.values())}"
    except (KeyError, TypeError):
        return "Wrong argument"


print(calculate_item_price(customers, "customer_two"))


def show_cart_contend(customers_dict: dict, customer_id):
    try:
        customer = customers_dict[str(customer_id)]
        return f"{customer_id} cart content: {customer}"
    except (KeyError, TypeError):
        return "Wrong argument"


print(show_cart_contend(customers, "customer_one"))
