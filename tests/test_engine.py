import pytest


def test_interface(client, app):

    response = client.get('/')
    assert response.status_code == 200
    assert b'Dungeon Escape' in response.data
    assert b'Enter Command:' in response.data
    assert b'<button type="submit"' in response.data

    response = client.post('/', data={'command': 'move north'})
    assert b'You are in the northern room' in response.data
