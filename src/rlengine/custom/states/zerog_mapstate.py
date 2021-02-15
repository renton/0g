import pygame
import sys
from pygame.locals import *

from random import randrange, choice, randint

from src.rlengine.states import EntityMapState
from src.rlengine.config import GAME_CONFIGS
from src.rlengine.renderers import MapRenderer
from src.rlengine.custom.entities import Hero


class ZeroGMapState(EntityMapState):
    def __init__(self, game, defaultmap):
        EntityMapState.__init__(self, game, defaultmap)
        self.game.bind_player_entity(Hero(defaultmap, 20, 20))
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

        EntityMapState.input(self, im)

