from flask_adventure_game.lexicon import scan


def test_empty_command():

    command = scan('')
    assert command['type'] == 'error'
    assert command['detail'] == 'Enter a command'

def test_movement_commands():

    command = scan('Go north')
    assert command['type'] == 'movement'
    assert command['detail'] == 'north'

    command = scan('HEAD WEST')
    assert command['type'] == 'movement'
    assert command['detail'] == 'west'

    command = scan('slither south')
    assert command['type'] == 'error'
    assert command['detail'] == "I don't know what that means"

    command = scan('move')
    assert command['type'] == 'error'
    assert command['detail'] == 'Please give a cardinal direction'

def test_action_commands():

    command = scan('Throw the rock into the ravine')
    assert command['type'] == 'action'
    assert command['detail'] == 'throw'

    command = scan('OPeN SesAMe')
    assert command['type'] == 'action'
    assert command['detail'] == 'open'

    command = scan('Spontaneously Combust')
    assert command['type'] == 'error'
    assert command['detail'] == "I don't know what that means"
