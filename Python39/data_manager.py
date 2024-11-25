import requests
from pprint import pprint

class DataManager:
    SHEETY_GET_ENDPOINT = "https://api.sheety.co/a342ec99e6d9b58df8930172f4e6fb9a/241125FlightDeals/prices"
    SHEETY_POST_ENDPOINT = "https://api.sheety.co/a342ec99e6d9b58df8930172f4e6fb9a/241125FlightDeals/prices"
    SHEETY_PUT_ENDPOINT = "https://api.sheety.co/a342ec99e6d9b58df8930172f4e6fb9a/241125FlightDeals/prices/[Object ID]"
    GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1mNoApS-FOWSVxBv7Q5MlYuIyrF8Y5BVH765qJIezId4/edit?gid=0#gid=0"

    def __init__(self):
        self.destination_data = {}

    def get_sheet_data(self):
        response = requests.get(url=DataManager.SHEETY_GET_ENDPOINT)
        return response.json()