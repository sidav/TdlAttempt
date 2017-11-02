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
_MAP_HEIGHT = 20

_MIN_ROOM_SIZE = 2
_MAX_ROOM_SIZE = 10

_FLOOR_CODE = ' '
_WALL_CODE = '#'
_DOOR_CODE = '+'


def placeRoom(self):
    pass


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
