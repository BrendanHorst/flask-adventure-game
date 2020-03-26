from flask_adventure_game import rooms

class Map(object):

    def __init__(self):

        self.north_room = rooms.NorthRoom()
        self.middle_room = rooms.MiddleRoom()
        self.south_room = rooms.SouthRoom()

    def next_room(self, target):

        return getattr(self, target).enter()
