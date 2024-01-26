"""Problem 0: Write a program that takes an integer input from the user and checks if it's odd or even. Use an
if-else statement to print the result."""


def odd_or_even():
    # try the user input
    try:
        num = int(input("Enter a integer: "))
        # check for even
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    # hande incorrect input type
    except ValueError:
        print("Wrong input type try again")


"""Problem 1: Write a Python program to find the sum of all even numbers from 1 to 100 using a loop. Make use of 
control flow constructs like the for loop and conditional statements."""


def even_numbers_sum():
    # contains the sum of the even numbers
    even_sum = 0
    for num in range(1, 101):
        # finds even numbers
        if num % 2 == 0:
            # adding the even num to the sum var
            even_sum += num

    print(f"The sum of all even numbers from 1 to 100 is: {even_sum}")


"""Problem 2: Write a Python script that prompts the user in the console a simple problem ( how much does 5 + 17 
equal to ) until the user provides a correct answer."""


def correct_answer():
    # try the user input.
    try:
        answer = int(input("How much does 5 + 17 equal to (enter a integer): "))
        while answer != (5 + 17):
            answer = int(input("Incorrect. How much does 5 + 17 equal to (enter a integer): "))
        print(f"{answer} is the correct answer")
    # hande incorrect input type
    except ValueError:
        print("Wrong input type try again")


"""Problem 3: Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is 
divisible by 3, "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5."""


def fizz_buzz():
    for num in range(1, 1001):
        # checks first the AND condition otherwise it would be covered by the other two cases
        if (num % 3 == 0) and (num % 5 == 0):
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
