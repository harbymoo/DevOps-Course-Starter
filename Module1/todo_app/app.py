from flask import Flask, render_template, request, redirect, make_response, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, save_item
from todo_app.data.trello_items import *

app = Flask(__name__)
app.config.from_object(Config())

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
BOARD_NAME = os.getenv('BOARD_NAME')

""" BOARD_LIST = {
    'To_Do': '64ef5905b30edf49e85fa346', 
    'Doing': '64ef5905b30edf49e85fa347',
    'Done': '64ef5905b30edf49e85fa348'
}   """

trello_instance = MYTRELLO(API_KEY, API_TOKEN)


""" @app.route('/',methods = ['POST', 'GET'])
def old_index():
    #items = get_items()
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            new_item = add_item(title)
        else:
            pass
    
    #items_get = get_items()
    items = sorted(get_items(), key=lambda x: x['status'])
    return render_template('index.html', items = items)  
    # return redirect('/') """

@app.route('/',methods = ['POST', 'GET'])
def index():

    BOARD_LIST = trello_instance.lists_on_board()
    card_items = trello_instance.get_cards()
    return render_template('trello.html', card_items = card_items, BOARD_LIST = BOARD_LIST)  

""" @app.route('/update_status', methods=['POST'])
def update_status():
    items = get_items()
    item_id = int(request.form.get('item_id'))
    new_status = request.form.get('status')
    for item in items:
        if item['id'] == item_id:
            item['status'] = new_status
            response = make_response(redirect(url_for('index')))
            response.set_cookie(str(item_id), new_status)
            return response

    items = sorted(get_items(), key=lambda x: x['status'])
    return render_template('index.html', items = items)  """

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

@app.route('/edit_the_card/<card_id>', methods=['POST', 'GET'])
def edit_the_card(card_id):

    card = next((card for card in trello_instance.get_cards() if card['ID'] == card_id), None)

    if request.method == 'POST':
        new_card_desc = request.form.get('card_edit_desc')
        trello_instance.modify_card(card_id, new_card_desc)

        return redirect(url_for('cards_list'))

        
    return render_template('edit.html', card = card)

if __name__ == 'main':
    app.run(debug = True)

