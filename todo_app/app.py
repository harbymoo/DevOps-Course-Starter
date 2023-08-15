from flask import Flask, render_template, request

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            new_item = add_item(title)
        else:
            pass

    if request.method == 'POST':
        complete = request.form.get('complete')
        if complete:
            new_item = add_item(title)
        else:
            pass
    
    # return 'Hello World!'
    items = get_items()
    return render_template('index.html', items = items)

if __name__ == 'main':
    app.run(debug = True)