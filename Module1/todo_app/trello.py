from dotenv import load_dotenv
import requests, os, json
from todo_app.data.trello_items import *

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
BOARD_LIST = os.getenv('BOARD_LIST')

print(f"output >> {API_KEY} - {API_TOKEN}")

board_id = '64ef5905b30edf49e85fa33f'

# Let's get board information
base_url = "https://api.trello.com/1/boards/"
url = f"{base_url}{board_id}/cards"

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
    print(f"Name: {item['name']} ID: {item['id']} ListID: {item['idList']}")

  
list_cards = []

for item in cards:
    temp_dict = {"name": item['name'], "ID": item['id'], "ListID": {item['idList']}}
    list_cards.append(temp_dict)

print(list_cards)

def move_card():
    pass

my_instance = MYTRELLO(API_KEY, API_TOKEN)

# my_instance.new_card("HARBS1", "My Card")

output = my_instance.get_cards()

for item in output:
    print(item)