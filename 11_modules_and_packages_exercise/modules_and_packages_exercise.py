"""1. Install the requests package in python
2. Make a request to `https://reqbin.com/echo/get/json`
3. Save the response as a json file called response.json"""

import requests

url = "https://reqbin.com/echo/get/json"


# header argument allows the URL request
def make_request(url_str: str):
    get_url = requests.get(url_str,
                           headers={
                               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 "
                                             "Safari/537.36"
                           }
                           )
    # if status code is successful return the url content
    if get_url.status_code == 200:
        return get_url.text
    else:
        return "Bad request"


def write_to_json(url_content: str):
    if url_content != "Bad request":
        with open("response.json", "w") as f:
            f.write(url_content)
            return "Json file exported"
    return "URL request problem. Json export failed"


url_extracted_content = make_request(url)
# print(write_to_json(url_extracted_content))
