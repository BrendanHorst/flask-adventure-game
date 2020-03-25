from flask_adventure_game.rooms import *

class Map(object):

    def __init__(self):

        self.north_room = NorthRoom()
        self.south_room = SouthRoom()

    def next_room(self, target):

        return getattr(self, target).enter()
