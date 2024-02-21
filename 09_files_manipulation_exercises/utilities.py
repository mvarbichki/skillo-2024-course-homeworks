import csv
import json
import xml
import xml.etree.ElementTree as Et
from custom_exceptions import InRange, IsAlphabetic


def inputs_check(name: str, score: str):
    try:
        float_score = float(score)
        # allows alphabetic for the name
        if not name.isalpha():
            raise IsAlphabetic("Name have to be alphabetic")
        # allows float score in range 1 to 10
        if not 1 <= float_score <= 10:
            raise InRange("Score have to be between 1 and 10")
    except ValueError:
        return "Score have to be float"
    except InRange as ir:
        return ir
    except IsAlphabetic as ia:
        return ia
    # if no exceptions return true
    else:
        return True


def write_to_csv(file: csv, arr: list, fieldnames_lst: list):
    with open(file, "w") as f:
        csv_file = csv.DictWriter(f, fieldnames=fieldnames_lst)
        # adds header
        csv_file.writeheader()
        # write to CSV file
        csv_file.writerows(arr)


def read_from_csv(file: csv):
    with open(file, "r", newline="") as f:
        csv_file = csv.reader(f)
        # skips header
        next(csv_file, None)
        # returns key, values in a list of tuples
        return [(k, v) for k, v in csv_file]


def read_json(file: json):
    with open(file, "r") as f:
        return json.load(f)


def extract_data_from_xml(file: xml):
    tree = Et.parse(file)
    root = tree.getroot()
    # returns list of tuples with name of the product and the price
    return [(product[0].text, product[1].text) for product in root]


# calculates salary and bonus
def salary_bonus_calculation(salary: float, bonus: float):
    salary += salary * bonus
    return salary


# validates the bonus
def if_bonus(bonus_type: float):
    try:
        # bonus have to be in range 0.1 - 0.9
        if not 0.1 <= float(bonus_type) <= 0.9:
            raise InRange("Bonus have to be between 0.1 and 0.9")
    except InRange as ir:
        return ir
    except ValueError:
        return "Bonus have to be float"
    else:
        return True


def avg_scores_calculation(arr: list):
    return sum(arr) // len(arr)
