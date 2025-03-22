#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import requests
import os


flightSearch = FlightSearch()
flightData = FlightData()
data = DataManager()
notification = NotificationManager()

sheety_data = data.get()
# Changing the IATACODES to the correct code
counter = 2
for sheet in sheety_data:
    if sheet["iataCode"] == "":
        response = flightSearch.findIataCode(sheet["city"])
        sheet["iataCode"] = response
        push = {"sheet1": sheet}
        data.put(push,counter)


    least_cost = flightData.findFlight(destinationcity=sheet["iataCode"],num_adults= 1, max_price=1000)
    # pprint(least_cost)


    if float(sheet["cost"]) > float(least_cost):
        notification.send_message(sheet["city"], least_cost)
        sheet["cost"] = least_cost
        push = {"sheet1": sheet}
        data.put(push, counter)



    counter += 1

