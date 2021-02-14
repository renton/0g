from .tile import Tile
from random import choice, randint
from src.rlengine.config import GAME_CONFIGS


# TODO walkable, los is an abstraction up
# map should not know what an entity is?
class Map():

    def __init__(self, tile_data, tile_klass, gen_sample=False):
        self.tile_klass = tile_klass
        self.tile_data = tile_data
        self.tiles = []
        self.size_x, self.size_y = 0, 0

        if gen_sample:
            self._gen_sample()

    def build_tile(self, id):
        return self.tile_klass(self.get_tile_data(id))

    def get_tile_data(self, id):
        if id in self.tile_data['gametiles']:
            return self.tile_data['gametiles'][id]
        else:
            return self.tile_data['gametiles'][0]

    def _gen_sample(self):
        for i in range(GAME_CONFIGS['map_configs']['sample_map_x_size']):
            self.tiles.append([])
            for j in range(GAME_CONFIGS['map_configs']['sample_map_y_size']):
                if (
                    (j == (GAME_CONFIGS['map_configs']['sample_map_y_size'] - 1)) or
                    (j == 0) or (i == (GAME_CONFIGS['map_configs']['sample_map_x_size'] - 1)) or
                    (i == 0)
                ):
                    self.tiles[i].append(self.build_tile(0))
                else:
                    if randint(0, 9) == 1:
                        self.tiles[i].append(self.build_tile(0))
                    else:
                        self.tiles[i].append(self.build_tile(1))

        self.size_x = len(self.tiles)
        self.size_y = len(self.tiles[0])

    def empty_map(self):
        self.tiles[:] = []
