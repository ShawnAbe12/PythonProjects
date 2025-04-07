import requests
from pprint import pprint
import os
from dotenv import find_dotenv, load_dotenv



class DataManager:

    def __init__(self):
        dotenv_file = find_dotenv()
        load_dotenv(dotenv_file)
        self.SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
        # self.sheet_headers = os.getenv("sheet_headers")
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
        #, headers=self.sheet_headers
        sheety = requests.post(url=self.SHEETY_ENDPOINT, json=self.post_parameters)
        print(sheety.text)
    def get(self):
        sheety = requests.get(url=self.SHEETY_ENDPOINT)
        data = sheety.json()["prices"]
        pprint(data)
        return data
    def put(self,data,objectID):
        endpoint = self.SHEETY_ENDPOINT + "/" + str(objectID)
        response = requests.put(url=endpoint, json=data)
        print(response.status_code)
        print(response.text)
    #This class is responsible for talking to the Google Sheet.
    pass
