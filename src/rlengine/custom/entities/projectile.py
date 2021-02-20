import pygame
from src.rlengine.game.entities import MapFloatEntity
from src.rlengine.config.constants import *


# TODO better naming of states - better state management?
class Projectile(MapFloatEntity):
    def __init__(self, cur_map, x, y):
        MapFloatEntity.__init__(self, 1, cur_map, x, y, {})
        self.x = x
        self.y = y
        self.w = 6
        self.h = 6
        self.ddx = 0
        self.ddy = 0
        self.block_colour = (0, 255, 0)
        self.block_colour_colliding = (255, 255, 255)
        self.is_colliding = False

        self.fading_steps = 40
        self.fading_in = True

    # TODO pass x and y offsets?
    def hit_wall(self, walls_hit):
        if RL_TOP in walls_hit or RL_BOTTOM in walls_hit:
            self.ddy = self.ddy * (-1)

        if RL_LEFT in walls_hit or RL_RIGHT in walls_hit:
            self.ddx = self.ddx * (-1)

    # TODO support for multiple primitives with different positions
    def get_sprites_to_draw(self):
        return [['circle']]

    def step(self, next_x, next_y):
        self.is_colliding = False
        if self.life_steps >= self.fading_steps:
            self.fading_in = False

        MapFloatEntity.step(self, next_x, next_y)

    def get_block_colour(self):
        if self.fading_in:
            return (25, 25, 25)

        if self.is_colliding:
            return self.block_colour_colliding
        else:
            return self.block_colour
