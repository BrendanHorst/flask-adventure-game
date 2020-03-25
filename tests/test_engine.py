import pytest


def test_interface(client, app):

    response = client.get('/')
    assert response.status_code == 200
    assert b'Dungeon Escape' in response.data
    assert b'Enter Command:' in response.data
    assert b'<button type="submit"' in response.data

    response = client.post('/', data={'command': 'move north'})
    assert b'You are in the northern room' in response.data
    assert 'current_room=north_room' in response.headers['Set-Cookie']

    response = client.post('/', data={'command': ' '})
    assert b'Welcome to Dungeon Escape!' not in response.data
