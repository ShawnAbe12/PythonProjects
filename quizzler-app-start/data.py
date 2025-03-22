import requests
url = "https://opentdb.com/api.php?amount=10&category=15&type=boolean"
connection = requests.get(url=url)
question_data = connection.json()["results"]
# print(question_data)