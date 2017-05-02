#import tdl
#UNCOMMENT THE FOLLOWING LINE FOR THE TDL USE:
#from ConsoleWrapper import *
from SidavRandom import *
#DELETE FOLLOWING AFTER DEBUG:
from SimplePathfinding import *

#playerx = SCREEN_WIDTH // 2
#playery = SCREEN_HEIGHT // 2
exit_game = False

def keys():
    global playerx, playery, exit_game
    keypressed = readKey()
    if (keypressed.key == 'ESCAPE') or (keypressed.key == 'ESCAPE'): exit_game = True
    if (keypressed.key == 'UP') or (keypressed.key == 'KP8'): playery -= 1
    if (keypressed.key == 'DOWN'): playery += 1
    if (keypressed.key == 'LEFT'): playerx -= 1
    if (keypressed.key == 'RIGHT'): playerx += 1

def mainLoop():
    while not tdl.event.is_window_closed():
        setForegroundColor(rand(256), rand(256), rand(256))
        string = "Look at my fucking console. Look. "
        # for y in range(SCREEN_HEIGHT):
        #     for x in range (SCREEN_WIDTH):
        #         setForegroundColor(rand(256), rand(256), rand(256))
        #         putChar(string[(x+y)%len(string)], x, y)
        #         #tdl.flush()
        putChar("@", playerx, playery)
        tdl.flush()
        # putChar(" ", playerx, playery)
        # handle keys and exit game if needed
        keys()
        if exit_game:
            break


i = 127
#UNCOMMENT THE FOLLOWING LINE FOR THE TDL USE:
#mainLoop()

#DELETE THE FOLLOWING AFTER THE DEBUG:
boolmap = [[1] * 5 for _ in range(5)]
boolmap[1][4] = 0
boolmap[1][3] = 0
boolmap[1][2] = 0
boolmap[1][1] = 0
boolmap[3][0] = 0
boolmap[3][1] = 0
boolmap[3][2] = 0
print(boolmap)
shit = CrapPathfinding(boolmap, 0, 4, 4, 1)
crapPath = shit.findPath()
print("PATH IS:")
for i in crapPath:
    print(str(i.x) + " " + str(i.y))