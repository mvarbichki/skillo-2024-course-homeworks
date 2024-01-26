# Successfully setup PyCharm on your PC following the setup guide and then watch the intro tutorial.

"""Problem 1: Arithmetic Operations Write a Python script that creates two numerical variables and performs all
arithmetic operations on them, printing the results."""


def arithmetic_operators(num_one, num_two):
    # handle non str input
    try:
        no = int(num_one)
        nt = int(num_two)
    except:
        return "Enter numbers"

    addition = f"Addition:  {no + nt}"
    subscription = f"Subscription: {no - nt}"
    multiplication = f"Multiplication: {no * nt}"
    exponential = f"Exponential: {no ** nt}"
    # handle division on zero
    if no == 0 or nt == 0:
        division = "Division: Can not division on 0"
        modulus = "Modulus: Can not division on 0"
        floor_div = "Floor division: can not division on 0"
    else:
        division = f"Division: {no / nt}"
        modulus = f"Modulus: {no % nt}"
        floor_div = f"Floor division: {no // nt}"

    return addition, subscription, multiplication, division, modulus, exponential, floor_div


print(arithmetic_operators(input("Enter first numeric: "), input("Enter second numeric: ")))