#TODO: get rid of dependencies
#import Routines.TdlConsoleWrapper as CW
#TODO: Optimisation for faster work.

_lastFromX = _lastFromY = -1
_lastVisibilityTable = [[]]



class xy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_line(fromx, fromy, tox, toy):
    line = []
    deltax = abs(tox - fromx)
    deltay = abs(toy - fromy)
    xmod = 1
    ymod = 1
    if tox < fromx:
        xmod = -1
    if toy < fromy:
        ymod = -1
    error = 0
    if deltax >= deltay:
        y = fromy
        deltaerr = deltay
        for x in range(fromx, tox+xmod, xmod):
            line.append(xy(x, y))
            error = error + deltaerr
            if 2 * error >= deltax:
                y = y + ymod
                error -= deltax
    elif deltay > deltax:
        x = fromx
        deltaerr = deltax
        for y in range(fromy, toy+ymod, ymod):
            line.append(xy(x, y))
            error = error + deltaerr
            if 2 * error >= deltay:
                x = x + xmod
                error -= deltay
    return line

#two-stage LOS check
#returns the visibility map from the view from fromx, fromy coords. True means that the cell is visible, False - not visible.

_visionObstructingMap = [[]] #True if the cell blocks line of sight, False otherwise.

def setvisionObstructingMap(visionObstructingMap):
    global _visionObstructingMap
    _visionObstructingMap = visionObstructingMap

def _straightLOSCheck(fromx, fromy, tox, toy):
    #Checks visible Line of Sight between two tiles
    #Uses straight Brasanham's Line
    #Kinda "first stage check", CAN NOT provide any final result
    mapW = len(_visionObstructingMap)
    mapH = len(_visionObstructingMap[0])
    line = get_line(fromx, fromy, tox, toy)
    for i, currCell in enumerate(line):
        x = currCell.x
        y = currCell.y
        if (x < 0 or y < 0 or x > mapW-1 or y > mapH-1):
            return False
        if _visionObstructingMap[x][y] == True and i < len(line)-1:
            return False
    return True

def _checkNeighbouringTiles(x, y, firstStageTable): #checks if the tile has some first-stage-visible neighbours
    mapW = len(firstStageTable)
    mapH = len(firstStageTable[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x+i < 0 or x+i >= mapW or y+j < 0 or y+j >= mapH:
                continue
            if abs(i*j) == 1:
                continue
            if not _visionObstructingMap[x+i][y+j] and firstStageTable[x+i][y+j]:
                return True
    return False



def getVisibilityTable(fromx, fromy):
    mapW = len(_visionObstructingMap)
    mapH = len(_visionObstructingMap[0])
    resultingMap = [[False] * (mapH) for _ in range(mapW)]
    #first stage
    firstStage = [[False] * (mapH) for _ in range(mapW)]
    for i in range(len(firstStage)):
        for j in range(len(firstStage[0])):
            firstStage[i][j] = _straightLOSCheck(fromx, fromy, i, j)
    #second stage
    secondStage = [[False] * (mapH) for _ in range(mapW)]
    for i in range(len(secondStage)):
        for j in range(len(secondStage[0])):
            if _visionObstructingMap[i][j]:
                secondStage[i][j] = _checkNeighbouringTiles(i, j, firstStage)
    #merging stages
    for i in range(len(firstStage)):
        for j in range(len(firstStage[0])):
            resultingMap[i][j] = bool(firstStage[i][j] or secondStage[i][j])
    return resultingMap

def visibleLineExists(fromx, fromy, tox, toy):
    global _lastFromX, _lastFromY, _lastVisibilityTable
    mapW = len(_visionObstructingMap)
    mapH = len(_visionObstructingMap[0])
    if fromx < 0 or fromx >= mapW or fromy < 0 or fromy >= mapH:
        return False
    if fromx == _lastFromX and fromy == _lastFromY and _lastVisibilityTable != [[]]:
        return bool(_lastVisibilityTable[tox][toy])
    else:
        _lastFromX = fromx
        _lastFromY = fromy
        _lastVisibilityTable = getVisibilityTable(fromx, fromy)
        return bool(_lastVisibilityTable[tox][toy])