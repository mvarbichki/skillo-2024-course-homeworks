"""Problem 1. Create a list with the numbers from 1 to 1000 and print it."""
lst = []


def append_range_to_lst(arr):
    for i in range(1, 1001):
        arr.append(i)
    return arr


# print(append_range_to_lst(lst))

"""Problem 2. Reverse the order of the elements in the list from problem 1 and print the result."""


def reverse_lst(arr):
    arr.reverse()
    return arr


reversed_lst = reverse_lst(append_range_to_lst(lst))
# print(reversed_lst)

"""Problem 3. Given a list of words, create a new list containing the lengths of each word."""

words = ["pen", "desk", "bottle", "happiness"]


def length_of_words(arr):
    return [len(word) for word in arr]


print(length_of_words(words))

