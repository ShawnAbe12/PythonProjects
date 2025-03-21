import requests
import datetime
import math
import smtplib
import time

#
#
#
# response = requests.get(url=iss)
#
# response.raise_for_status()
#
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
# print(longitude,latitude)

sun_api = "https://api.sunrise-sunset.org/json"
iss_api = "http://api.open-notify.org/iss-now.json"

LAT = 33.034061
LNG = -97.079643


def is_iss_overhead():
    iss_response = requests.get(url=iss_api)
    iss_response.raise_for_status()
    iss_data = iss_response.json()["iss_position"]

    iss_long = float(iss_data["longitude"])
    iss_lat = float(iss_data["latitude"])

    abs_lat = math.floor(abs(LAT - iss_lat))
    abs_long = math.floor(abs(LNG - iss_long))

    print(abs_lat, abs_long)
    if abs_lat <= 5 and abs_long <= 5:
        return True

def is_night():

    parameters = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0
    }
    sun_response = requests.get(url=sun_api, params=parameters)
    sun_response.raise_for_status()

    sun_data = sun_response.json()["results"]
    sunrise_data = int(sun_data["sunrise"].split("T")[1].split(":")[0])
    sunset_data = int(sun_data["sunset"].split("T")[1].split(":")[0])

    # print(sunrise_data, sunset_data)

    time_now = datetime.datetime.now()
    # print(time_now.hour)
    if sunset_data <= time_now.hour or time_now.hour <= sunrise_data:
        return True

gmail = "testingxzcv@gmail.com"
gmail_app_pass = "qrza kavj ialg spku"
yahoo = "testing62@myyahoo.com"
while True:
    with smtplib.SMTP("smtp.gmail.com.", port=587) as connection:
        connection.starttls()
        if is_iss_overhead():
            connection.login(user=gmail, password=gmail_app_pass)
            connection.sendmail(from_addr=gmail,to_addrs="johnabe5605@gmail.com",msg="Subject: THE ISS IS OVERHEAD"
                                                                                     "\n\nLOOK UP RIGHT NOW")
            print("Sent")
    time.sleep(60)

