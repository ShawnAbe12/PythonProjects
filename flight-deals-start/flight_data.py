import requests
import os
from dotenv import find_dotenv, load_dotenv
from pprint import pprint

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

DALLAS_IATA_CODE = "DFW"

API_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_DESTINATION_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_HEADER = "https://test.api.amadeus.com/v1/security/oauth2/token"

API_KEY = os.getenv("Amadeus_API_KEY")
API_SECRET = os.getenv("AmadeusAPI_SECRET")


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.stops = 0

    def least(self, connection):
        try:
            least_counter_ID = 0
            least_price = connection.json()["data"][0]["price"]["base"]
            print(f"{least_price}")

            try:
                counter = 0
                while True:
                    # print(f"{least_price}")
                    # print(f"Current Least Price: {least_price}")
                    # pprint(connection.json()['data'][counter]['price']['base'])
                    if float(least_price) > float(connection.json()['data'][counter]['price']['base']):
                        # print(f"Before: {least_price} and {connection.json()['data'][counter]['price']['base']} and {float(least_price) > float(connection.json()['data'][counter]['price']['base'])}")
                        least_price = connection.json()['data'][counter]['price']['base']
                        # print(f"After: {least_price}")
                        least_counter_ID = counter
                    counter += 1
            except:
                # print(f"The least Expensive flight to {destinationcity} is Flight ID: {least_counter_ID}, and the Base price is {least_price}")
                return least_price


        except:
            pass
