from flask_adventure_game import map

def test_map():

    room_layout = map.Map()

    assert room_layout.north_room.adjacent_rooms['south'] == 'middle_room'

    assert room_layout.middle_room.adjacent_rooms['north'] == 'north_room'
    assert room_layout.middle_room.adjacent_rooms['south'] == 'south_room'

    assert room_layout.south_room.adjacent_rooms['north'] == 'middle_room'
