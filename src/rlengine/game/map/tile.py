# note: only 1 destructable entity can ever be on a tile
# TODO entity tiles should be an abstraction up
class Tile():
    def __init__(self, tile_data):
        self.tile_data = tile_data
        self.entities = {}

        self._load_tile_attributes()

    def _load_tile_attributes(self):
        self.tileset_id = self.tile_data['tileset_id']
        self.tile_id = self.tile_data['tile_id']
        self.block_colour = self.tile_data['block_colour']

    # def set_entity(self, e):
    #     self.entities[e.u_id] = e

    # def unset_entity(self, e):
    #     if e.u_id in self.entities:            
    #         del self.entities[e.u_id]

    # def can_move(self):
    #     for k, v in self.entities.items():
    #         if not v.passable:
    #             return False
    #     return self.walkable

    # def get_entities(self):
    #     return self.entities

    # def get_attackable_target(self):
    #     for k, v in self.entities.items():
    #         if v.attackable:
    #             return v
    #     return None
