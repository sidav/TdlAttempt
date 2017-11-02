# import sys
# import os
# import tdl
from ConsoleWrapper import *
import RBRDungeonGenerator
import BSPDungeonGenerator
#from BSPDungeonGenerator import generateMap
from CADungeonGenerator import doCAshit
from CALandscapeGenerator import doCALandshit
import SidavLOS as LOS

from SidavRandom import *
#DELETE FOLLOWING AFTER DEBUG:
from SimplePathfinding import *
from AStarPathfinding import *

playerx = SCREEN_WIDTH // 2
playery = SCREEN_HEIGHT // 2
map = [[]]
exit_game = False
Re_generate = True
generator = 3

def keys():
    global playerx, playery, exit_game, Re_generate, generator
    keypressed = readKey()
    if (keypressed.key == 'ESCAPE') or (keypressed.key == 'ESCAPE'): exit_game = True
    if (keypressed.key == 'UP') or (keypressed.key == 'KP8'): playery -= 1
    if (keypressed.key == 'DOWN') or (keypressed.key == 'KP2'): playery += 1
    if (keypressed.key == 'LEFT') or (keypressed.key == 'KP4'): playerx -= 1
    if (keypressed.key == 'RIGHT') or (keypressed.key == 'KP6'): playerx += 1
    if (keypressed.key == 'SPACE'):
        Re_generate = True
    if (keypressed.key == 'ENTER'):
        randomize()
        generator+=1
        if generator > 3:
            generator = 0
        Re_generate = True


def main():
    global Re_generate, map
    while not tdl.event.is_window_closed(): # <--- not shit
        if Re_generate:
            clearConsole()
            if generator == 0:
                doCALandshit(80, 25) #It's the landscape generator's shit.
                setForegroundColor(200,100,30)
                putString("CA Landscape Generator", 0, 0)
            if generator == 1:
                map = BSPDungeonGenerator.generateMapWithRandomParams(80, 25) #It's BSP generator's shit.
                setForegroundColor(200,100,30)
                putString("BSP Generator", 0, 0)
            elif generator == 2:
                map = doCAshit() #It's the cave generator shit
                setForegroundColor(200, 100, 30)
                putString("Cave CA Generator", 0, 0)
            elif generator == 3:
                map = RBRDungeonGenerator.getMap()
                setForegroundColor(200, 100, 30)
                putString("Room-By-Room Generator", 0, 0)
            Re_generate = False
        #drawRect(3,1,10,10)
        if generator != 0:
            ##FOLLOWING SHIT IS LOS TEST
            clearConsole()
            obstrMap = [[True] * (len(map[0])) for _ in range(len(map))]
            for i, row in enumerate(map):
                for j, col in enumerate(map[0]):
                    if map[i][j] == BSPDungeonGenerator._DOOR_CODE:
                        map[i][j] = BSPDungeonGenerator._FLOOR_CODE
                    if map[i][j] == BSPDungeonGenerator._FLOOR_CODE:
                        obstrMap[i][j] = False
            LOS.setvisionObstructingMap(obstrMap)
            #visMap = LOS.getVisibilityTable(playerx, playery)
            setForegroundColor(12, 12, 72)
            drawCharArray(map)
            for i in range(len(map)):
                for j in range(len(map[0])):
                    if LOS.visibleLineExists(playerx, playery, i, j):
                        setBackgroundColor(100, 100, 100)
                        setForegroundColor(255,255,255)
                        putChar(map[i][j], i, j)
            setBackgroundColor(255, 0, 0)
            putChar('@', playerx, playery)
            setBackgroundColor(0, 0, 0)
            ##LOS TEST ENDS HERE
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