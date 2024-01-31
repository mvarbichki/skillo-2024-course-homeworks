"""Problem 0: Write a program that takes an integer input from the user and checks if it's odd or even. Use an
if-else statement to print the result."""


def odd_or_even():
    # checks the user input
    try:
        num = int(input("Enter an integer: "))
        # check for even
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    # hande incorrect input type
    except ValueError:
        print("Wrong input type! Try again")


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
    # checks the user input
    try:
        answer = int(input("How much does 5 + 17 equal to (enter an integer): "))
        while answer != (5 + 17):
            answer = int(input("Incorrect. How much does 5 + 17 equal to (enter a integer): "))
        print(f"{answer} is the correct answer")
    # hande incorrect input type
    except ValueError:
        print("Wrong input type! Try again")


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


"""Problem 4: Design a Python program that simulates a simple guessing game. The program should generate a random 
number between 1 and 100 and ask the user to guess it. Provide hints like "Too high" or "Too low" until the user 
guesses the correct number. Use a while loop for this game."""
import random


def guess_random_number():
    # generates random number between 1 and 100
    random_num = random.randint(1, 100)
    # checks the user input
    try:
        answer = int(input("Guess the random number (enter an integer between 1 and 100): "))
        while answer != random_num:
            # compare the answer and the random number and gives hint
            if answer > random_num:
                answer = int(input("Too high. Try again (enter an integer between 1 and 100): "))
            elif answer < random_num:
                answer = int(input("Too low. Try again (enter an integer between 1 and 100): "))
        print(f"{answer} is the correct answer")
    # hande incorrect input type
    except ValueError:
        print("Wrong input type! Try again")


"""Problem 5: Modify problem 2 so that every time the user is prompted the problem is different. Think of a way to 
design that and come up with a proper solution for that."""


def modified_correct_answer():
    # dict of problems and answers
    problems = {
        "5 + 17": 22,
        "18 - 5": 13,
        "6 * 2": 12,
        "45 / 9": 5
    }

    # converts dict into list of tuples. Unpacks a random problem with its answer
    key_problem, val_answer = random.choice(list(problems.items()))

    # checks the user input
    try:
        guessing = int(input(f"How much does {key_problem} equal to (enter an integer): "))
        # until the problem answer is different from the input guessing, the problem will prompt
        while val_answer != guessing:
            guessing = int(input(f"Try again. How much does {key_problem} equal to (enter an integer): "))

        # prints the correct answer
        print(f"{val_answer} is the correct answer")
    # hande incorrect input type
    except ValueError:
        print("Wrong input type! Try again")


"""Problem 6: Write a Python program that takes an integer input from the user and prints the multiplication table 
for that number from 1 to 10 using a for loop."""


def input_multiplication_table():
    # checks the user input
    try:
        num = int(input("Enter an integer for multiplication table for it from 1 to 10: "))
        # iterate through range 1 - 10
        for i in range(1, 11):
            # multiplying the input with each iteration in the range
            print(f"{num} * {i} is: {i * num}")
    # hande incorrect input type
    except ValueError:
        print("Wrong input type! Try again")


"""Problem 7: Create a Python program that checks if a given integer is a prime number. Use a for loop to iterate 
through possible divisors and use an if-else statement to determine if it's prime."""


def find_the_prime():
    try:
        # increments each time if the num modulo division is equal to 0
        counter = 0
        num = int(input("Enter an integer for a prime number check: "))
        # skips the check if input is 1 or 0
        if (num == 1) or (num == 0):
            print(f"{num} is not prime")
        else:
            # since we skip 1, the iteration began in range from 2.
            # it's limited to the num + 1 to check division on itself
            for i in range(2, num + 1):
                # checks if the num divided without remainder and increment the counter var
                if num % i == 0:
                    counter += 1
                    # since we skip 1 it should modulo division only on itself to be prime
                    # if counter pass 1 the cycle will beak
                    if counter > 1:
                        break
            # after the cycle if the counter is equal to 1 the num is prime
            if counter == 1:
                print(f"{num} is prime")
            else:
                print(f"{num} is not prime")
    # hande incorrect input type
    except ValueError:
        print("Wrong input type! Try again")


"""Problem 8: Pattern Printing:
Write a program that takes an integer 'n' as input and prints the following pattern using nested for loops:
Expected output for input 5:
1
12
123
1234
12345
"""


def number_pattern():
    try:
        num = int(input("Enter an integer: "))
        # first cycle in range of the input
        for i in range(num):
            # the second cycle in range 1 (to begin from 1) is limited to the iteration of the first cycle plus two
            # additional  runs to equal the input
            for j in range(1, i + 2):
                # prints index of the second cycle on the same row
                print(j, end="")
            # used as a separator between the second cycle's iterations to print new iterations on the new line
            print()
    # hande incorrect input type
    except ValueError:
        print("Wrong input type! Try again")
