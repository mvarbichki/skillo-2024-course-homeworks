"""Problem 1. Create a list with the numbers from 1 to 1000 and print it."""
lst = []


def append_range_to_lst(arr):
    for i in range(1, 1001):
        arr.append(i)
    return arr


print(append_range_to_lst(lst))
