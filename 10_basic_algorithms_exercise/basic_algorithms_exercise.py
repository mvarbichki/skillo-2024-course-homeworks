from utilities import (string_list, punctuation_and_spaces_remover, is_int, is_word_len_equal,
                       letters_uniformity, is_str, is_same_str)

"""0. Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backward)."""


def is_palindrome(string: str):
    if is_str(string):
        clean_str = punctuation_and_spaces_remover(string)
        # reverse the string in var
        reversed_str = "".join([c for c in reversed(clean_str)])
        if clean_str == reversed_str:
            return f"'{string}' is palindrome"
        else:
            return f"'{string}' is NOT palindrome"
    return "The argument must be a string"


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
        return "The argument must be integer"


# print(is_prime(9))

"""2. Write a program to reverse a given string without using string slicing."""


def reverse_string(string: str):
    if is_str(string):
        reversed_str_list = [c for c in reversed(string)]
        return "".join(reversed_str_list)
    return "The argument must be a string"


# print(reverse_string(string_list[2]))


"""3. Create a program that checks if two given strings are anagrams of each other."""

anagrams_one = ("silent", "silent")
anagrams_two = ("funeral", "real fun")
anagrams_three = ("Church of Scientology", "rich-chosen goofy cult")

non_anagrams_one = ("pop", "mob")
non_anagrams_two = ("team", "beam")


def is_anagram(word_own: str, word_two: str):
    # allows to check for anagram if the arguments are string and not comparing the same string
    if is_str(word_own) and is_str(word_two) and not is_same_str(word_own, word_two):
        clean_word_one = punctuation_and_spaces_remover(word_own)
        clean_word_two = punctuation_and_spaces_remover(word_two)
        first_word_uniformity_compared_to_second = letters_uniformity(clean_word_one, clean_word_two)
        second_word_uniformity_compared_to_first = letters_uniformity(clean_word_two, clean_word_one)
        # if word lengths are not the same then they are not checked for anagrams
        if is_word_len_equal(clean_word_one, clean_word_two):
            # if no difference between the letters of both words then they are anagrams
            if first_word_uniformity_compared_to_second and second_word_uniformity_compared_to_first:
                return f"{word_own} and {word_two} are anagrams"
            else:
                return f"{word_own} and {word_two} are NOT anagrams"
        else:
            return f"Words are not the same length"

    else:
        return "The arguments are not string or comparing the same string"


# print(is_anagram(anagrams_three[1], anagrams_three[0]))

"""4. Write a program that counts the number of words in a given string."""


def count_words_in_str(string: str):
    if is_str(string):
        words_list = [w for w in string.split()]
        return f"There are/is {len(words_list)} words in the given string"
    return "The argument must be a string"


# print(count_words_in_str("3. Create a program that checks if two given strings are anagrams of each other."))

