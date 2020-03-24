from flask_adventure_game import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/')
    assert response.data == b'Dungeon Escape'
    assert response.data == b'Enter Command:'
