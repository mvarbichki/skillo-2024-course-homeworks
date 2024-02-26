# Successfully setup PyCharm on your PC following the setup guide and then watch the intro tutorial.

"""Problem 1: Arithmetic Operations Write a Python script that creates two numerical variables and performs all
arithmetic operations on them, printing the results."""


def arithmetic_operators(num_one: float, num_two: float):
    # handle non str input
    try:
        no = float(num_one)
        nt = float(num_two)
    except ValueError:
        return "Enter numbers"

    addition = f"Addition: {'{:.2f}'.format(no + nt)}"
    subscription = f"Subscription: {'{:.2f}'.format(no - nt)}"
    multiplication = f"Multiplication: {'{:.2f}'.format(no * nt)}"
    exponential = f"Exponential: {'{:.2f}'.format(no ** nt)}"
    # handle division on zero
    if no == 0 or nt == 0:
        division = "Division: Can not division on 0"
        modulus = "Modulus: Can not division on 0"
        floor_div = "Floor division: can not division on 0"
    else:
        division = f"Division: {'{:.2f}'.format(no / nt)}"
        modulus = f"Modulus: {'{:.2f}'.format(no % nt)}"
        floor_div = f"Floor division: {'{:.2f}'.format(no // nt)}"

    return addition, subscription, multiplication, division, modulus, exponential, floor_div


# print(arithmetic_operators(input("Enter first numeric: "), input("Enter second numeric: ")))

"""Problem 2:
Write a Python script that creates 5 string variables of 5 bulgarian PINs ( ЕГН ) and 5 names in
tuples.
Finally insert only the pairs whose name begins with a vowel in a dictionary and print it."""

p1 = ("8807754693", "Sam")
p2 = ("9807654697", "Alex")
p3 = ("7806654693", "Mell")
p4 = ("8811757793", "Emo")
p5 = ("9507722693", "Olga")
# vowel for check
vowel = "aeiouAEIOU"
# persons list for check
persons_list = [p1, p2, p3, p4, p5]


# dict to store results
def vowel_names(vow: str, p_list: list):
    vowel_dict = dict()
    for person in p_list:
        # checks person first letter for vowel
        if person[1][0] in vow:
            # adds the person to the dict
            vowel_dict[person[0]] = person[1]
    return vowel_dict


# print(vowel_names(vowel, persons_list))
