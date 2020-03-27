from flask_adventure_game import rooms

class Map(object):

    def __init__(self):

        #Dungeon Area
        self.dungeon = rooms.Dungeon()
        self.north_cell = rooms.NorthCell()
        self.east_cell = rooms.EastCell()
        self.south_cell = rooms.SouthCell()

        #Cavern Area
        self.crossroads = rooms.Crossroads()
        self.bridge_east = rooms.BridgeEast()
        self.bridge_west = rooms.BridgeWest()
        self.cavern_entrance = rooms.CavernEntrance()

        #Overgrown Area
        self.root_forest = rooms.RootForest()
        self.waterfall = rooms.Waterfall()

    def next_room(self, target):

        return getattr(self, target).enter()
