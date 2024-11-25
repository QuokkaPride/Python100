from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()
notify = NotificationManager()
flight_data = FlightData()

sheet_data = data_manager.get_sheet_data()
sheet_data = sheet_data["prices"]
for row in sheet_data:
    if row["iataCode"] == "":
        print(row["city"])
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.update_destination_code(row["id"], row["iataCode"])

# pprint(sheet_data)