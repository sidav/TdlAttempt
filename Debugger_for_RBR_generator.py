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
    'ustairs': '<',
    'dstairs': '>',
    'debugtile': '#'
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
    RBRDungeonGenerator.setRandomSeed(int(time.time()))
    while not CW.isWindowClosed():
        key_pressed_text = ''
        map = RBRDungeonGenerator.generateDungeon(SCREEN_WIDTH, 21)

        for i in range(SCREEN_WIDTH):
            for j in range(21):
                tile_char = tile_names[map[i][j].tile_code]
                #CW.setForegroundColor(tile_colors[tile_char])
                CW.setForegroundColor(key_levels[map[i][j].key_level])
                CW.putChar(tile_char, i, j)
                if map[i][j].tile_code == 'debugtile':
                    CW.setForegroundColor(255, 0, 255)

        CW.flushConsole()
        while key_pressed_text != 'SPACE':
            key_pressed_text = CW.readKey().keychar

