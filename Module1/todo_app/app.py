from flask import Flask, render_template, request, redirect, make_response, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, save_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/',methods = ['POST', 'GET'])
def index():
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
    # return redirect('/')

@app.route('/update_status', methods=['POST'])
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
    return render_template('index.html', items = items) 

if __name__ == 'main':
    app.run(debug = True)