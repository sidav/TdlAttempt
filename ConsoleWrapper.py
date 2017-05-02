import tdl


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



def setBackgroundColor(r, g, b):
    global BACKCOLOR
    BACKCOLOR = (r, g, b)


def setForegroundColor(r, g, b):
    global FORECOLOR
    FORECOLOR = (r, g, b)



def flushConsole():
    tdl.flush()


def clearConsole():
    console.clear(bg = none, fg = (0, 0, 0))


def readKey():
    global LAST_KEY_PRESSED
    LAST_KEY_PRESSED = tdl.event.key_wait()
    return LAST_KEY_PRESSED


