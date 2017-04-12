from enum import Enum
import lib.config as config

COLOR_BLACK = (0x00, 0x00, 0x00)
COLOR_BLUE = (0x00, 0x00, 0xFF)
COLOR_GREEN = (0x00, 0xFF, 0x00)
COLOR_RED = (0xFF, 0x00, 0x00)
COLOR_WHITE = (0xFF, 0xFF, 0xFF)

FONT_END = 64
FONT_MINI = 10
FONT_NORMAL = 16

BACKGROUND_COLOR = COLOR_BLACK
PLAYER_COLOR = COLOR_BLUE
TRAIL_COLOR = COLOR_RED

# Config variables
# pylint: disable=I0011,C0103
config = config.load()
# pylint: disable=I0011,I0012; enable=C0103

ACCEL_SPEED = config["accel_speed"]
ENTITY_SIZE = config["entity_size"]
GAME_WIDTH = config["screen"]["width"]
GAME_HEIGHT = config["screen"]["height"]
MAX_ENEMY_COUNT = config["max_enemies"]
MAX_TRAIL_COUNT = config["max_trail"]
TIME_TO_LOSE = config["lose_time"] # Seconds

# pylint: disable=I0011,invalid-name
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
