from utilities import string_list, punctuation_and_spaces_remover

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
