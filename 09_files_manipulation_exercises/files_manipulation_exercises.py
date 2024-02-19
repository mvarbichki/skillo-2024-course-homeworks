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

# imports my validation module
from utilities import inputs_check, record_to_csv


def students_score_to_csv():
    # empty str triggers the while loop
    name = ""
    # keeps all user inputs. Used for the CSV saving
    students_scores_list = []
    print("Add student records and results. After you have added the desired records, type stop instead of a "
          "student's name and the record will be exported to CSV. The program ALLOWS student names duplication !\n")
    while name.lower() != "stop":
        name = input("Enter student name (or 'stop' to save and export the records): \n")
        # used to stop the cycle immediately if a stop is entered
        if name.lower() != "stop":
            score = input(f"Enter {name.title()} score: \n")
            correct_inputs = inputs_check(name, score)
            # checks for bad inputs. If such returns message
            if correct_inputs is True:
                # if no bad inputs append the record
                students_scores_list.append({"name": name.title(), "score": "{:.2f}".format(float(score))})
                print(f"Student {name} - appended\n")
            else:
                print(f"{correct_inputs}. You have to start over")
                return
    if students_scores_list:
        record_to_csv(students_scores_list)
        print("Exported to CSV")
    else:
        print("Empty record")
    return


# students_score_to_csv()

"""5. Design a program that reads a JSON file containing a list of products with names and prices. Calculate the 
total cost of all products and display it."""
import json
from utilities import read_json


def calculating_product_prices(arr: json):
    total_price = 0
    for row in read_json(arr):
        total_price += float(row.get("price"))

    return f"Total price of all products in the json file are: {'{:.2f}'.format(total_price)}"


print(calculating_product_prices("products.json"))
