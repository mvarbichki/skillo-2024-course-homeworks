"""1. Install the requests package in python
2. Make a request to `https://reqbin.com/echo/get/json`
3. Save the response as a json file called response.json"""

import requests
import json


url = "https://reqbin.com/echo/get/json"


def make_request(url_str: str):
    get_url = requests.get(url_str)
    return get_url.text


def write_to_json(url_content: str):
    with open("response.json", "w") as f:
        json_object = json.dumps(url_content)
        f.write(json_object)
        return "Json file exported"


url_extracted_content = make_request(url)
print(write_to_json(url_extracted_content))
