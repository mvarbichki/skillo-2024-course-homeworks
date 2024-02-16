"""1. Create a Python script that reads a text file called "numbers.txt" containing integers and calculates their
sum."""


def sum_file(file_name):
    numbers_sum = 0
    with open(file_name, "r") as f:
        # gets each numbers row
        for row in f:
            # splits each row of numbers into lists by ","
            for num in row.split(","):
                # converts each number form the list into float and adds it to a var
                numbers_sum += float(num)
    return numbers_sum


# print(sum_file("numbers.txt"))

"""2. Write a program that reads a text file, "words.txt," and counts the number of words in it."""


def count_words_file(file_name):
    with open(file_name, "r") as f:
        # splits converts each file's row in to list of words
        # each list is counted via len and result appended in a list
        # returns the counted words as sum of the list
        return sum([len(row.split()) for row in f])


# print(count_words_file("words.txt"))


"""3. Create a Python script that prompts the user to enter student names and their corresponding scores, then stores 
this data in a CSV file called "student_scores.csv."""


class IsAlphabetic(Exception):
    def __init__(self, message):
        super().__init__(message)


class IsNegative(IsAlphabetic):
    pass


# TODO separate check from the program
def students_score():
    try:
        name = input("Enter your name: ")
        if not name.isalpha():
            raise IsAlphabetic("Name have to be alphabetic")
        score = float(input("Enter your score: "))
        if score < 1:
            raise IsNegative("Score have to be positive")
    except ValueError:
        return "Score have to be float"
    except IsNegative as ine:
        return ine
    except IsAlphabetic as ia:
        return ia


print(students_score())
