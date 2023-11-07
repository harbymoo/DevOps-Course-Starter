from dotenv import load_dotenv, find_dotenv
import os
from flask.testing import FlaskClient
from todo_app import app
import pytest
import requests

@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch):
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    monkeypatch.setattr(requests, 'get', stub)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a tes
    # t_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def stub(url, params={}, headers=None):
    test_board_id = os.environ.get('BOARDID')
    print(test_board_id)
    fake_response_data = None

    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [
            { 'name': 'To Do', 'id': '654321' },
            { 'name': 'Doing', 'id': '765432' },
            { 'name': 'Done',  'id': '876543' }
        ]
        
        return StubResponse(fake_response_data)


    if url == f'https://api.trello.com/1/boards/{test_board_id}/cards':
        fake_response_data = [{
            'name': 'To Do',
            'desc': '',
            'id': '123abc',
            'due': '',
            'idList': '654321',     
            'cards': [{'name': 'card1', 'DESC': "", 'ID': '12345', 'due': '', 'ListID': '654321'}]
            },
        {
            'name': 'Doing',
            'desc': '',
            'id': '123edf',
            'due': '',
            'idList': '765432',     
            'cards': [{'name': 'card2', 'DESC': "", 'ID': '23456', 'due': '', 'ListID': '765432'}]
            },
        {
            'name': 'Done',
            'desc': '',
            'id': '123ghi',
            'due': '',
            'idList': '876543',     
            'cards': [{'name': 'card3', 'DESC': "", 'ID': '34567', 'due': '', 'ListID': '876543'}]
            }
        ]
        
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def test_flask_app_homepage(monkeypatch: pytest.MonkeyPatch, client: FlaskClient):
    
    # Arrange
    # Add test data

    # Act
    homepage_response = client.get('/')
    print(homepage_response)

    # Assert
    assert homepage_response.status_code == 200
    assert '<title>To-Do App</title>' in homepage_response.data.decode()
