import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')

print(f"output >> {API_KEY} - {API_TOKEN}")

board_id = '64ef5905b30edf49e85fa33f'

# Let's get board information
base_url = "https://api.trello.com/1/boards/"
url = f"{base_url}{board_id}/lists"

headers = {
    "Accept": "application/json"
}

query = {
    'key': API_KEY,
    'token': API_TOKEN
}

response = requests.get(
    url, 
    headers=headers, 
    params=query
    )

print(f'Response code - {response.status_code} {url}{query}')
print(json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": ")))

cards = response.json()

for item in cards:
    print(f"Name: {item['name']} ID: {item['id']}")
