from .map_entity import MapEntity


class MapFloatEntity(MapEntity):
    def __init__(self, e_id, cur_map, x, y, attr_data=None):
        self.ddx = 0.0
        self.ddy = 0.0

        self.h = 10
        self.w = 10

        MapEntity.__init__(self, e_id, cur_map, x, y, attr_data)

    def step(self):     
        MapEntity.step(self)
        self.x += self.ddx
        self.y += self.ddy

    def set_ddx(self, ddx):
        self.ddx = ddx

    def set_ddy(self, ddy):
        self.ddy = ddy

    def get_xy(self):
        return (self.x, self.y)
