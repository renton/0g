from .entity import Entity
# TODO sprite might need it's own class


class MapEntity(Entity):
    def __init__(self, e_id, cur_map, x, y, attr_data=None):
        Entity.__init__(self, e_id, attr_data)

        self.cur_map = cur_map
        self.x = x
        self.y = y

        self.ai = None

    def get_sprites_to_draw(self):
        return [self._generate_base_tile()]

    def _generate_base_tile(self):
        return (self.tileset_id, self.tile_id)

    def set_ai(self, ai):
        self.ai = ai

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def get_xy(self):
        return (self.x, self.y)

    def step(self):
        Entity.step(self)
