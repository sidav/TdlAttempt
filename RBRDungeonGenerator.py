# Room-By-Room dungeon generator.
# Was already implemented in C# for my "StealthRoguelike" prototype.

#############################################################################
def _random(min, max): #IT'S JUST A WRAPPER. Min, max inclusive!            #
    return _rand(max-min+1)+min                                             #
                                                                            #
_LCG_X = None                                                               #
                                                                            #
def setRandomSeed(seed):                                                    # FOR TEH GREAT INDEPENDENCY!
    global _LCG_X                                                           #
    _LCG_X = seed                                                           #
                                                                            #
def _rand(mod):                                                             #
    global _LCG_X                                                           #
    if _LCG_X is None:                                                      #
        _LCG_X = 7355608                                                    #
    LCG_A = 14741                                                           #
    LCG_C = 757                                                             #
    LCG_M = 77777677777                                                     #
    _LCG_X = (LCG_A*_LCG_X + LCG_C) % LCG_M                                 #
    return _LCG_X%mod                                                       #
#############################################################################

_MAP_WIDTH = 80
_MAP_HEIGHT = 25

_MIN_ROOM_SIZE = 2
_MAX_ROOM_SIZE = 10

_FLOOR_CODE = ' '
_WALL_CODE = '#'
_DOOR_CODE = '+'


class _Coordinate:
    x = y = 0
    def __init__(self):
        self.x = _random(0, _MAP_WIDTH)
        self.y = _random(0, _MAP_HEIGHT)


def fillRoom(maparr, x, y, w, h, char): # fill rect for room
    for i in range (x, x+w):
        for j in range (y, y+h):
            maparr[i][j] = char


def findWallForDoor(maparr):
    for _ in range(1000):
        # first, take a look at a random cell
        x = _random(0, _MAP_WIDTH)
        y = _random(0, _MAP_HEIGHT)
        # check if it's a wall
        if maparr[x][y] != _WALL_CODE:
            continue
        # let's check if it is "thick" wall
        if () or ():



def placeInitialRoom(maparr):
    roomW = _random(_MIN_ROOM_SIZE, _MAX_ROOM_SIZE)
    roomH = _random(_MIN_ROOM_SIZE, _MAX_ROOM_SIZE)
    halfRoomW = int(roomW / 2)
    halfRoomH = int(roomH / 2)
    halfMapW = int(_MAP_WIDTH / 2)
    halfMapH = int(_MAP_HEIGHT / 2)
    for i in range (halfMapW - halfRoomW, halfMapW + halfRoomW):
        for j in range (halfMapH - halfRoomH, halfMapH + halfRoomH):
            maparr[i][j] = _FLOOR_CODE


def generateDungeon():
    # Fill the map with solid walls.
    maparr = [[_WALL_CODE] * (_MAP_HEIGHT + 1) for _ in range(_MAP_WIDTH + 1)]
    # Place the random room in center of the map.
    placeInitialRoom(maparr)
    return maparr


def getMap(): # FOR TESTING PURPOSES
    return generateDungeon()
