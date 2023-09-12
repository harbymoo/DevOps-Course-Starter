import json
import requests
import os

BOARD_LIST = {
    'To_Do': '64ef5905b30edf49e85fa346', 
    'Doing': '64ef5905b30edf49e85fa347',
    'Done': '64ef5905b30edf49e85fa348'
}

class MYTRELLO():
    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token
        self.boardID = '64ef5905b30edf49e85fa33f'
    
    def new_card(self, card_name, description="", BoardID="64ef5905b30edf49e85fa33f", ListID="64ef5905b30edf49e85fa346"):

        card_url = "https://api.trello.com/1/cards"

        headers = {
            "Accept": "application/json"
        }

        query = {
            "key": self.api_key,
            "token": self.api_token,
            "idList": ListID,
            "name": card_name,
            "desc": description
        }

        response = requests.post(
            card_url,
            headers=headers,
            params=query
            )
        
        card_new = response.json()

        return card_new
    
    def get_cards(self):
        
        # Let's get board information
        base_url = "https://api.trello.com/1/boards/"
        url = f"{base_url}{self.boardID}/cards"

        print(url)

        headers = {
            "Accept": "application/json"
        }

        query = {
            "key": self.api_key,
            "token": self.api_token
        }

        response = requests.get(
            url, 
            headers=headers, 
            params=query
            )
        
        the_cards = response.json()

        list_cards = []

        for item in the_cards:
            temp_dict = {"name": item['name'], "DESC": item['desc'], "ID": item['id'], "ListID": item['idList']}
            list_cards.append(temp_dict)

        return list_cards
    
    def move_cards(self, card_id, ListID):
        
        # Let's get board information
        base_url = "https://api.trello.com/1/cards/"
        url = f"{base_url}{card_id}"

        headers = {
            "Accept": "application/json"
        }

        query = {
            "idList": ListID,
            "key": self.api_key,
            "token": self.api_token
        }

        print(requests.status_codes)

        response = requests.put(
            url, 
            headers=headers, 
            params=query
            )
        
        the_move = response.json()

        return the_move
    
    def modify_card(self, card_id, card_desc):

        base_url = "https://api.trello.com/1/cards/"
        url = url = f"{base_url}{card_id}"

        headers = {
            "Accept": "application/json"
        }

        query = {
            "desc": card_desc,
            "key": self.api_key,
            "token": self.api_token
        }

        response = requests.put(
            url,
            headers=headers,
            params=query
        )

        card_update = response.json()

        return card_update

    def lists_on_board(self):
        
        base_url = "https://api.trello.com/1/boards/"
        url = f"{base_url}{self.boardID}/lists"

        headers = {
            "Accept": "application/json"
        }

        query = {
            "key": self.api_key,
            "token": self.api_token
        }

        response = requests.get(
            url, 
            headers=headers, 
            params=query
            )
        
        board_lists_output = response.json()
        
        BOARD_LIST = {}
        
        for item in board_lists_output:
            BOARD_LIST[item['name']] = item['id']
            
        return BOARD_LIST  
      
if __name__ == '__main__':

    API_KEY = os.getenv('API_KEY')
    API_TOKEN = os.getenv('API_TOKEN')

    my_trello_instance = MYTRELLO(API_KEY,API_TOKEN)

    my_trello_instance.get_cards()