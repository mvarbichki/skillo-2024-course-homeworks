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
    # counts the correct answers
    answered_questions = 0
    # checks the user input
    try:
        print("Answer on following 4 questions")
        # after each correct answer a new will prompt
        answer = int(input("How much does 5 + 17 equal to (enter an integer): "))
        while answer != (5 + 17):
            answer = int(input("Incorrect. How much does 5 + 17 equal to (enter a integer): "))
        # adds the correct answer
        answered_questions += 1
        # tracks the progress
        print(f"{answer} is correct. Answered question {answered_questions} of 4")
        # asks new question
        answer = int(input("How much does 18 - 5 equal to (enter an integer): "))
        while answer != (18 - 5):
            answer = int(input("Incorrect. How much does 18 - 5 equal to (enter an integer): "))
        answered_questions += 1
        print(f"{answer} is correct. Answered question {answered_questions} of 4")
        answer = int(input("How much does 6 * 2 equal to (enter an integer): "))
        while answer != (6 * 2):
            answer = int(input("Incorrect. How much does 6 * 2 equal to (enter an integer): "))
        answered_questions += 1
        print(f"{answer} is correct. Answered question {answered_questions} of 4")
        answer = int(input("How much does 45 / 9 equal to (enter an integer): "))
        while answer != (45 / 9):
            answer = int(input("Incorrect. How much does 45 / 9 equal to (enter an integer): "))
        answered_questions += 1
        print(f"Answered question {answered_questions} of 4. Done")
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
