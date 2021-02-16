from pygame.constants import K_x
from .map_entity import MapEntity


class MapFloatEntity(MapEntity):
    def __init__(self, e_id, cur_map, x, y, attr_data=None):
        self.ddx = 0.0
        self.ddy = 0.0

        self.h = 10
        self.w = 10

        self.snap_to_grid = False

        MapEntity.__init__(self, e_id, cur_map, x, y, attr_data)

    def hit_wall(self):
        pass

    def step(self):
        MapEntity.step(self)
        next_x = self.x + self.ddx
        next_y = self.y + self.ddy

        did_move = (self.x != next_x) or (self.y != next_y)
        return (did_move, next_x, next_y)

    def set_ddx(self, ddx):
        self.ddx = ddx

    def set_ddy(self, ddy):
        self.ddy = ddy
