import requests
from pprint import pprint



class DataManager:

    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/7db547e6e47cf4eb2c77f55e67b89a9d/flightDeals/prices"
        self.sheet_headers = {"Authorization": "Bearer aSODjpadajlkxzcm"}
        self.city = ""
        self.iata_Code = ""
        self.lowest_price = ""
    def post(self,city,iata_code,lowest_price):
        self.city = city
        self.iata_Code = iata_code
        self.lowest_price = lowest_price
        self.post_parameters = {
            "price": {
                "city": self.city,
                "iataCode": self.iata_Code,
                "lowestPrice": self.lowest_price
            }
        }
        sheety = requests.post(url=self.SHEETY_ENDPOINT, json=self.post_parameters, headers=self.sheet_headers)
        print(sheety.text)
    def get(self):
        sheety = requests.get(url=self.SHEETY_ENDPOINT)
        data = sheety.json()["prices"]
        return data
    def put(self,data,objectID):
        endpoint = self.SHEETY_ENDPOINT + "/" + str(objectID)
        response = requests.put(url=endpoint, json=data)
        print(response.status_code)
        print(response.text)
    #This class is responsible for talking to the Google Sheet.
    pass
