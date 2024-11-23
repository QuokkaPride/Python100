import requests
from datetime import datetime


USERNAME = "slothbro"
TOKEN = "alsdfjlkasjdflkadsjflk"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Minutes Speaking Spanish",
    "unit": "Mins",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# posting a pixel
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}" 

today = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "1",
}

response = requests.post(post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# updating a pixel
update_pixel_endpoint = f"{post_pixel_endpoint}/{today}"

update_pixel_config = {
    "quantity": "100",
}

response = requests.put(update_pixel_endpoint, json=update_pixel_config, headers=headers)
print(response.text)
