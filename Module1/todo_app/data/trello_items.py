import json
import requests
import os
from datetime import datetime


class MYTRELLO():
    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token
        self.boardID = os.getenv('BOARDID')
 
    def new_card(self, card_name, ListID, card_due, description=""):

        card_url = "https://api.trello.com/1/cards"

        headers = {
            "Accept": "application/json"
        }

        query = {
            "key": self.api_key,
            "token": self.api_token,
            "idList": ListID,
            "name": card_name,
            "due": card_due,
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
            print(item)
            print(f"Keys in item: {item.keys()}")
            print(f"{item['due']} and {type(item['due'])}")
            if item['due'] is not None:
                print(f"ok {item['due']}")
                if item['due']:
                    ## due_temp = datetime.fromisoformat(item['due'])
                    due_temp = item['due'][:-1]
                    print(f"DUE_TEMP = {due_temp}")
                    due_date = datetime.strptime(due_temp, "%Y-%m-%dT%H:%M:%S.%f")
                # due_date = due_temp.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    due_date = None
            else:
                due_date = None
            temp_dict = {
                "name": item['name'],
                "DESC": item['desc'],
                "ID": item['id'], 
                "due": due_date, 
                "ListID": item['idList']
            }
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
        url = f"{base_url}{card_id}"

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
    
    def delete_card(self, card_id):

        base_url = "https://api.trello.com/1/cards/"
        url = f"{base_url}{card_id}"

        headers = {
            "Accept": "application/json"
        }

        query = {
            "key": self.api_key,
            "token": self.api_token
        }

        response = requests.delete(
            url, 
            headers=headers, 
            params=query
            )

        card_delete = response.json()

        return card_delete