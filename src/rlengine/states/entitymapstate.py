import pygame
import sys
from pygame.locals import *

from src.rlengine.config.system import GAME_CONFIGS

from .mapstate import MapState
from src.rlengine.renderers import EntityRenderer


class EntityMapState(MapState):
    def __init__(self, game, defaultmap):
        MapState.__init__(self, game, defaultmap)
        self.entity_renderer = EntityRenderer()
        self.entities = []

    def _step_entities(self):
        for entity in self.entities:
            (did_move, next_x, next_y) = entity.step()
            if did_move and self.can_entity_move(next_x, next_y, entity.w, entity.h):
                entity.set_xy(next_x, next_y)
            # TODO check entity-to-entity collision detection

    def _draw_entities(self):
        for entity in self.entities:
            ex, ey = entity.get_xy()
            self.entity_renderer.draw_entity(
                self.screen,
                entity.get_sprites_to_draw(),
                self.camera_tile_x,
                self.camera_tile_y,
                ex,
                ey,
                entity.w,
                entity.h,
                self.zoom_level
            )

    def can_entity_move(self, x, y, w, h):
        touching_tiles = [
            self.get_tile_at_coords(x, y),
            self.get_tile_at_coords(x+w-1, y),
            self.get_tile_at_coords(x, y+h-1),
            self.get_tile_at_coords(x+w-1, y+h-1)
        ]

        for touching_tile in touching_tiles:
            if not touching_tile.is_walkable:
                return False

        return True

    def get_tile_at_coords(self, x, y):
        tile_x = int(x / GAME_CONFIGS['tile_configs']['tile_size'])
        tile_y = int(y / GAME_CONFIGS['tile_configs']['tile_size'])
        return self.cur_map.tiles[tile_x][tile_y]

    def add_entity_to_map(self, entity):
        self.entities.append(entity)

    def step(self):
        self._step_entities()
        MapState.step(self)

    def run_mainloop(self):
        self._step()

    def draw(self):
        MapState.draw(self)
        self._draw_entities()
