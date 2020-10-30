import requests

URL = "https://api.github.com"
PARAMS = {'address':'Madurai'}


def get_handler():

    resp = requests.get(url=URL)
    print(resp.json())


get_handler()