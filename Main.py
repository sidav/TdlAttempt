#import tdl
from ConsoleWrapper import *
from BSPDungeonGenerator import doShit
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
    while not tdl.event.is_window_closed(): # <--- not shit
        clearConsole()
        doShit()
        #drawRect(0,0,10,10)
        #SHIT ENDS HERE.
        tdl.flush()
        # putChar(" ", playerx, playery)
        # handle keys and exit game if needed
        keys()
        if exit_game:
            break

i = 127
mainLoop()