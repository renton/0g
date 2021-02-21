import pygame
from src.rlengine.config import GAME_CONFIGS, SYS_CONFIGS


# TODO debug mode
class EntityRenderer():
    def __init__(self, rm):
        self.debug_mode = False
        self.draw_hitboxes = False
        self.rm = rm

    def draw_entity_hitbox(self, screen, entity, camera_x, camera_y, zoom_level):
        hitbox = entity.get_hitbox()

        ex = (hitbox.x) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
        ey = (hitbox.y) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
        camera_x = camera_x * self.get_zoomed_tile_size(zoom_level)
        camera_y = camera_y * self.get_zoomed_tile_size(zoom_level)

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (
                ex - camera_x,
                ey - camera_y,
                hitbox.w * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
                hitbox.h * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
            ),
            0
        )

    # TODO function to resolve camera shit so we don't have to think about it
    # TODO only draw entities in frame
    # TODO just pass in entity object if gonna call it draw_entity
    def draw_entity(self, screen, entity, camera_x, camera_y, zoom_level):

        block_colour = entity.get_block_colour()
        sprites_to_draw = entity.get_sprites_to_draw()
        x, y = entity.get_xy()
        x_offset, y_offset = entity.get_sprite_draw_offset_xy()
        x += x_offset
        y += y_offset
        h = entity.h
        w = entity.w

        for sprite in sprites_to_draw:
            ex = (x) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
            ey = (y) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
            ecamera_x = camera_x * self.get_zoomed_tile_size(zoom_level)
            ecamera_y = camera_y * self.get_zoomed_tile_size(zoom_level)

            if self.debug_mode:
                pygame.draw.rect(
                    screen,
                    block_colour,
                    (
                        ex - ecamera_x,
                        ey - ecamera_y,
                        w * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
                        h * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
                    ),
                    0
                )
            else:
                if sprite[0] == 'block':
                    pygame.draw.rect(
                        screen,
                        block_colour,
                        (
                            ex - ecamera_x,
                            ey - ecamera_y,
                            w * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
                            h * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
                        ),
                        0
                    )

                if sprite[0] == 'circle':
                    ex, ey = entity.get_center_point()
                    ex = (x+(h/2)) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
                    ey = (y+(w/2)) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
                    pygame.draw.circle(
                        screen,
                        block_colour,
                        (
                            ex - ecamera_x,
                            ey - ecamera_y,
                        ),
                        (w/2) * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level],
                        2
                    )

                if sprite[0] == 'sprite':
                    tile_id = sprite[1]
                    tileset_id = sprite[2]
                    screen.blit(
                        self.rm.get_tile_by_id(
                            tileset_id,
                            tile_id,
                            GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
                        ),
                        (
                            ex - ecamera_x,
                            ey - ecamera_y,
                        )
                    )

        if self.draw_hitboxes:
            self.draw_entity_hitbox(screen, entity, camera_x, camera_y, zoom_level)

    def get_zoomed_tile_size(self, zoom_level):
        return (
            GAME_CONFIGS['tile_configs']['tile_size'] * GAME_CONFIGS['tile_configs']['zoom_levels'][zoom_level]
        )
