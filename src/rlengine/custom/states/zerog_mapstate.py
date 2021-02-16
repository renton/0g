import pygame
import sys
from pygame.locals import *

from random import randrange, choice, randint

from src.rlengine.states import EntityMapState
from src.rlengine.config import GAME_CONFIGS
from src.rlengine.renderers import MapRenderer
from src.rlengine.custom.entities import Hero, Projectile

START_CAMERA_X = 0
START_CAMERA_Y = 0


# TODO step override to plant projectiles
class ZeroGMapState(EntityMapState):
    def __init__(self, game, defaultmap):
        EntityMapState.__init__(self, game, defaultmap)
        self._set_camera(START_CAMERA_X, START_CAMERA_Y)
        self.game.bind_player_entity(Hero(defaultmap, 40, 40))
        self.player = self.game.player1

        self.add_entity_to_map(self.player.e)

    def input(self, im):
        if self.im.is_key_event(KEYDOWN, K_UP):
            # self.player.e.move_tile_y = -1
            self.player.e.set_ddy(-0.6)
            self.player.e.set_ddx(0)
        if self.im.is_key_event(KEYDOWN, K_DOWN):
            # self.player.e.move_tile_y = 1
            self.player.e.set_ddy(0.6)
            self.player.e.set_ddx(0)
        if self.im.is_key_event(KEYDOWN, K_LEFT):
            # self.player.e.move_tile_x = -1
            self.player.e.set_ddx(-0.6)
            self.player.e.set_ddy(0)
        if self.im.is_key_event(KEYDOWN, K_RIGHT):
            # self.player.e.move_tile_x = 1
            self.player.e.set_ddx(0.6)
            self.player.e.set_ddy(0)

        if self.im.is_key_event(KEYDOWN, K_p):
            mouse_map_x, mouse_map_y = self.mouse_to_map_coords()
            self.add_entity_to_map(Projectile(self.cur_map, mouse_map_x, mouse_map_y))

        if self.im.is_lmouse_pressed():
            mouse_map_x, mouse_map_y = self.mouse_to_map_coords()
            self.player.e.action_launch(mouse_map_x, mouse_map_y)

        EntityMapState.input(self, im)

