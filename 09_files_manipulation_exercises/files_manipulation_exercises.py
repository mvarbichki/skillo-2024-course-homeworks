import json

from utilities import inputs_check, write_to_csv, read_json, extract_data_from_xml, read_from_csv, \
    salary_bonus_calculation, if_bonus, avg_scores_calculation

"""1. Create a Python script that reads a text file called "numbers.txt" containing integers and calculates their
sum."""


def sum_file(file):
    numbers_sum = 0
    with open(file, "r") as f:
        # gets each numbers row
        for row in f:
            # splits each row of numbers into lists by ","
            for num in row.split(","):
                # converts each number form the list into float and adds it to a var
                numbers_sum += float(num)
    return numbers_sum


# print(sum_file("numbers.txt"))

"""2. Write a program that reads a text file, "words.txt," and counts the number of words in it."""


def count_words_file(file):
    with open(file, "r") as f:
        # splits converts each file's row in to list of words
        # each list is counted via len and result appended in a list
        # returns the counted words as sum of the list
        return sum([len(row.split()) for row in f])


# print(count_words_file("words.txt"))


"""3. Create a Python script that prompts the user to enter student names and their corresponding scores, then stores 
this data in a CSV file called "student_scores.csv."""


# imports my validation module


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
        write_to_csv("student_scores.csv", students_scores_list, ["name", "score"])
        print("Exported to CSV")
    else:
        print("Empty record")
    return


# students_score_to_csv()

"""5. Design a program that reads a JSON file containing a list of products with names and prices. Calculate the 
total cost of all products and display it."""


def calculating_product_prices(arr):
    json_file = read_json(arr)
    total_price_list = sum([price.get("price") for price in json_file])
    return f"Total price of all products: {'{:.2f}'.format(total_price_list)}"


# print(calculating_product_prices("products.json"))


"""6. Write a Python script that reads a JSON file, "contacts.json," containing contact information (name, email, 
phone)."""


def read_contacts(arr):
    # unpack name, email and phone for each person in list of tuples
    return [(row.get("name"), row.get("email"), row.get("phone")) for row in read_json(arr)]


# for contact in read_contacts("contacts.json"):
#    print(f"Name: {contact[0]}, email: {contact[1]}, phone: {contact[2]} ")

"""8. Provide an example XML file, "inventory.xml," that represents a list of products in a store. Write a Python 
program to read this XML file and print the names and prices of all products."""


def read_xml(file):
    result_list = []
    for inventory in extract_data_from_xml(file):
        result_list.append(inventory)
    return result_list


# for item in read_xml("inventory.xml"):
#    print(f"{item[0]}: {item[1]}$")

"""4. Write a program that reads a CSV file called "employee_data.csv," and for each employee, calculates their total 
salary (considering base salary and bonuses) and saves it in a new CSV file called "total_salaries.csv."""


def employee_salary_csv(file, bonus_percentage: float):
    valid_bonus = if_bonus(bonus_percentage)
    if valid_bonus is True:
        employee_total_salary_list = []
        for name, salary in read_from_csv(file):
            total_salary = salary_bonus_calculation(salary=float(salary), bonus=bonus_percentage)
            # appends dicts of employee name and total in a list
            employee_total_salary_list.append(
                {"Employee": name, "Total salary": total_salary}
            )
        # writes processed data to a new csv file
        write_to_csv("total_salaries.csv", employee_total_salary_list, ["Employee", "Total salary"])
        return "total_salaries.csv exported"
    else:
        return valid_bonus


# print(employee_salary_csv("employee_data.csv", 0.2))


"""7. Create a CSV file, "student_data.csv," with student names and their corresponding JSON data containing exam 
scores. Write a program that reads the CSV file and calculates the average score for each student."""


def average_students_score(file):
    student_exam_score_list = read_from_csv(file)
    result_list = []
    for student in student_exam_score_list:
        json_exam_scores = json.loads(student[1])
        # gets all student scores in a list
        student_scores_list = [score for score in json_exam_scores.values()]
        # calculates avg score
        average_score = avg_scores_calculation(student_scores_list)
        # appends each student and avg score in a result list
        result_list.append(f"Student {student[0]} has an average score: {average_score}")
    return result_list


# print(average_students_score("student_data.csv"))
