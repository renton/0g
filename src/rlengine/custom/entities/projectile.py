import pygame
from src.rlengine.game.entities import MapFloatEntity


class Projectile(MapFloatEntity):
    def __init__(self, cur_map, x, y):
        MapFloatEntity.__init__(self, 1, cur_map, x, y, {})
        self.x = x
        self.y = y
        self.w = 6
        self.h = 6
        self.ddx = 0.7
        self.ddy = 0.7
        self.block_colour = (0, 255, 0)
        self.block_colour_colliding = (40, 40, 40)
        self.is_colliding = False

    def get_hitbox(self):
        x, y = self.get_xy()
        return pygame.Rect(x-(self.w/2), y-(self.h/2), self.w, self.h)

    # TODO pass x and y offsets?
    def hit_wall(self):
        self.ddx = self.ddx * (-1)
        self.ddy = self.ddy * (-1)

    # TODO support for multiple primitives with different positions
    def get_sprites_to_draw(self):
        return [['circle']]

    def step(self, next_x, next_y):
        self.is_colliding = False
        MapFloatEntity.step(self, next_x, next_y)

    def get_block_colour(self):
        if self.is_colliding:
            return self.block_colour_colliding
        else:
            return self.block_colour
