class Room(object):

    def __init__(self):

        self.adjacent_rooms = {'north': None, 'south': None, 'east': None, 'west': None }


class South_Room(Room):

    def __init__(self):

        super(South_Room, self).__init__()
        self.adjacent_rooms['north'] = 'north_room'

    def enter(self):

        return 'You are in the southern room'

class North_Room(Room):

    def __init__(self):

        super(South_Room, self).__init__()
        self.adjacent_rooms['south'] = 'south_room'

    def enter(self):

        return 'You are in the northern room'
