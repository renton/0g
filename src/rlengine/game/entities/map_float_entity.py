from .map_entity import MapEntity


class MapFloatEntity(MapEntity):
    def __init__(self, entity, cur_map, x, y):
        MapEntity.__init__(self, entity, cur_map, x, y)