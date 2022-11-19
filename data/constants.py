###############################################################################
# File Name  : constants.py
# Date       : 11/18/2022
# Description: Game constants.
###############################################################################

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Super Mario Bros 1-1"

# Colors
# (R,G,B)
GRAY = (100, 100, 100)
NAVY_BLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FOREST_GREEN = (31, 162, 35)
BLUE = (0, 0, 255)
SKY_BLUE = (39, 145, 251)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
NEAR_BLACK = (19, 15, 48)
COM_BLUE = (233, 232, 255)
GOLD = (255, 215, 0)

BG_COLOR = WHITE

SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLIER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

# Mario Forces
WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01
JUMP_GRAVITY = .31
JUMP_VEL = -10
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6

# Mario states
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAG_POLE = 'flag pole'
GAME_OVER = 'game over'
LEVEL1 = 'level1'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'

# Goomba States
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

# Koopa states
SHELL_SLIDE = 'shell slide'

# Brick states
RESTING = 'resting'
BUMPED = 'bumped'

# Coin states
OPENED = 'opened'
SPIN = 'spin'

# Mushroom states
REVEAL = 'reveal'
SLIDE = 'slide'

# star states
BOUNCE = 'bounce'

# Fire states
FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'

# Brick and coin box content
MUSHROOM = 'mushroom'
STAR = 'star'
FIRE_FLOWER = 'fire flower'
SIX_COINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'
FIRE_BALL = 'fireball'

# List of enemies
GOOMBA = 'goomba'
KOOPA = 'koopa'

# Level States
FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

# Flag state
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

# 1up score
ONEUP = '379'

# Main menu cursor states
PLAYER1 = '1 player'
PLAYER2 = '2 player'

# Game info dictionary keys
COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
MARIO_DEAD = 'mario dead'

# States for entire game
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'

# Sound States
NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'
MARIO_INVINCIBLE = 'mario invincible'
