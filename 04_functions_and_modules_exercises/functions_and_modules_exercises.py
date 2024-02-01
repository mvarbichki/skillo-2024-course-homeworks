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
# operator module
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


# print(simple_calculator(5, 2, "/"))

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