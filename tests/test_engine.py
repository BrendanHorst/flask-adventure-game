import pytest


def test_interface(client, app):

    response = client.get('/')
    assert response.status_code == 200
    assert b'Dungeon Escape' in response.data
    assert b'Enter Command:' in response.data
    assert b'<button type="submit"' in response.data

    #Moving north from the start (middle) should return the north room
    response = client.post('/', data={'command': 'move north'})
    assert b'You are in the northern room' in response.data
    assert 'current_room=north_room' in response.headers['Set-Cookie']

    #Moving south from the start (middle) should return the south room
    response = client.post('/', data={'command': 'move south'})
    assert b'You are in the southern room' in response.data
    assert 'current_room=south_room' in response.headers['Set-Cookie']

    #Moving left or right should stay in the current room (middle)
    response = client.post('/', data={'command': 'move east'})
    assert b'You are in the middle room' in response.data
    assert 'current_room=middle_room' in response.headers['Set-Cookie']

    #Ensures that inputting a false command does not go back to the beginning
    response = client.post('/', data={'command': ' '})
    assert b'Welcome to Dungeon Escape!' not in response.data
