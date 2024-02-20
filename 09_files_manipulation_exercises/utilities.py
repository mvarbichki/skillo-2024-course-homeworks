import csv
import json
import xml.etree.ElementTree as Et


# my exceptions
class IsAlphabetic(Exception):
    def __init__(self, message):
        super().__init__(message)


class IsScoreRange(IsAlphabetic):
    pass


def inputs_check(name: str, score: str):
    try:
        float_score = float(score)
        # allows alphabetic for the name
        if not name.isalpha():
            raise IsAlphabetic("Name have to be alphabetic")
        # allows float score in range 1 to 10
        if not 1 <= float_score <= 10:
            raise IsScoreRange("Score have to be between 1 and 10")
    except ValueError:
        return "Score have to be float"
    except IsScoreRange as isr:
        return isr
    except IsAlphabetic as ia:
        return ia
    # if no exceptions return true
    else:
        return True


def record_to_csv(arr: list):
    with open("student_scores.csv", "w") as f:
        csv_file = csv.DictWriter(f, fieldnames=["name", "score"])
        # adds header
        csv_file.writeheader()
        # write to CSV file
        csv_file.writerows(arr)


def read_json(arr: json):
    with open(arr, "r") as f:
        return json.load(f)


def extract_data_from_xml(arr):
    tree = Et.parse(arr)
    root = tree.getroot()
    # returns list of tuples with name of the product and the price
    return [(product[0].text, product[1].text) for product in root]
