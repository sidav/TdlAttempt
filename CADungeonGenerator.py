from SidavRandom import * #Can be deleted if the following wrapper will be handled
from ConsoleWrapper import drawCharArray, setForegroundColor, putChar

### PATHFINDING SHIT FOR THE MAP VALIDATION
### All that pathfinding routines are so much simplified because their purpose is just to check if the path exists at all.
### i.e. that routines don't even need to find the shortest path, they should just check does there ANY path exist.
### The original ("full" with shortest path search) algorithm is in the SimplePathfiding.py in that repo.
class cell:
    def __init__(self, x, y, passabru, value):
        self.x = x
        self.y = y
        self.passable = passabru
        self.value = value

class cellStack:

    def __init__(self):
        self.stack = []

    def push(self, crap):
        self.stack.append(crap)

    def pop(self):
        if len(self.stack) == 0:
            #print("pop is fucked up.")
            return None
        ret = self.stack[len(self.stack)-1]
        self.stack.remove(ret)
        return ret

    def shift(self):
        if len(self.stack) == 0:
            #print("shift is fucked up.")
            return None
        ret = self.stack[0]
        self.stack.remove(ret)
        return ret

class CrapPathfinding:

    def abs(self, t):
        if t < 0:
            return -t
        return t

    def coordsValid(self, x, y):
        if 0 <= x < len(self.boolmap) and 0 <= y < len(self.boolmap[0]):
            return True
        return False

    def selectAdjacentZeroValueSquare(self):
        x = self.currentCell.x
        y = self.currentCell.y
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if self.coordsValid(x+i, y+j) and (i != 0 or j != 0) and (self.diagonalsAllowed or abs(i) + abs(j) != 2):
                    if self.cellmap[x+i][y+j].value == 0 and self.cellmap[x+i][y+j].passable and self.cellmap[x+i][y+j] != self.origin:
                        selectedSquare = self.cellmap[x+i][y+j] #yep, we have selected that one.
                        selectedSquare.value = self.currentCell.value + 1
                        return selectedSquare
        return None #There isn't any adjacent squares with zero value

    def CheckPath(self):
        #some pre-checks:
        if not self.target.passable:
            print("Target square is non-passable!")
            return False
        while True:
            #while True:
            selectedSquare = self.selectAdjacentZeroValueSquare()
            if selectedSquare is None:
                break
            if selectedSquare == self.target:
                return True
            self.unfinished.push(selectedSquare)
            #step 5
            self.currentCell = self.unfinished.shift()
            if self.currentCell == None:
                print("No way exists!")
                return False
        return True

    def PathExists(self, fromx, fromy, tox, toy, allowDiags):
        self.diagonalsAllowed = allowDiags
        self.target = self.cellmap[tox][toy]
        self.origin = self.cellmap[fromx][fromy]
        self.currentCell = self.origin
        return bool(self.CheckPath())

    def __init__(self, inpboolmap):
        x = len(inpboolmap)
        y = len(inpboolmap[0])
        self.boolmap = inpboolmap #if true, then the given cell is passabru!
        self.unfinished = cellStack()
        self.finalReversedPath = []
        self.cellmap = [[0] * y for _ in range(x)]
        for i in range(x):
            for j in range(y):
                self.cellmap[i][j] = cell(i, j, self.boolmap[i][j], 0)
###PATHFINDING SHIT ENDED


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


_MAP_WIDTH = 80
_MAP_HEIGHT = 25
_TOTAL_AUTOMATA_PAIRS = 8
_GENERATION_STEPS = 250

class Automata:
    def __init__(self, x, y, maparr):
        self.x = x
        self.y = y
        self.maparr = maparr

    def step(self):
        dx = randHorDir()
        dy = randVertDir()
        for _ in range(1000):
            while dx*dy != 0 or dx == dy:
                randomize()
                dx = randHorDir()
                dy = randVertDir()
            if (0 < self.x+dx < len(self.maparr)-2 and 0 < self.y+dy < len(self.maparr[0])-2):
                self.x += dx
                self.y += dy
                self.maparr[self.x][self.y] = " "
                break

def mapTooBoolArray(inputMap):
    boolMap = [[False] * (_MAP_HEIGHT + 1) for _ in range(_MAP_WIDTH+1)]
    for i in range(len(inputMap)):
        for j in range(len(inputMap[0])):
            if inputMap[i][j] == " ":
                boolMap[i][j] = True
    return boolMap

def makeWallOutline(arr): #just to be sure that the map won't be open to its borders.
    mapW = len(arr)
    mapH = len(arr[0])
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if 0 < i < mapW - 1 and 0 < j < mapH - 1:
                continue
            arr[i][j] = '#'# _WALL_CODE


def generateCave():
    class position:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    while True:
        maparr = [["#"] * (_MAP_HEIGHT + 1) for _ in range(_MAP_WIDTH + 1)]
        auts = []
        autsInitialPositions = []
        for i in range(1, _TOTAL_AUTOMATA_PAIRS + 1):
            x = i * _MAP_WIDTH // (_TOTAL_AUTOMATA_PAIRS + 1)
            y = i * _MAP_HEIGHT // (_TOTAL_AUTOMATA_PAIRS + 1)
            auts.append(Automata(x, y, maparr))
            auts.append(Automata(x, _MAP_HEIGHT - y, maparr))
            autsInitialPositions.append(position(x, y))
            autsInitialPositions.append(position(x, _MAP_HEIGHT - y))
            # auts.append(Automata(_MAP_WIDTH-x, y, maparr))
        for aut in auts:
            for _ in range(_GENERATION_STEPS):
                aut.step()
        #make wall outline:
        makeWallOutline(maparr)
        #validate cave:
        validator = CrapPathfinding(mapTooBoolArray(maparr))
        mapIsValid = True
        for i in range (1, len(auts)):
            mapIsValid *= validator.PathExists(autsInitialPositions[0].x, autsInitialPositions[0].y, autsInitialPositions[i].x, autsInitialPositions[i].y, False)
        if mapIsValid:
            break
    print(len(auts))
    return maparr


def doCAshit():
    maparr = generateCave()
    setForegroundColor(255, 255, 255)
    drawCharArray(maparr)
    return maparr
