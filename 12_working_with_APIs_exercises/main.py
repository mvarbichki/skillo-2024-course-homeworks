"""Problem 0:
Choose a public API of your choice (e.g., weather, news, or any other available API).
- Write a Python program that makes a GET request to the chosen API.
- Retrieve data from the API and display specific information from the response.
- Ensure error handling for cases where the request may fail.
- Implement a feature that allows users to interact with the data (e.g., search, filter, or manipulate the JSON data).
"""

from breeds import DogBreeds

breeds = DogBreeds()

print(breeds.get_breeds())
print(breeds.search_breed("boxer"))
