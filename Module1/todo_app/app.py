from flask import Flask, render_template, request, redirect, make_response, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, save_item
from todo_app.data.trello_items import *

app = Flask(__name__)
app.config.from_object(Config())

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
BOARD_NAME = os.getenv('BOARD_NAME')

trello_instance = MYTRELLO(API_KEY, API_TOKEN)


@app.route('/',methods = ['POST', 'GET'])
def index():

    BOARD_LIST = trello_instance.lists_on_board()
    card_items = trello_instance.get_cards()
    return render_template('trello.html', card_items = card_items, BOARD_LIST = BOARD_LIST)  

@app.route('/trello_list', methods=['GET'])
def cards_list():
   
    BOARD_LIST = trello_instance.lists_on_board()
    card_items = trello_instance.get_cards()
    return render_template('trello.html', card_items = card_items, BOARD_LIST = BOARD_LIST)  

@app.route('/trello_list', methods=['POST', 'GET'])
def new_card_submit():
    if request.method == "POST": 
        card_name = request.form.get("card_title")
        card_desc = request.form.get("card_description")
    
    BOARD_LIST = trello_instance.lists_on_board()
    trello_instance.new_card(card_name, card_desc)
    card_items = trello_instance.get_cards()
    return render_template('trello.html', card_items = card_items, BOARD_LIST = BOARD_LIST)

@app.route('/move_the_card', methods=['POST', 'GET'])
def move_the_card():
    if request.method == "POST":
        card_id = request.form.get("card_id_value")
        list_id = request.form.get("list_id_value")
  
    BOARD_LIST = trello_instance.lists_on_board()
    trello_instance.move_cards(card_id, list_id)
    card_items = trello_instance.get_cards()
    return render_template('trello.html', card_items = card_items, BOARD_LIST = BOARD_LIST)

@app.route('/edit_the_card/<card_name>/<card_id>', methods=['POST', 'GET'])
def edit_the_card(card_id, card_name):

    # card = next((card for card in trello_instance.get_cards() if card['ID'] == card_id), None)
    # print(f"{card_id}")
    for card in trello_instance.get_cards():
        if card_id == card['ID']:
            print(card)
            f_card = card

    print(f"found - {f_card}")

    if request.method == 'POST':
        new_card_desc = request.form.get('card_edit_desc')
        trello_instance.modify_card(card_id, new_card_desc)

        return redirect(url_for('cards_list'))
        
    return render_template('edit.html', card = f_card, card_id = card_id, card_name = card_name)

@app.route('/delete_the_card/<card_id>', methods=['POST', 'GET', 'DELETE'])
def delete_the_card(card_id):
    
    for card in trello_instance.get_cards():
        if card_id == card['ID']:
            print(card)
            f_card = card

    if request.method == 'POST':
        card_to_be_deleted = request.form.get('delete_id_value')

        print(card_to_be_deleted)

    return render_template('delete_confirm.html', card = f_card, card_id = card_id)

@app.route('/confirm_delete/<delete_id_value>', methods=['POST', 'GET', 'DELETE'])
def confirm_delete(delete_id_value):

    for card in trello_instance.get_cards():
        if delete_id_value == card['ID']:
            print(card)
            f_card = card
       
    if request.method == 'POST':
        confirmation = request.form.get('confirmation')

        print(f"answer - {confirmation}")

        if confirmation == 'yes':
            trello_instance.delete_card(delete_id_value)
            return redirect(url_for('cards_list'))
        else:
            return redirect(url_for('cards_list'))
        
    return render_template('delete_confirm.html', card = f_card, confirmation = confirmation )

if __name__ == 'main':
    app.run(debug = True)

