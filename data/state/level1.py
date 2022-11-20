###############################################################################
# File Name  : level1.py
# Date       : 11/18/2022
# Description:
###############################################################################

import pygame as pg
from .. import constants as c
from .. import tools


class Level(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        # calls when the state object is created
        self.game_info = persist
        self.persist = self.game_info

        self.game_info[c.CURRENT_TIME] = current_time
        self.game_info[c.LEVEL_STATE] = c.NOT_FROZEN
        self.game_info[c.MARIO_DEAD] = False

        self.state = c.NOT_FROZEN
        self.death_timer = 0
        self.flag_score = None

