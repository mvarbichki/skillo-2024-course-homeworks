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
    # hande incorrect input
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

