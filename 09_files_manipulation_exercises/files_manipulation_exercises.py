"""1. Create a Python script that reads a text file called "numbers.txt" containing integers and calculates their
sum."""


def sum_file(file_name):
    with open(file_name, "r") as f:
        res = [int(num) for num in f]
    return sum(res)


# print(sum_file("numbers.txt"))
