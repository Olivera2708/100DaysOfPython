import requests
from datetime import datetime

from requests.api import head

USERNAME = ""
TOKIN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKIN,
    "username": USERNAME
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKIN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixeal_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "37"
}
requests.post(url=pixeal_creation_endpoint, json=pixel_data, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
new_pixel = {
    "quantity": "45"
}

response = requests.put(url=update_endpoint, json = new_pixel, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
