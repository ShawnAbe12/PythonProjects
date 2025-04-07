# with open("weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     day = []
#     temp = []
#     cond = []
#     for row in data:
#         day.append(row[0])
#         if row[1] != "temp":
#             2temp.append(int(row[1]))
#         cond.append(row[2])
#     print(day)
#     print(temp)
#     print(cond)

import pandas as pd

# data = pandas.read_csv("weather_data.csv")
# print(data['day'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
#
# # avg = round(sum(temp_list) / len(temp_list),1)
# avg = data["temp"].mean()
# print(avg)
#
# max = data["temp"].max()
# print(max)
#
# print(data["condition"])
# print(data.condition)
#
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()].temp)
#
# monday = data[data.day == "Tuesday"]
# print(monday.condition)
#
# monday_temp = (monday.temp *(9/5)) + 32
# print(monday_temp)

# list = [1,2,3,4,5,[1,2,3]]
# data = pandas.DataFrame(list)
# print(data)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240607.csv")

gray = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"]
black = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"]
#
fur_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray), len(cinnamon), len(black)]
    }
print(fur_dict)

data = pd.DataFrame.from_dict(fur_dict)

data.to_csv("squirrel_count.csv")