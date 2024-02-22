from utilities import string_list, punctuation_and_spaces_remover, is_int

"""0. Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backward)."""


def is_palindrome(string: str):
    clean_str = punctuation_and_spaces_remover(string)
    # reverse the string in var
    reversed_str = "".join([c for c in reversed(clean_str)])
    if clean_str == reversed_str:
        return f"'{string}' is palindrome"
    else:
        return f"'{string}' is NOT palindrome"


# print(is_palindrome(string_list[6]))

"""1. Write a function that checks if a given number is prime or not."""


# already solved this problem earlier in the course. Here I tried to improve the solution
def is_prime(number: int):
    # argument validation
    if is_int(number):
        # if number is 2 or above proceed with prime check
        if not number < 2:
            # list comprehension must remain empty so the number can be prime
            division_remainder = [i for i in range(2, number) if number % i == 0]
            if not division_remainder:
                return f"{number} is prime"
            return f"{number} is not prime"
        else:
            return f"{number} is not prime"
    else:
        return "Argument must be integer"


# print(is_prime(9))

"""2. Write a program to reverse a given string without using string slicing."""


def reverse_string(string: str):
    reversed_str_list = [c for c in reversed(string)]
    return "".join(reversed_str_list)


# print(reverse_string(string_list[2]))
