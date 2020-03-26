class Room(object):

    def __init__(self):

        self.adjacent_rooms = {'north': None, 'south': None, 'east': None, 'west': None }


class SouthRoom(Room):

    def __init__(self):

        super(SouthRoom, self).__init__()
        self.adjacent_rooms['north'] = 'middle_room'

    def enter(self):

        return 'You are in the southern room'

class MiddleRoom(Room):

    def __init__(self):

        super(MiddleRoom, self).__init__()
        self.adjacent_rooms['north'] = 'north_room'
        self.adjacent_rooms['south'] = 'south_room'

    def enter(self):

        return 'You are in the middle room'

class NorthRoom(Room):

    def __init__(self):

        super(NorthRoom, self).__init__()
        self.adjacent_rooms['south'] = 'middle_room'

    def enter(self):

        return 'You are in the northern room'
