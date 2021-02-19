from src.rlengine.game.entities import MapFloatEntity


class Projectile(MapFloatEntity):
    def __init__(self, cur_map, x, y):
        MapFloatEntity.__init__(self, 1, cur_map, x, y, {})
        self.x = x
        self.y = y
        self.ddx = 0.7
        self.ddy = 0.7

    # TODO pass x and y offsets?
    def hit_wall(self):
        self.ddx = self.ddx * (-1)
        self.ddy = self.ddy * (-1)
