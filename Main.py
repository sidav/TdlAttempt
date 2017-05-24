# import sys
# import os
# import tdl
from ConsoleWrapper import *
from BSPDungeonGenerator import doShit
from CellularAutomataDungeonGenerator import doCAshit
from SidavRandom import *
#DELETE FOLLOWING AFTER DEBUG:
from SimplePathfinding import *
from AStarPathfinding import *

playerx = SCREEN_WIDTH // 2
playery = SCREEN_HEIGHT // 2
exit_game = False
Re_generate = True
BSP: bool = True

def keys():
    global playerx, playery, exit_game, Re_generate, BSP
    keypressed = readKey()
    if (keypressed.key == 'ESCAPE') or (keypressed.key == 'ESCAPE'): exit_game = True
    if (keypressed.key == 'UP') or (keypressed.key == 'KP8'): playery -= 1
    if (keypressed.key == 'DOWN'): playery += 1
    if (keypressed.key == 'LEFT'): playerx -= 1
    if (keypressed.key == 'RIGHT'): playerx += 1
    if (keypressed.key == 'SPACE'):
        Re_generate = True
    if (keypressed.key == 'ENTER'):
        randomize()
        BSP = not BSP
        Re_generate = True

def main():
    global Re_generate
    while not tdl.event.is_window_closed(): # <--- not shit
        if Re_generate:
            clearConsole()
            if BSP:
                doShit() #It's BSP generator's shit.
                setForegroundColor(200,100,30)
                putString("BSP Generator", 0, 0)
            else:
                doCAshit() #It's the cave generator shit
                setForegroundColor(200, 100, 30)
                putString("Cave CA Generator", 0, 0)
            Re_generate = False
        #drawRect(3,1,10,10)
    #################
    #SHIT ENDS HERE.#
    #################
        tdl.flush()
        # putChar(" ", playerx, playery)
        # handle keys and exit game if needed
        keys()
        if exit_game:
            break

i = 127
if __name__ == '__main__':
    main()