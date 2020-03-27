class Room(object):

    def __init__(self):

        self.adjacent_rooms = {'north': None, 'south': None, 'east': None, 'west': None }


# -----Dungeon Area-----

class SouthCell(Room):

    def __init__(self):

        super(SouthCell, self).__init__()

        self.adjacent_rooms['north'] = 'dungeon'

    def enter(self):

        return "\nYou look around inside the dilapidated cell.  The bars are rusted and bent all out of shape, and the door is nonexistant.  Up above you can see the hole you fell down; it's so narrow and tall that you can't see the top.  Other than the remains of a wooden bench there isn't anything else in the cell."


class Dungeon(Room):

    def __init__(self):

        super(Dungeon, self).__init__()

        self.adjacent_rooms['south'] = 'south_cell'
        self.adjacent_rooms['north'] = 'north_cell'
        self.adjacent_rooms['east'] = 'east_cell'
        self.adjacent_rooms['west'] = 'crossroads'

    def enter(self):

        return "\nYou enter what appears to be the ruins of an ancient dungeon, with rubble everywhere.  There are only 3 cells accessible; anything else seems to have been cut off from a cave-in"


class NorthCell(Room):

    def __init__(self):

        super(NorthCell, self).__init__()

        self.adjacent_rooms['south'] = 'dungeon'

    def enter(self):

        return "\nThe door to the north cell opens without a problem.  You take two steps forward and the floor starts to give.  You quickly turn around to leave, but it's too late.  The floor below you collapses and you fall towards a pit of spikes, lava, sawblades, and sharks somehow.  Must be lava sharks.  You don't die to any of that, though, you hit a rock on your way down."


class EastCell(Room):

    def __init__(self):

        super(EastCell, self).__init__()

        self.adjacent_rooms['west'] = 'dungeon'

    def enter(self):

        return "\nYou enter the east cell.  There is a mysterious package hidden underneath the wooden bench."


# -----Cavern Area-----

class Crossroads(Room):

    def __init__(self):

        super(Crossroads, self).__init__()

        self.adjacent_rooms['east'] = 'dungeon'
        self.adjacent_rooms['west'] = 'bridge_east'
        self.adjacent_rooms['north'] = 'root_forest'

    def enter(self):

        return "\nYou enter a large open cavern with crumbling stone brick paths showing the way."


class BridgeEast(Room):

    def __init__(self):

        super(BridgeEast, self).__init__()

        self.adjacent_rooms['east'] = 'crossroads'
        self.adjacent_rooms['west'] = 'bridge_west'

    def enter(self):

        return "\nStanding before you is what seems to have once been a bridge, however all that remains is an impassable ravine stretching down into the abyss."


class BridgeWest(Room):

    def __init__(self):

        super(BridgeWest, self).__init__()

        self.adjacent_rooms['east'] = 'bridge_east'
        self.adjacent_rooms['north'] = 'cavern_entrance'

    def enter(self):

        return "\nYou are on the western side of the destroyed bridge."


class CavernEntrance(Room):

    def __init__(self):

        super(CavernEntrance, self).__init__()

        self.adjacent_rooms['south'] = 'bridge_west'
        self.adjacent_rooms['north'] = 'goal'

    def enter(self):

        return "The cave starts to get wider and the air a little nicer as you walk.  Up ahead, a few beams of light appear from the other end of the cavern.  But in order to get to the exit, you need to get past the dragon.  And the dragon looks hungry."


# -----Overgown Area-----

class RootForest(Room):

    def __init__(self):

        super(RootForest, self).__init__()

        self.adjacent_rooms['south'] = 'crossroads'
        self.adjacent_rooms['west'] = 'waterfall'

    def enter(self):

        return "\nYou enter a room filled with the roots from what must be a forest on the surface, so that it's hard to move around."


class Waterfall(Room):

    def __init__(self):

        super(Waterfall, self).__init__()

        self.adjacent_rooms['east'] = 'root_forest'

    def enter(self):

        return "\nYou hit a dead end in a pretty room with a waterfall pouring into a small pool of clear water.  You realize that you are quite thirsty."
