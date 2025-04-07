import string

import requests
import os



DALLAS_IATA_CODE = "DFW"

API_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_DESTINATION_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_HEADER = "https://test.api.amadeus.com/v1/security/oauth2/token"

os.environ["AMADEUS_API_KEY"] = "CzWCV9xbjmUIlME1qk13X9EN09paWLI2"
os.environ["AMADEUS_API_SECRET"] = "kAJmzcy2QbbJATCl"
API_KEY = os.environ["AMADEUS_API_KEY"]
API_SECRET = os.environ["AMADEUS_API_SECRET"]

class FlightSearch:
    def __init__(self):
        pass
    # connection = requests.post(url=API_URL,headers=headers,data=body)

    # print(connection.text)
    #     conc = connection.json()
    #     data = conc["data"][0]["price"]["total"]
    #     print(data)
    def findFlight(self, destinationcity, num_adults, max_price ):
        ACCESS_TOKEN = self.get_new_Token()

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
            "departureDate": "2025-05-22",
            "adults": num_adults,
            "maxPrice": max_price
        }
        try:
            connection = requests.get(url=FLIGHT_DESTINATION_URL, headers=headers, data=body, params=parameters)

            least_counter_ID = 0
            least_price = connection.json()["data"][0]["price"]["base"]

            counter = 0
            try:
                while True:
                    if least_price < connection.json()['data'][counter]['price']['base']:
                        least_price = connection.json()['data'][counter]['price']['base']
                        least_counter_ID = counter
                    # print(f"Flight ID: {counter}\nBase cost of flight from DFW to {destinationcity} is {connection.json()['data'][counter]['price']['base']}")
                    counter +=1
            except:
                print(f"No more flights {destinationcity}")
                print(f"The least Expensive flight to {destinationcity} is Flight ID: {least_counter_ID}, and the Base price is {least_price}\n")


        except:
            print(f"There are no Flights to {destinationcity} under {max_price} for {num_adults} available on 05-29-2025")

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
