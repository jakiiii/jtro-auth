import os
import json
import requests

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

headers = {
    "Content-Type": "application/json",
}

data = {
    "username": 'jaki@jqurity.com',
    "password": 'SADHIN101119',
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()  # ['token']
print(token)
