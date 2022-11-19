###############################################################################
# File Name  : collider.py
# Date       : 11/19/2022
# Description:
###############################################################################

import pygame as pg
from .. import constants as c

class Collider(pg.sprite.Sprite):
    def __init__(self,x,y,width,height,name='collider'):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width,height)).convert()
        #fill image with red color

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.state = None
        