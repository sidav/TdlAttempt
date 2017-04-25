#import tdl
from ConsoleWrapper import *
from SidavRandom import *

playerx = SCREEN_WIDTH // 2
playery = SCREEN_HEIGHT // 2
exit_game = False

def keys():
    global playerx, playery, exit_game
    keypressed = readKey()
    if (keypressed.key == 'ESCAPE') or (keypressed.key == 'ESCAPE'): exit_game = True
    if (keypressed.key == 'UP') or (keypressed.key == 'KP8'): playery -= 1
    if (keypressed.key == 'DOWN'): playery += 1
    if (keypressed.key == 'LEFT'): playerx -= 1
    if (keypressed.key == 'RIGHT'): playerx += 1


i = 127

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