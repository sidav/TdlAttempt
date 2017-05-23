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


MAP_WIDTH = 80
MAP_HEIGHT = 25
TOTAL_AUTOMATA_PAIRS = 4

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

def doCAshit():
    maparr = [["#"] * (MAP_HEIGHT + 1) for _ in range(MAP_WIDTH + 1)]
    auts = []
    for i in range(1, TOTAL_AUTOMATA_PAIRS+1):
        x = i * MAP_WIDTH // (TOTAL_AUTOMATA_PAIRS + 1)
        y = i * MAP_HEIGHT // (TOTAL_AUTOMATA_PAIRS + 1)
        auts.append(Automata(x, y, maparr))
        auts.append(Automata(x, MAP_HEIGHT-y, maparr))
        #auts.append(Automata(MAP_WIDTH-x, y, maparr))
    for aut in auts:
        for _ in range(300):
            aut.step()
    print(len(auts))
    setForegroundColor(255, 255, 255)
    drawCharArray(maparr)
