import tdl
from BresenhamLine import *

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 25

LIMIT_FPS = 20  # 20 frames-per-second maximum

tdl.set_font('terminal8x12_gs_ro.png', greyscale=True, altLayout=False)
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen= False, renderer= "SDL")
FORECOLOR = (255,255,255)
BACKCOLOR = (0, 0, 0)

# LAST_KEY_PRESSED = tdl.event

def putChar(char, x, y):
    console.draw_char(x, y, char, bg=BACKCOLOR, fg=FORECOLOR)


def putString(string, x, y):
    console.draw_str(x, y, string, bg=BACKCOLOR, fg=FORECOLOR)


def drawLine(x0, y0, x1, y1):
    line = get_line(x0, y0, x1, y1)
    for i in line:
        putChar("#", i.x, i.y)

def drawCircle(x0, y0, radius):
    circle = get_circle(x0, y0, radius)
    for i in circle:
        putChar("#", i.x, i.y)

def drawRect(x0, y0, w, h):
    for i in range(x0, x0+w):
        putChar("#", i, y0)
        putChar("#", i, y0+h-1)
    for j in range(y0, y0+h):
        putChar("#", x0, j)
        putChar("#", x0+w-1, j)

def setBackgroundColor(r, g, b):
    global BACKCOLOR
    BACKCOLOR = (r, g, b)


def setForegroundColor(r, g, b):
    global FORECOLOR
    FORECOLOR = (r, g, b)



def flushConsole():
    tdl.flush()


def clearConsole():
    console.clear(bg = (0, 0, 0), fg = (0, 0, 0))


def readKey():
    global LAST_KEY_PRESSED
    LAST_KEY_PRESSED = tdl.event.key_wait()
    return LAST_KEY_PRESSED


