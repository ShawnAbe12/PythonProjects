import requests
import datetime as dt
USERNAME = "acrimony"
TOKEN = "qwepjqspidawqpn"
GRAPH_ID = "graph1"
today = dt.datetime.today().date()
today = today.strftime("%Y%m%d")
# today = txt.replace("-","")
# print(today)
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Habits Graph",
    "unit":"Minutes",
    "type":"int",
    "color":"shibafu"
}

headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_post_config ={
    "date":today,
    "quantity":"50"
}

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
pixel_put_config ={
    "quantity":"90"
}

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# print(pixel_endpoint)


# response = requests.post(url=pixel_post_endpoint,json=pixel_post_config,headers=headers)
# print(response.text)


#
# response = requests.put(url=pixel_put_endpoint,json=pixel_put_config,headers=headers)
# print(response.text)


response = requests.delete(url=pixel_delete_endpoint,headers=headers)
print(response.text)