import pygame
from src.rlengine.config import GAME_CONFIGS, SYS_CONFIGS


class MapRenderer():
    def __init__(self, rm):
        self.block_mode = True
        self.rm = rm

    def _draw_tile(self, screen, tile, x, y, zoom_level):
        ex = x * self.get_zoomed_tile_size(zoom_level)
        ey = y * self.get_zoomed_tile_size(zoom_level)
        if self.block_mode:
            if tile.block_colour is not None:
                pygame.draw.rect(
                    screen,
                    tile.block_colour,
                    (
                        ex,
                        ey,
                        self.get_zoomed_tile_size(zoom_level),
                        self.get_zoomed_tile_size(zoom_level)
                    ),
                    0
                )
        else:
            screen.blit(
                self.rm.get_tile_by_id(
                    tile.tileset_id,
                    tile.tile_id,
                    GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
                ),
                (
                    ex,
                    ey,
                )
            )

    def draw_map(self, screen, cur_map, camera_tile_x, camera_tile_y, zoom_level):
        # draw map
        # TODO only need to draw what's in viewport (not the whole map_window)
        # if not self.fixed_camera:
        #     self.set_camera_to_entity(self.camera_target)

        # TODO entity renderers should be classes that can be swapped in and out and decoupled with the mapstate
        for x in range((GAME_CONFIGS['map_configs']['map_window_size_x'] // GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level])):
            for y in range((GAME_CONFIGS['map_configs']['map_window_size_y'] // GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level])):
                if ((camera_tile_x + x) >= 0) and ((camera_tile_y + y) >= 0):
                    if (((camera_tile_x + x) < len(cur_map.tiles)) and ((camera_tile_y + y) < len(cur_map.tiles[camera_tile_x + x]))):
                        tile = cur_map.tiles[camera_tile_x + x][camera_tile_y + y]
                        self._draw_tile(screen, tile, x, y, zoom_level)
                        # for _, e in tile.get_entities().items():
                        #     ex = (x) * self.get_zoomed_tile_size()
                        #     ey = (y) * self.get_zoomed_tile_size()

                        #     if e.cur_map:
                        #         # TODO we should just be able to say we want to draw the map and entities and not care about camera
                        #         # maybe draw map can handle everything? You are drawing tiles over the entitiy... you need
                        #         self.entity_renderer.draw_entity(
                        #                                         e.get_tiles_to_draw(),
                        #                                         ex,
                        #                                         ey,
                        #                                         self.zoom_level,
                        #         )

    def get_zoomed_tile_size(self, zoom_level):
        return (
            GAME_CONFIGS['tile_configs']['tile_size'] * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
        )
