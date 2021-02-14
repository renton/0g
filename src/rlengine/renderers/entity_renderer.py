import pygame
from src.rlengine.config import GAME_CONFIGS, SYS_CONFIGS


class EntityRenderer():
    def __init__(self):
        self.block_mode = True

    # TODO function to resolve camera shit so we don't have to think about it
    # TODO only draw entities in frame
    def draw_entity(self, screen, sprites_to_draw, camera_x, camera_y, x, y, w, h, zoom_level):

        for sprite in sprites_to_draw:
            ex = (x) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
            ey = (y) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
            camera_x = camera_x * self.get_zoomed_tile_size(zoom_level)
            camera_y = camera_y * self.get_zoomed_tile_size(zoom_level)
            print('entity: ', x, y)
            print('camera: ', camera_x, camera_y)
            print('ex/ey: ', ex, ey)
            if self.block_mode:
                pygame.draw.rect(
                    screen,
                    (200, 30, 30),
                    (
                        ex - camera_x,
                        ey - camera_y,
                        w * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
                        h * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
                    ),
                    0
                )

    def get_zoomed_tile_size(self, zoom_level):
        return (
            GAME_CONFIGS['tile_configs']['tile_size'] * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
        )
