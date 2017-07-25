from SidavRandom import * #Can be deleted if the following wrapper will be handled
from ConsoleWrapper import drawCharArray, setForegroundColor, putChar


def random(min, max): #IT'S JUST A WRAPPER. Min, max inclusive!
    return rand(max-min+1)+min

def randHorDir(): #What a shame.
    return random(-1, 1)

def randVertDir(): #What a shame.
    val = random(0, 100)
    if val < 30:
        return -1
    elif val > 70:
        return 1
    else:
        return 0


TOTAL_LAND_AUTOMS = 8#8
TOTAL_MNT_AUTOMS = 5#5
TOTAL_FOREST_AUTOMS = 8#12
LAND_CYCLES = 650
MNT_CYCLES = 175
FOREST_CYCLES = 150
_TOWN_PLACEMENT_TRIES = 3000
_WATER_CODE = '~'
_GROUND_CODE = '.'
_MOUNTAIN_CODE = '^'
_FOREST_CODE = 'f'
_TOWN_CODE = 'O'


class Automata:
    def __init__(self, x, y, maparr, brush, allowed = []):
        self.x = x
        self.y = y
        self.maparr = maparr
        self.brush = brush
        self.allowed = allowed
        self.allowed.append(self.brush)

    def step(self):
        MAX_DIRECTION_TRIES = 1000
        dx = randHorDir()
        dy = randVertDir()
        for _ in range(MAX_DIRECTION_TRIES):
            while dx*dy != 0 or dx == dy:
                randomize()
                dx = randHorDir()
                dy = randVertDir()
            if (0 < self.x+dx < len(self.maparr)-2 and 0 < self.y+dy < len(self.maparr[0])-2) and self.maparr[self.x+dx][self.y+dy] in self.allowed:
                self.x += dx
                self.y += dy
                self.maparr[self.x][self.y] = self.brush
                break

def addLandscapeElements(maparr, automs, brush, allowed:list, cycles, randomPlacement = True, minDistanceToMapBorder = 15):
    mapW = len(maparr)
    mapH = len(maparr[0])
    auts = []
    if randomPlacement:
        for i in range(1, automs + 1):
            selx = random(0+minDistanceToMapBorder, mapW-minDistanceToMapBorder)
            sely = random(0+minDistanceToMapBorder, mapH-minDistanceToMapBorder)
            while maparr[selx][sely] not in allowed:
                selx = random(0 + minDistanceToMapBorder, mapW - minDistanceToMapBorder)
                sely = random(0 + minDistanceToMapBorder, mapH - minDistanceToMapBorder)
            auts.append(Automata(selx, sely, maparr, brush, allowed))
    else:
        for i in range(1, automs+1):
            x = i * mapW // (TOTAL_LAND_AUTOMS + 1)
            y = i * mapH // (TOTAL_LAND_AUTOMS + 1)
            auts.append(Automata(x, y, maparr, _GROUND_CODE, [_WATER_CODE]))
    for aut in auts:
        for _ in range(cycles):
            aut.step()


def countSurroundings(maparr, x, y, code): #returns the number of surroundings for the tile
    mapW = len(maparr)
    mapH = len(maparr[0])
    result = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (0 < x+i < mapW and 0 < y+j < mapH):
                continue
            if (i !=0 or j != 0) and maparr[x+i][y+j] == code:
                result += 1
    return result

#TODO: replace the following with the universal solution.
def addSingleElement(maparr, elemCode, neighbours:list, neighborNumber:list, elemCount:int): #adds some shit (i.e. town, military base...) on the random map
    mapW = len(maparr)
    mapH = len(maparr[0])
    x = 0
    y = 0
    #to place a town we need the forest AND (water OR mountain) nearby.
    for _ in range(elemCount):
        for _ in range(_TOWN_PLACEMENT_TRIES):
            x = random(1, mapW-1)
            y = random(1, mapH-1)
            if maparr[x][y] != _GROUND_CODE and maparr[x][y] != _FOREST_CODE:
                continue
            forests = countSurroundings(maparr, x, y, _FOREST_CODE)
            mnts = countSurroundings(maparr, x, y, _MOUNTAIN_CODE)
            wtr = countSurroundings(maparr, x, y, _WATER_CODE)
            if forests >= MIN_FORESTS_NEARBY and (mnts >= MIN_MOUNTAINS_NEARBY or wtr >= MIN_WATER_NEARBY):
                maparr[x][y] = _TOWN_CODE
                break


def drawMap(maparr):
    for i in range(len(maparr)):
        for j in range(len(maparr[i])):
            if maparr[i][j] == _WATER_CODE:
                setForegroundColor(0, 64, 255)
            elif maparr[i][j] == _GROUND_CODE:
                setForegroundColor(200, 64, 64)
            elif maparr[i][j] == _MOUNTAIN_CODE:
                setForegroundColor(200, 200, 200)
            elif maparr[i][j] == _FOREST_CODE:
                setForegroundColor(0, 255, 64)
            elif maparr[i][j] == _TOWN_CODE:
                setForegroundColor(255, 128, 255)
            putChar(maparr[i][j], i, j)

def doCALandshit(mapW, mapH):
    maparr = [[_WATER_CODE] * (mapH) for _ in range(mapW)]
    #land
    addLandscapeElements(maparr, TOTAL_LAND_AUTOMS, _GROUND_CODE, [_WATER_CODE], LAND_CYCLES, True)
    #mountains
    addLandscapeElements(maparr, TOTAL_MNT_AUTOMS, _MOUNTAIN_CODE, [_GROUND_CODE], MNT_CYCLES)
    # forest
    addLandscapeElements(maparr, TOTAL_FOREST_AUTOMS, _FOREST_CODE, [_GROUND_CODE, _MOUNTAIN_CODE], FOREST_CYCLES)
    # towns
    addTowns(maparr, 3)
    setForegroundColor(255, 255, 255)
    drawMap(maparr)

    #drawCharArray(maparr)
