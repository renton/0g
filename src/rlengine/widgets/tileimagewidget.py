from src.rlengine.widgets import Widget
from src.rlengine.config import GAME_CONFIGS


class TileImageWidget(Widget):
    def __init__(self, x, y, select_event=None):
        Widget.__init__(self, x, y, select_event)
        self.tileset_id = None
        self.tile_id = None

    def set_tile(self, tileset_id, tile_id):
        self.tileset_id = tileset_id
        self.tile_id = tile_id

    def draw(self, screen, rm):
        if self.tileset_id is not None and self.tile_id is not None:
            screen.blit(
                    rm.get_tile_by_id(self.tileset_id, self.tile_id, GAME_CONFIGS['tile_configs']['zoom_levels'][-1]), (
                        self.x,
                        self.y,
                        )
                    )
