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

_MAX_PLACEMENT_TRIES = 1000

_MAX_CORRIDORS_COUNT = 150
_MAX_ROOMS_COUNT = 50

_MIN_ROOM_SIZE = 3
_MAX_ROOM_SIZE = 10
_MIN_CORRIDOR_LENGTH = 3
_MAX_CORRIDOR_LENGTH = 10

_FLOOR_CODE = ' '
_WALL_CODE = '#'
_DOOR_CODE = '\\'#'\''


class _Vector:
    x = y = 0

    def __init__(self, x = None, y = None):

        if x is None or y is None:
            self.x = _random(0, _MAP_WIDTH-1)
            self.y = _random(0, _MAP_HEIGHT-1)
        else:
            self.x = x
            self.y = y

####################################################


def dig(maparr, x, y, w, h, char=_FLOOR_CODE): # fill rect with char
    for i in range (x, x+w):
        for j in range (y, y+h):
            if (0 <= i < _MAP_WIDTH and 0 <= j < _MAP_HEIGHT):
                maparr[i][j] = char


def isWall(maparr, x, y, w=1, h=1):
    for i in range (x, x+w):
        for j in range(y, y+h):
            if (0 < i < _MAP_WIDTH-1 and 0 < j < _MAP_HEIGHT-1):
                if maparr[i][j] != _WALL_CODE:
                    return False
            else:
                return  False
    return True


def pickDirectionForDigging(maparr, x, y):
    direction = None
    if x >= _MAP_WIDTH or y >= _MAP_HEIGHT:
        print("!!!Oh noes! Coordinates cheburachnulis at ${0}, ${1}!!!".format(x, y))
        #return _Vector(0, 0)
    if maparr[x][y+1] == _FLOOR_CODE:
        direction = _Vector(0, -1)
    elif maparr[x-1][y] == _FLOOR_CODE:
        direction = _Vector(1, 0)
    elif maparr[x][y-1] == _FLOOR_CODE:
        direction = _Vector(0, 1)
    elif maparr[x+1][y] == _FLOOR_CODE:
        direction = _Vector(-1, 0)
    else:
        direction = _Vector(0, 0)
    return direction


def tryAddCorridor(maparr):
    for tries in range (_MAX_PLACEMENT_TRIES):
        currCell = _Vector()
        corrLength = _random(_MIN_CORRIDOR_LENGTH, _MAX_CORRIDOR_LENGTH)

        while not isWall(maparr, currCell.x, currCell.y):
            currCell = _Vector()

        digDirection = pickDirectionForDigging(maparr, currCell.x, currCell.y)
        dirx = digDirection.x
        diry = digDirection.y
        if dirx == diry == 0:
            continue

        if dirx == 1: # dig right
            if isWall(maparr, currCell.x+1, currCell.y-1, corrLength, 3):
                dig(maparr, currCell.x+1, currCell.y, corrLength, 1)
                maparr[currCell.x][currCell.y] = _DOOR_CODE
                return
        elif dirx == -1: # dig left
            if isWall(maparr, currCell.x-corrLength, currCell.y-1, corrLength, 3):
                dig(maparr, currCell.x-corrLength, currCell.y, corrLength, 1)
                maparr[currCell.x][currCell.y] = _DOOR_CODE
                return
        elif diry == 1: # dig down
            if isWall(maparr, currCell.x-1, currCell.y+1, 3, corrLength):
                dig(maparr, currCell.x, currCell.y+1, 1, corrLength)
                maparr[currCell.x][currCell.y] = _DOOR_CODE
                return
        elif diry == -1: # dig up
            if isWall(maparr, currCell.x-1, currCell.y-corrLength, 3, corrLength):
                dig(maparr, currCell.x, currCell.y-corrLength, 1, corrLength)
                maparr[currCell.x][currCell.y] = _DOOR_CODE
                return


def tryAddRoom(maparr):
    for tries in range (_MAX_PLACEMENT_TRIES):
        currCell = _Vector()
        roomW = _random(_MIN_ROOM_SIZE, _MAX_ROOM_SIZE)
        roomH = _random(_MIN_ROOM_SIZE, _MAX_ROOM_SIZE)
        horOffset = _random(0, roomW-1)
        vertOffset = _random(0, roomH-1)
        while not isWall(maparr, currCell.x, currCell.y):
            currCell = _Vector()

        digDirection = pickDirectionForDigging(maparr, currCell.x, currCell.y)
        dirx = digDirection.x
        diry = digDirection.y
        if dirx == diry == 0:
            continue
        #TODO: add dig up/down restrictions (i.e. there should be more "digged horizontally" rooms than "digged vertically" ones)
        if dirx == 1: # dig right
            if isWall(maparr, currCell.x, currCell.y-vertOffset-1, roomW+2, roomH+2):
                dig(maparr, currCell.x+1, currCell.y-vertOffset, roomW, roomH)
                maparr[currCell.x][currCell.y] = _DOOR_CODE
                return
        elif dirx == -1: # dig left
            if isWall(maparr, currCell.x-roomW-1, currCell.y-vertOffset-1, roomW+2, roomH+2):
                dig(maparr, currCell.x-roomW, currCell.y-vertOffset, roomW, roomH)
                maparr[currCell.x][currCell.y] = _DOOR_CODE
                return
        elif diry == 1: # dig down
            if isWall(maparr, currCell.x-horOffset-1, currCell.y, roomW+2, roomH+2):
                dig(maparr, currCell.x-horOffset, currCell.y+1, roomW, roomH)
                maparr[currCell.x][currCell.y] = _DOOR_CODE
                return
        elif diry == -1: # dig up
            if isWall(maparr, currCell.x-horOffset-1, currCell.y-roomH-1, roomW+2, roomH+2):
                dig(maparr, currCell.x-horOffset, currCell.y-roomH, roomW, roomH)
                maparr[currCell.x][currCell.y] = _DOOR_CODE
                return

# def findWallForDoor(maparr):
#     for _ in range(1000):
#         # first, take a look at a random cell
#         x = _random(0, _MAP_WIDTH)
#         y = _random(0, _MAP_HEIGHT)
#         # check if it's a wall
#         if maparr[x][y] != _WALL_CODE:
#             continue
#         # let's check if it is "thick" wall
#         if () or ():



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
    #TODO: all the other shit
    currentRoomsCount = 0
    currentCorrsCount = 0
    while currentRoomsCount < _MAX_ROOMS_COUNT or currentCorrsCount < _MAX_CORRIDORS_COUNT:
        if currentCorrsCount < _MAX_CORRIDORS_COUNT:
            tryAddCorridor(maparr)
            currentCorrsCount += 1
        if currentRoomsCount < _MAX_ROOMS_COUNT:
            tryAddRoom(maparr)
            currentRoomsCount += 1

    return maparr


def getMap(): # FOR TESTING PURPOSES
    return generateDungeon()
