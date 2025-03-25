import requests
import os
from dotenv import find_dotenv, load_dotenv
from flight_search import FlightSearch
from pprint import pprint

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

DALLAS_IATA_CODE = "DFW"

API_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_DESTINATION_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_HEADER = "https://test.api.amadeus.com/v1/security/oauth2/token"

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

class FlightData:
    #This class is responsible for structuring the flight data.


    def __init__(self):
        self.stops = 0
        pass
    def findFlight(self, originCityCode, destinationcity, fromTime, toTime, num_adults, max_price, isDirect = True):
        flightSearch = FlightSearch()
        ACCESS_TOKEN = flightSearch.get_new_Token()


        headers = {
            'Authorization': f'Bearer {ACCESS_TOKEN}',
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }
        parameters = {
            "originLocationCode": DALLAS_IATA_CODE,
            "destinationLocationCode": destinationcity,
            "departureDate": "2025-05-21",
            "adults": num_adults,
            "maxPrice": max_price,
            # "nonStop" : False
        }
        try:
            connection = requests.get(url=FLIGHT_DESTINATION_URL, headers=headers, data=body, params=parameters)

            least_counter_ID = 0
            least_price = connection.json()["data"][0]["price"]["base"]
            


            try:
                counter = 0
                while True:
                    # print(f"Current Least Price: {least_price}")
                    # pprint(connection.json()['data'][counter]['price']['base'])
                    if float(least_price) > float(connection.json()['data'][counter]['price']['base']):
                        # print(f"Before: {least_price} and {connection.json()['data'][counter]['price']['base']} and {float(least_price) > float(connection.json()['data'][counter]['price']['base'])}")
                        least_price = connection.json()['data'][counter]['price']['base']
                        # print(f"After: {least_price}")
                        least_counter_ID = counter
                    counter +=1
            except:
                print(f"The least Expensive flight to {destinationcity} is Flight ID: {least_counter_ID}, and the Base price is {least_price}")
                return least_price


        except:
            print(f"There are no Flights to {destinationcity} under {max_price} for {num_adults} available on 05-29-2025")
