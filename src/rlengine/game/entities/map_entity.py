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

        # come from animations
        self.tile_id = 0
        self.tileset_id = 0

        self.is_visible = True
        self.is_active = True

        self.ai = None

    def get_hitbox(self):
        return self.get_rect()

    def get_sprites_to_draw(self):
        return [self._generate_base_tile()]

    def _get_current_sprite(self):
        return (self.tile_id, self.tileset_id)

    def _generate_base_tile(self):
        tile_id, tileset_id = self._get_current_sprite()
        return ('sprite', tile_id, tileset_id)

    def get_sprite_draw_offset_xy(self):
        return (0, 0)

    def set_ai(self, ai):
        self.ai = ai

    def get_block_colour(self):
        return self.block_colour

    def get_rect(self):
        x, y = self.get_xy()
        return pygame.Rect(x, y, self.w, self.h)

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def get_xy(self):
        return (self.x, self.y)

    def step(self):
        Entity.step(self)
