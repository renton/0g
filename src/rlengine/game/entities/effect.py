from .map_float_entity import MapFloatEntity


class Effect(MapFloatEntity):
    def __init__(self, e_id, cur_map, x, y, effect_lifespan, attr_data=None):
        MapFloatEntity.__init__(self, e_id, cur_map, x, y, attr_data)
        self.ignore_walls = True
        self.effect_lifespan = effect_lifespan

    def get_sprites_to_draw(self):
        return [['circle']]

    def calculate_step(self):
        x, y = self.get_xy()
        return (True, x, y)

    def step(self, next_x, next_y):
        if self.get_lifespan() > self.effect_lifespan:
            self.is_active = False
        MapFloatEntity.step(self, next_x, next_y)
