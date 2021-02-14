from src.rlengine.game.entities import MapFloatEntity


class Hero(MapFloatEntity):
    def __init__(self, cur_map, x, y):
        MapFloatEntity.__init__(self, 0, cur_map, x, y, {})
