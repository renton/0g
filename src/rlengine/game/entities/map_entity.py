from .entity import Entity


class MapEntity(Entity):
    def __init__(self, cur_map, x, y):
        Entity.__init__(self)

        self.cur_map = cur_map
        self.x = x
        self.y = y
