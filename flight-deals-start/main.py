#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import requests
import os


flightSearch = FlightSearch()
data = DataManager()
notification = NotificationManager()

sheety_data = data.get()
pprint(sheety_data)
# Changing the IATACODES to the correct code
counter = 2
for sheet in sheety_data:
    if sheet["iataCode"] == "":
        response = flightSearch.findIataCode(sheet["city"])
        sheet["iataCode"] = response
        push = {"sheet1": sheet}
        data.put(push,counter)

    least_cost = flightSearch.findFlight(sheet["iataCode"], 1, 1000)
    if float(sheet["cost"]) > float(least_cost):
        notification.send_message(sheet["city"], least_cost)
        sheet["cost"] = least_cost
        push = {"sheet1": sheet}
        data.put(push, counter)



    counter += 1

