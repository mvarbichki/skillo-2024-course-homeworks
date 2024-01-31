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
