import os
import requests

class FlightSearch:
    AMADEUS_URL = "https://api.sandbox.amadeus.com/v1/reference/locations/cities"
    AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
    AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")

    headers = {
        "Authorization": f"Bearer {AMADEUS_API_KEY}"
    }

    def __init__(self):
        self.city_codes = {}

    def get_destination_code(self, city_name):
        if city_name in self.city_codes:
            return self.city_codes[city_name]
        else:
            response = requests.get(url=f"{FlightSearch.AMADEUS_URL}?q={city_name}", headers=FlightSearch.headers)
            data = response.json()
            self.city_codes[city_name] = data[0]["iataCode"]
            return data[0]["iataCode"]
