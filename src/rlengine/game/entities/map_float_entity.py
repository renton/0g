from .map_entity import MapEntity

# TODO should this be a mixin?


class MapFloatEntity(MapEntity):
    def __init__(self, e_id, cur_map, x, y, attr_data=None):
        self.ddx = 0.0
        self.ddy = 0.0

        self.ignore_walls = False

        MapEntity.__init__(self, e_id, cur_map, x, y, attr_data)
        self.h = 10
        self.w = 10

    def hit_wall(self, walls_hit):
        pass

    def get_center_point(self):
        x, y = self.get_xy()
        return (x + (self.w/2), y + (self.h/2))

    def calculate_step(self):
        next_x = self.x + self.ddx
        next_y = self.y + self.ddy

        did_move = (self.x != next_x) or (self.y != next_y)
        return (did_move, next_x, next_y)

    def step(self, next_x, next_y):
        MapEntity.step(self)
        self.set_xy(next_x, next_y)

    def set_ddx(self, ddx):
        self.ddx = ddx

    def set_ddy(self, ddy):
        self.ddy = ddy
