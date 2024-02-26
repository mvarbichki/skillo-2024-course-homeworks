from utilities import (palindrome_string_list, punctuation_and_spaces_remover, is_int, is_str, is_same_str,
                       read_from_csv, read_from_json, write_to_csv, two_sum_unique_pairs, sum_pairs_match, is_int_arr,
                       reverse_str)

"""0. Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backward)."""


def is_palindrome(string: str):
    if is_str(string):
        clean_str = punctuation_and_spaces_remover(string)
        reversed_str = reverse_str(clean_str)
        if is_same_str(clean_str, reversed_str):
            return f"'{string}' is palindrome"
        else:
            return f"'{string}' is NOT palindrome"
    return "The argument must be a string"


# print(is_palindrome(palindrome_string_list[6]))

"""1. Write a function that checks if a given number is prime or not."""


# already solved this problem earlier in the course. Here I tried to improve the solution
def is_prime(number: int):
    # argument validation
    if is_int(number):
        # if number is 2 or above proceed with prime check
        if not number < 2:
            # list comprehension must remain empty so the number can be prime
            division_remainder = [i for i in range(2, number) if number % i == 0]
            if not division_remainder:
                return f"{number} is prime"
            return f"{number} is not prime"
        else:
            return f"{number} is not prime"
    else:
        return "The argument must be integer"


# print(is_prime(9))

"""2. Write a program to reverse a given string without using string slicing."""


def reverse_string(string: str):
    if is_str(string):
        reversed_str = reverse_str(string)
        return reversed_str
    return "The argument must be a string"


# print(reverse_string(palindrome_string_list[2]))


"""3. Create a program that checks if two given strings are anagrams of each other."""

anagrams_one = ("silent", "listen")
anagrams_two = ("funeral", "real fun")
anagrams_three = ("Church of Scientology", "rich-chosen goofy cult")
non_anagrams_two = ("team", "beam")
# after reworking is_anagram now catches cases as non_anagrams_one with identical letters
non_anagrams_one = ("pop", "oop")


def is_anagram(first_str: str, second_str: str):
    # allows to check for anagram if the arguments are string and not comparing the same string
    if is_str(first_str) and is_str(second_str) and not is_same_str(first_str, second_str):
        # sorting the results to be compared as a same str
        clean_str_one = sorted(punctuation_and_spaces_remover(first_str))
        clean_str_two = sorted(punctuation_and_spaces_remover(second_str))
        if is_same_str(clean_str_one, clean_str_two):
            return f"{first_str} and {second_str} are anagrams"
        else:
            return f"{first_str} and {second_str} are NOT anagrams"
    else:
        return "The arguments are not string or comparing the same string"


# print(is_anagram(non_anagrams_one[0], non_anagrams_one[1]))

"""4. Write a program that counts the number of words in a given string."""


def count_words_in_str(string: str):
    if is_str(string):
        words_list = [w for w in string.split()]
        return f"There are/is {len(words_list)} words in the given string"
    return "The argument must be a string"


# print(count_words_in_str("3. Create a program that checks if two given strings are anagrams of each other."))

"""5. Create a program that reads a CSV file, "sales.csv," containing sales data, and a JSON file, "products.json,
" with product information. Calculate the total revenue for each product and save it in a new CSV file called 
"product_revenue.csv."""


def total_revenue_export(csv_file, json_file):
    csv_contend = read_from_csv(csv_file)
    json_contend = read_from_json(json_file)
    result_list = []
    for csv_row in csv_contend:
        product_name_in_csv = csv_row[0]
        price_in_csv = int(csv_row[1])
        for json_row in json_contend:
            price_in_json = json_row.get("price")
            if product_name_in_csv == json_row.get("product"):
                result_list.append(
                    {"product": product_name_in_csv, "revenue": str(float(price_in_json * price_in_csv))}
                )
    return result_list


total_revenue_result = total_revenue_export("sales.csv", "products.json")
# print(write_to_csv("product_revenue.csv", total_revenue_result, ["product", "revenue"]))


"""6. Develop a Python script that reads a JSON file called "inventory.json" with information about products and 
their quantities. Create a new CSV file, "low_stock.csv," containing the names of products with a quantity less than 
10."""


def low_stocks(filename):
    products = read_from_json(filename)
    low_stocks_list = [
        {
            "product": product.get("product"),
            "quantity": product.get("quantity")
        }
        for product in products
        if product.get("quantity") < 10
    ]
    return low_stocks_list


low_stocks_result = low_stocks("inventory.json")
# print(write_to_csv("low_stock.csv", low_stocks_result, ["product", "quantity"]))


"""7. Write a program that is given a number and an array and checks if there is a pair of numbers in the array that 
has a sum equal to the given number. ( two-sum problem )"""


def two_sum_problem(number: int, arr: list):
    if is_int(number) and is_int_arr(arr):
        pairs_list = sum_pairs_match(number, arr)
        if pairs_list:
            return f"{number} sum pairs are: {two_sum_unique_pairs(pairs_list)}"
        return f"No match for {number}"
    else:
        return "The arguments must be an integer or array of integers"


print(two_sum_problem(7, [7, 3, 4, 6, 2, "3", 10]))
print(two_sum_problem("t", [7, 3, 4, 6, 2, 3, 10]))
print(two_sum_problem(7, [7, 3, 4, 6, 2, 3, 10]))
print(two_sum_problem(8, [7, 3, 4, 6, 2, 3, 10]))
print(two_sum_problem(10, [7, 3, 4, 6, 2, 3, 10]))
print(two_sum_problem(3, [7, 3, 4, 6, 2, 3, 10]))
