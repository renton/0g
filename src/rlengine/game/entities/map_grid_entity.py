from pygame.constants import K_x
from .map_entity import MapEntity

from src.rlengine.config import GAME_CONFIGS
# TODO should this be a mixin?


class MapGridEntity(MapEntity):
    def __init__(self, e_id, cur_map, x, y, attr_data=None):
        MapEntity.__init__(self, e_id, cur_map, x, y, attr_data)
        self.tile_x = 1
        self.tile_y = 1
        self.snap_to_grid = True
        self.w = self.h = GAME_CONFIGS['tile_configs']['tile_size']

        self.move_tile_x = 0
        self.move_tile_y = 0

    def calculate_step(self):
        MapEntity.step(self)
        if self.move_tile_x == 0 and self.move_tile_y == 0:
            (next_x, next_y) = self.get_xy()
            return (False, next_x, next_y)

        next_tile_x = self.tile_x + self.move_tile_x
        next_tile_y = self.tile_y + self.move_tile_y

        (next_x, next_y) = self.get_xy_from_tiles(next_tile_x, next_tile_y)

        did_move = (self.tile_x != next_tile_x) or (self.tile_y != next_tile_y)

        self._reset_move()
        return (did_move, next_x, next_y)

    def step(self, next_x, next_y):
        self.set_xy(next_x, next_y)

    def _reset_move(self):
        self.move_tile_x = 0
        self.move_tile_y = 0

    def set_xy(self, x, y):
        self.tile_x = int(x / GAME_CONFIGS['tile_configs']['tile_size'])
        self.tile_y = int(y / GAME_CONFIGS['tile_configs']['tile_size'])

    def get_xy(self):
        return self.get_xy_from_tiles(self.tile_x, self.tile_y)

    def get_xy_from_tiles(self, tile_x, tile_y):
        return (
            tile_x * GAME_CONFIGS['tile_configs']['tile_size'],
            tile_y * GAME_CONFIGS['tile_configs']['tile_size']
        )
