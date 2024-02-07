"""Problem 1. Create a list with the numbers from 1 to 1000 and print it."""

lst = []


def append_range_to_lst(arr: list):
    try:
        for i in range(1, 1001):
            arr.append(i)
        return arr
    except AttributeError:
        return "Wring argument"


# print(append_range_to_lst(lst))

"""Problem 2. Reverse the order of the elements in the list from problem 1 and print the result."""


def reverse_lst(arr: list):
    try:
        arr.reverse()
        return arr
    except AttributeError:
        return "Wrong argument"


# print(reverse_lst(append_range_to_lst(lst)))

"""Problem 3. Given a list of words, create a new list containing the lengths of each word."""

words = ["pen", "desk", "bottle", "happiness"]


def length_of_words(arr: list):
    try:
        return [len(word) for word in arr]
    except TypeError:
        return "Wrong input"


# print(length_of_words(words))

"""Problem 3.1. Given a list of words, create a new dictionary mapping every word to it's length."""


def comp_convert_ls_world_length(arr: list):
    try:
        return {word: len(word) for word in arr}
    except TypeError:
        return "Wrong argument"


# print(comp_convert_ls_world_length(words))

"""Problem 4. Write a function that takes a list and returns the sum of all even numbers in the list."""
numbers_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def comp_sum_of_list_even(arr: list):
    try:
        even_lst = [num for num in arr if num % 2 == 0]
        # returns the usm of all even numbers
        return sum(even_lst)
    except TypeError:
        return "Wrong argument"


# print(comp_sum_of_list_even(numbers_lst))

"""Problem 5. Given a tuple of integers, find the maximum and minimum values without using built-in functions."""
import sys

numbers_tuple = (2, 4, 7, 1, -2, 5, 9, 93)


def tuple_min_max_values(arr: tuple):
    # presented vars with minimum and maximum system-allowed values ensure it will not skip any number from the tuple
    min_value = sys.maxsize
    max_value = -sys.maxsize

    try:
        for num in arr:
            # if the check number is higher/lower than the checked var it will become its new value
            if min_value > num:
                min_value = num
            if max_value < num:
                max_value = num
        return f"Min value is: {min_value} and max value is: {max_value}"
    except TypeError:
        return "Wrong argument"


# print(tuple_min_max_values(numbers_tuple))


"""Problem 6. Implement a basic queue structure ( as a global var ) by defining two functions `enqueue` and `dequeue."""

from queue import Queue

q_lst = Queue()


# adds task to the back of the queue
def enqueue(arr, task):
    return arr.put(task)


# gets task from the front of the queue
def dequeue(arr):
    return arr.get()


enqueue(q_lst, "task one")
enqueue(q_lst, "mid task")
enqueue(q_lst, "task two")

# print(dequeue(q_lst))
# print(dequeue(q_lst))
# print(dequeue(q_lst))

"""Problem 7. Create a dictionary that maps students to their bank account number. Some students may have multiple bank 
accounts."""

students = dict()


# takes a few arguments and maps them in dict. Does not check for identical records in the inner list (bank acc)
def students_bank_acc_mapper(arr: dict, student_name: str, bank_acc_name: str, bank_acc_number: str):
    # handles bad arguments
    try:
        # if the key in the dict (the student name) exist it will append to its value (the inner list). This adds
        # other bank accounts to the same student
        if [student_name for student in arr.keys() if student_name.lower() == student]:
            arr.get(student_name.lower()).append({bank_acc_name.lower(): bank_acc_number})
        # otherwise, adds a new student plus bank account (lower case) in the dict
        else:
            arr.update({student_name.lower(): [{bank_acc_name.lower(): bank_acc_number}]})
        return arr
    except (ValueError, AttributeError):
        return "Wrong arguments"


# students_bank_acc_mapper(students, "Peter", "acc1", "23424")
# students_bank_acc_mapper(students, "Peter", "acc2", "23424")
# students_bank_acc_mapper(students, "SAMMY", "acc2", "23424")
# print(students)

"""Problem 8. Think of a function that can hash lists. Implement it and test it."""


def hashing_lists(arr: list):
    try:
        # iterates in a given array. In sub-for-cycle iterates, all word's characters are converted in ascii, and write
        # them in list comprehension as separate sub-lists
        return [[ord(c) for c in word] for word in arr]
    except TypeError:
        return "Wrong argument"


def de_hashing_list(arr: list):
    try:
        # same process as in hashing_lists, but this time write ascii characters as str in sub-lists
        # (each word in separate list) and join the sub-lists in whole words
        return ["".join(chr(word) for word in c) for c in arr]
    except TypeError:
        return "Wrong arguments"


# print(hashing_lists(words))
# print(de_hashing_list(hashing_lists(words)))

"""Problem 9. Write a function that counts the frequency of each word in a given string and returns a dictionary with 
the result."""

sentence = "Today is a good day in a good neighborhood for a good person"


def word_frequency(arr: str):
    # handles bad arguments
    try:
        # splits single str in to a list. Dict comprehension to add each word as key and the counted frequency as value
        return {word: arr.split().count(word) for word in arr.split()}
    except AttributeError:
        return "Wrong argument"


# print(word_frequency(sentence))

"""Problem 10. Create two sets with some common elements and find their intersection."""
set_one = {"one", "two", "six"}
set_two = {"one", "two", "four", "six", "ten"}


def sets_intersection(first_arr: set, second_arr: set):
    # handles bad arguments
    try:
        # returns all elements that are in both sets
        return first_arr.intersection(second_arr)
    except AttributeError:
        return "Wrong arguments"


# print(sets_intersection(set_one, set_two))


"""11. Given two sets, write a function that determines if one set is a subset of the other."""


def sets_subset(first_arr: set, second_arr: set):
    try:
        # returns boolean if checked set elements are contained in the checking one
        return first_arr.issubset(second_arr)
    except AttributeError:
        return "Wrong arguments"


# print(sets_subset(set_one, set_two))
# print(sets_subset(set_two, set_one))


"""Problem 12. Write a function to remove duplicates from a list using a set."""

lst_of_duplicates = ["one", "one", "two", "two"]


def removing_duplicates(arr: list):
    try:
        # converts a list into a set to remove duplicates
        return set(arr)
    except TypeError:
        return "Wrong argument"


# print(removing_duplicates(lst_of_duplicates))


"""Problem 13. Use list comprehension to create a list of the squares of even numbers from 1 to 30."""


def pow_even_in_range():
    return [pow(num, 2) for num in range(1, 31) if num % 2 == 0]


# print(pow_even_in_range())


"""Problem 14. Given a list of words, create a dictionary where the keys are the words and the values are their 
lengths, using dictionary comprehension."""


def words_length_dict(arr: list):
    try:
        return {word: len(word) for word in arr}
    except TypeError:
        return "Wrong argument"


# print(words_length_dict(words))


"""Problem 15. Write a program that generates a set of prime numbers less than 100 using list comprehensions and 
sets."""


def find_prime(num):
    try:
        converted_num = int(num)
        if converted_num <= 1:
            return False
        else:
            for i in range(2, converted_num):
                if converted_num % i == 0:
                    return False
            else:
                return True
    except ValueError:
        return "Wrong input type! Try again"


def prime_1_100():
    # set comprehension prime numbers. Checks each num from the given range with find_prime function if true adds it
    return {num for num in range(2, 100) if find_prime(num)}

# print(prime_1_100())
