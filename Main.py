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
boolmap = [[1] * 3 for _ in range(3)]
boolmap = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,0,1,1],
    [1,1,1,1,1],
]
boolmap = [[1] * 9 for _ in range(9)]
boolmap[0][3] = 0
boolmap[0][6] = 0
boolmap[1][3] = 0
boolmap[2][2] = 0
boolmap[2][7] = 0
boolmap[2][8] = 0
boolmap[3][3] = 0
boolmap[3][4] = 0
boolmap[3][5] = 0
boolmap[4][4] = 0
boolmap[4][4] = 0
boolmap[4][6] = 0
boolmap[4][7] = 0
boolmap[5][6] = 0
boolmap[6][4] = 0
boolmap[6][6] = 0
boolmap[7][2] = 0
boolmap[7][3] = 0
boolmap[7][5] = 0
boolmap[8][1] = 0
boolmap[8][4] = 0
print(boolmap)
shit = CrapPathfinding(boolmap, 0, 8, 8, 2)
crapPath = shit.findPath()
print("PATH IS:")
for i in crapPath:
    print(str(i.x) + " " + str(i.y))