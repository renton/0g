import pygame
from .entity import Entity
# TODO sprite might need it's own class
# TODO should be a mixin with no inherited class?


class MapEntity(Entity):
    def __init__(self, e_id, cur_map, x, y, attr_data=None):
        Entity.__init__(self, e_id, attr_data)

        self.block_colour = (255, 0, 0)
        self.cur_map = cur_map
        self.x = x
        self.y = y
        self.w = 0
        self.h = 0

        self.ai = None

    def get_sprites_to_draw(self):
        return [self._generate_base_tile()]

    def _generate_base_tile(self):
        return (self.tileset_id, self.tile_id)

    def set_ai(self, ai):
        self.ai = ai

    def get_rect(self):
        x, y = self.get_xy()
        print(self.e_id, x, y, self.w, self.h)
        return pygame.Rect(x, y, self.w, self.h)

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def get_xy(self):
        return (self.x, self.y)

    def step(self):
        Entity.step(self)
