###############################################################################
# File Name  : mario.py
# Date       : 11/19/2022
# Description: Mario logic.
###############################################################################

import pygame as pg
from .. import tools, setup
from .. import constants as c


class Mario(pg.sprite.Sprite):
    def __init__(self):
        self.sprite_sheet = setup.GFX['NES_Mario_Luigi.png']
        self.setup_timers()

    def setup_timer(self):
        # Sets up timer for animation
        self.walking_timer = 0
        self.invincible_animation_timer = 0
        self.invincible_start_timer = 0
        self.death_Timer = 0

    def setup_state_booleans(self):
        # Setup a boolean that affects Mario behavior
        self.facing_right = True
        self.allow_jump = True
        self.dead = False
        self.invincible = False
        self.big = False
        self.allow_fireball = True

    def setup_forces(self):
        # Setup the forces that affects Mario velocity
        self.x_vel = 0
        self.y_val = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL

    def setup_counters(self):
        # Keep track of various
        self.frame_index = 0
        self.invincible_index = 0

    def load_images_from_sheet(self):
        self.right_frames = []
        self.left_frames = []

        self.right_small_normal_frames = []
        self.left_small_normal_frames = []
        self.right_small_green_frames = []
        self.left_small_green_frames = []
        self.right_small_red_frames = []
        self.left_small_red_frames = []
        self.right_small_black_frames = []
        self.left_small_black_frames = []

        self.right_big_normal_frames = []
        self.left_big_normal_frames = []
        self.right_big_green_frames = []
        self.left_big_green_frames = []
        self.right_big_red_frames = []
        self.left_big_red_frames = []
        self.right_big_black_frames = []
        self.left_big_black_frames = []

        self.right.fire_frames = []
        self.left.fire_frames = []
