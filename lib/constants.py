from enum import Enum

COLOR_BLACK = (0x00, 0x00, 0x00)
COLOR_BLUE = (0x00, 0x00, 0xFF)
COLOR_GREEN = (0x00, 0xFF, 0x00)
COLOR_RED = (0xFF, 0x00, 0x00)
COLOR_WHITE = (0xFF, 0xFF, 0xFF)

FONT_END = 64
FONT_MINI = 10
FONT_NORMAL = 16

ACCEL_SPEED = 0.5
BACKGROUND_COLOR = COLOR_BLACK
ENTITY_SIZE = 32
GAME_WIDTH = 640
GAME_HEIGHT = 480
MAX_ENEMY_COUNT = 25
MAX_TRAIL_COUNT = 50
PLAYER_COLOR = COLOR_BLUE
TIME_TO_LOSE = 10 # Seconds
TRAIL_COLOR = COLOR_RED

# pylint: disable=I0011,invalid-name
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
