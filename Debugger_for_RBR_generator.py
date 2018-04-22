import RBRDungeonGenerator
import ConsoleWrapper as CW
from Main import SCREEN_WIDTH, SCREEN_HEIGHT

_WALL_CODE = chr(177)
_FLOOR_CODE = '.'
_CLDOOR_CODE = '+'
_OPDOOR_CODE = '\\'


tile_names = {
    'wall': _WALL_CODE,
    'floor': _FLOOR_CODE,
    'door': _CLDOOR_CODE
}


tile_colors = {
    _WALL_CODE: (128, 128, 128),
    _FLOOR_CODE: (64, 64, 64),
    _CLDOOR_CODE: (128, 128, 128),
    _OPDOOR_CODE: (128, 64, 0)
}


def debug_RBR():
    map = RBRDungeonGenerator.generateDungeon(SCREEN_WIDTH, SCREEN_HEIGHT)
    for i in range(SCREEN_WIDTH):
        for j in range(SCREEN_HEIGHT):
            CW.putChar(tile_names[map[i][j]], i, j)
    CW.flushConsole()
    while not CW.isWindowClosed():
        CW.readKey()

