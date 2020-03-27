from flask_adventure_game import map

def test_map():

    room_layout = map.Map()

    #Dungeon Area
    assert room_layout.south_cell.adjacent_rooms['north'] == 'dungeon'

    assert room_layout.dungeon.adjacent_rooms['north'] == 'north_cell'
    assert room_layout.dungeon.adjacent_rooms['east'] == 'east_cell'
    assert room_layout.dungeon.adjacent_rooms['south'] == 'south_cell'
    assert room_layout.dungeon.adjacent_rooms['west'] == 'crossroads'

    assert room_layout.north_cell.adjacent_rooms['south'] == 'dungeon'

    assert room_layout.east_cell.adjacent_rooms['west'] == 'dungeon'

    #Cavern Area
    assert room_layout.crossroads.adjacent_rooms['north'] == 'root_forest'
    assert room_layout.crossroads.adjacent_rooms['east'] == 'dungeon'
    assert room_layout.crossroads.adjacent_rooms['west'] == 'bridge_east'

    assert room_layout.bridge_east.adjacent_rooms['east'] == 'crossroads'
    assert room_layout.bridge_east.adjacent_rooms['west'] == 'bridge_west'

    assert room_layout.bridge_west.adjacent_rooms['north'] == 'cavern_entrance'
    assert room_layout.bridge_west.adjacent_rooms['east'] == 'bridge_east'

    assert room_layout.cavern_entrance.adjacent_rooms['south'] == 'bridge_west'

    #Overgrown Area
    assert room_layout.root_forest.adjacent_rooms['south'] == 'crossroads'
    assert room_layout.root_forest.adjacent_rooms['west'] == 'waterfall'

    assert room_layout.waterfall.adjacent_rooms['east'] == 'root_forest'
