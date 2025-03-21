import requests
import json
import datetime
APP_ID = "91d4641b"
API_KEY = "315a0b7ad602ccca9227352a16b3d2fd"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/7db547e6e47cf4eb2c77f55e67b89a9d/myWorkouts/workouts"

query = input("What exercise did you do?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters ={
    "query":query,
    "weight_kg":55,
    "height_cm":200,
    "age":18
}

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")


nutritionix = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=parameters)
results = nutritionix.json()
# data = nutritionix.json()["exercises"]
sheet_headers = {"Authorization":"Bearer dsaokjeqwpnkczlj"}
for exercises in results["exercises"]:
    post_parameters = {
        "workout": {
            "date":today_date,
            "time":now_time,
            "exercise":exercises["name"].title(),
            "duration":exercises["duration_min"],
            "calories":exercises["nf_calories"],

        }
    }
    sheety = requests.post(url=SHEETY_ENDPOINT,json=post_parameters,headers=sheet_headers)
    print(sheety.text)

# print(nutritionix.json())