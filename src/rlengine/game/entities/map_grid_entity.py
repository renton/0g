from .map_entity import MapEntity

from src.rlengine.config import GAME_CONFIGS


class MapGridEntity(MapEntity):
    def __init__(self, e_id, cur_map, x, y, attr_data=None):
        MapEntity.__init__(self, e_id, cur_map, x, y, attr_data)
        self.tile_x = 1
        self.tile_y = 1
        self.w = self.h = GAME_CONFIGS['tile_configs']['tile_size']

    def step(self):
        MapEntity.step(self)

    def get_xy(self):
        return (
            self.tile_x * GAME_CONFIGS['tile_configs']['tile_size'],
            self.tile_y * GAME_CONFIGS['tile_configs']['tile_size']
        )
