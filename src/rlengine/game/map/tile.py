# note: only 1 destructable entity can ever be on a tile
# TODO entity tiles should be an abstraction up
class Tile():
    def __init__(self, tile_data):
        self.tile_data = tile_data
        self.entities = {}

        self._load_data(self.tile_data)

    def _load_data(self, dataset):
        for k, v in dataset.items():
            if hasattr(v, '__call__'):
                setattr(self, k, v())
            else:
                setattr(self, k, v)

    def _modify_data(self, dataset):
        for k, v in dataset.items():
            if hasattr(self, k):
                if hasattr(v, '__call__'):
                    setattr(self, k, getattr(self, k) + v())
                else:
                    setattr(self, k, getattr(self, k) + v)

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
