"""Problem 0:
Fix the mistakes in the following snippet:
items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
for item in items.keys()
income = 0
qty = input(f"How many {item}s have you sold? ")
income = income + qty * items[item]
print(f"\nThe income today was £{income:0.2f}")"""


# custom-made class for handling negative int
class NegativeValue(Exception):
    def __init__(self, message):
        super().__init__(message)


items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}


def income_calculation(arr: dict):
    # moves income out of for cycle
    income = 0
    # handles wrong input type
    try:
        for item in arr.keys():
            qty = int(input(f"How many {item}s have you sold? "))
            # handles negative values, but allows 0
            if qty < 0:
                raise NegativeValue("Input can not negative")
            income += qty * arr[item]
        return f"\nThe income today was £{income:0.2f}"
    except ValueError:
        return "You have to enter an integer"
    except NegativeValue as nv:
        return nv


# print(income_calculation(items))

"""Problem 1:
Rewrite the following function so it is exception safe
def get_integer_input():
num = int(input("Enter an integer: "))
return num
number = get_integer_input()
print("You entered:", number)"""


def get_integer_input():
    # try/except to check for correct type
    try:
        num = int(input("Enter an integer: "))
        return num
    except ValueError:
        return "Wrong type"


number = get_integer_input()
# print("You entered:", number)
