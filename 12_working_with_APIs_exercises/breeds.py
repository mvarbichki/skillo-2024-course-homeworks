import requests
from utilities import UnsuccessfulRequest, is_str


class DogBreeds:
    def __init__(self):
        self.__dog_breeds_url = "https://dog.ceo/api/breeds/list/all"

    def get_breeds(self):
        response = requests.get(self.__dog_breeds_url)
        # checks if response is successful
        if response.ok:
            breeds = response.json()
            # gets just the breed names from the response
            breeds_name = breeds.get("message")
            # returns as class obj the desired response
            return BreedsResponse(
                breeds=list(breeds_name.keys())
            )
        else:
            # if request is unsuccessful retunr the code
            raise UnsuccessfulRequest(response.status_code)

    def search_breed(self, searched_breed: str):
        if is_str(searched_breed):
            all_breads = self.get_breeds()
            if searched_breed.lower() in all_breads.get_breeds_list():
                return f"Found: {searched_breed}"
            else:
                return "No result found"
        else:
            return "Incorrect argument type for searching"


class BreedsResponse:
    def __init__(self, breeds: list):
        self.__breeds = breeds

    def __str__(self):
        return f"Dogs breed names: {self.__breeds}"

    # returns the result of breeds in list
    def get_breeds_list(self):
        return self.__breeds
