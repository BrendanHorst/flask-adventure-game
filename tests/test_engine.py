import pytest


def test_interface(client, app):

    response = client.get('/')
    assert response.status_code == 200
    assert b'Dungeon Escape' in response.data
    assert b'Enter Command:' in response.data
    assert b'<button type="submit">Submit</button>' in response.data
    assert b'<button type="submit">Reset</button>' in response.data


def test_movement(client, app):

    #Moving north from the start (south cell) should return the dungeon
    response = client.post('/', data={'command': 'move north'})
    assert 'current_room=dungeon' in response.headers['Set-Cookie']

    #Moving west from the dungeon should return the crossroads
    response = client.post('/', data={'command': 'move west'})
    assert 'current_room=crossroads' in response.headers['Set-Cookie']

    #Moving south from the crossroads should stay in the same room
    response = client.post('/', data={'command': 'move south'})
    assert 'current_room=crossroads' in response.headers['Set-Cookie']

    #Ensures that inputting a false command does not go back to the beginning
    response = client.post('/', data={'command': ' '})
    assert b'Welcome to Dungeon Escape!' not in response.data


def test_reset(client, app):

    response = client.get('/reset')
    assert b'Welcome to Dungeon Escape!' in response.data
    assert 'current_room=south_cell' in response.headers['Set-Cookie']


def test_errors(client, app):

    response = client.post('/', data={'command': 'make waffles' })
    assert b"I don't know what that means" in repsonse.data

    response = client.post('/', data={'command': 'go there'})
    assert b"Please give a cardinal direction" in response.data
