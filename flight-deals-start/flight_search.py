import string

import requests
import os
from dotenv import find_dotenv, load_dotenv

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

DALLAS_IATA_CODE = "DFW"

API_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_DESTINATION_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_HEADER = "https://test.api.amadeus.com/v1/security/oauth2/token"


API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

class FlightSearch:
    def __init__(self):
        pass
    # connection = requests.post(url=API_URL,headers=headers,data=body)

    # print(connection.text)
    #     conc = connection.json()
    #     data = conc["data"][0]["price"]["total"]
    #     print(data)

    # print(connection.json())
    def findIataCode(self,city):
        IATA_CODE_DESTINATION_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        city_upper = city.upper()
        ACCESS_TOKEN = self.get_new_Token()
        parameters = {
            "keyword": city_upper
        }
        headers = {
            'Authorization': f'Bearer {ACCESS_TOKEN}',
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }
        IATA_CODE = requests.get(url=IATA_CODE_DESTINATION_URL,headers=headers,data = body, params= parameters);
        return IATA_CODE.json()['data'][0]["iataCode"]
    def get_new_Token(self):
        header = {
            'Content-Type':"application/x-www-form-urlencoded"
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret': API_SECRET
        }
        response = requests.post(url=TOKEN_HEADER, headers= header, data = body)
        return response.json()['access_token']
