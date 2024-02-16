"""1. Create a Python script that reads a text file called "numbers.txt" containing integers and calculates their
sum."""


def sum_file(file_name):
    with open(file_name, "r") as f:
        res = [int(row) for row in f]
    return sum(res)


# print(sum_file("numbers.txt"))


"""2. Write a program that reads a text file, "words.txt," and counts the number of words in it."""


def count_words_file(file_name):
    with open(file_name, "r") as f:
        # splits converts each file's row in to list of words
        # each list is counted via len and result appended in a list
        # returns the counted words as sum of the list
        return sum([len(row.split()) for row in f])


print(count_words_file("words.txt"))
