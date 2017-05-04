#import tdl
from ConsoleWrapper import *
from SidavRandom import *
#DELETE FOLLOWING AFTER DEBUG:
from SimplePathfinding import *
from AStarPathfinding import *

playerx = SCREEN_WIDTH // 2
playery = SCREEN_HEIGHT // 2
exit_game = False
crapx = []
crapy = []

def keys():
    global playerx, playery, crapx, crapy, exit_game
    keypressed = readKey()
    if (keypressed.key == 'ESCAPE') or (keypressed.key == 'ESCAPE'): exit_game = True
    if (keypressed.key == 'UP') or (keypressed.key == 'KP8'): playery -= 1
    if (keypressed.key == 'DOWN'): playery += 1
    if (keypressed.key == 'LEFT'): playerx -= 1
    if (keypressed.key == 'SPACE'):
        crapx.append(playerx)
        crapy.append(playery)
    if (keypressed.key == 'RIGHT'): playerx += 1

def mainLoop():
    x = 9
    y = 9
    fx = 2
    fy = 2
    tx = 3
    ty = 5
    #boolmap = [[1] * y for _ in range(x)]
    boolmap = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    shit = AStarPathfinding(boolmap, fx, fy, tx, ty, allowDiags=True)
    crapPath = shit.findPath()
    while not tdl.event.is_window_closed(): # <--- not shit
        setForegroundColor(128, 128, 128)
        for i in range(len(boolmap)+2):
            for j in range(len(boolmap[0])+2):
                putChar("#", i, 0)
                putChar("#", i, len(boolmap[0])+1)
                putChar("#", 0, j)
                putChar("#", len(boolmap)+1, j)
        setForegroundColor(255, 255, 255)
        for i in range(len(boolmap)):
            for j in range(len(boolmap[0])):
                if not boolmap[i][j]:
                    putChar("#", i+1, j+1)
        setForegroundColor(255,0,0)
        for i in crapPath:
            putChar("*", i.x+1, i.y+1)
        setForegroundColor(0, 0, 255)
        putChar("@", fx+1, fy+1)
        setForegroundColor(0, 255, 255)
        putChar("T", tx+1, ty+1)
        putString("Path cost = " + str(shit.getPathCost()), 20, 0)
        #####################################
        clearConsole()
        for i in range(len(crapx)):
            drawLine(playerx, playery, crapx[i], crapy[i])
        drawCircle(playerx, playery, 7)
        setForegroundColor(255, 64, 64)
        putChar("@", playerx, playery)
        #SHIT ENDS HERE.
        tdl.flush()
        # putChar(" ", playerx, playery)
        # handle keys and exit game if needed
        keys()
        if exit_game:
            break


i = 127
mainLoop()