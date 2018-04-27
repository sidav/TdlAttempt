import RBRDungeonGenerator
import ConsoleWrapper as CW
from Main import SCREEN_WIDTH, SCREEN_HEIGHT
import time

_WALL_CODE = chr(177)
_FLOOR_CODE = '.'
_CLDOOR_CODE = '+'
_OPDOOR_CODE = '\\'


tile_names = {
    'wall': _WALL_CODE,
    'floor': _FLOOR_CODE,
    'door': _CLDOOR_CODE,
    'ustairs' : '>',
    'dstairs': '<'
}


tile_colors = {
    _WALL_CODE: (128, 128, 128),
    _FLOOR_CODE: (64, 64, 64),
    _CLDOOR_CODE: (128, 128, 128),
    _OPDOOR_CODE: (128, 64, 0)
}

key_levels = {
    0: (128, 128, 128),
    1: (0, 128, 0),
    2: (128, 0, 0),
    3: (128, 0, 128)
}

def debug_RBR():
    while not CW.isWindowClosed():
        RBRDungeonGenerator.setRandomSeed(int(time.time()))
        map = RBRDungeonGenerator.generateDungeon(SCREEN_WIDTH, SCREEN_HEIGHT)

        for i in range(SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                tile_char = tile_names[map[i][j].char]
                #CW.setForegroundColor(tile_colors[tile_char])
                CW.setForegroundColor(key_levels[map[i][j].key_level])
                CW.putChar(tile_char, i, j)

        CW.flushConsole()
        CW.readKey()

