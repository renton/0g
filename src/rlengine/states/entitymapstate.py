import pygame
import sys
from pygame.locals import *

from .mapstate import MapState
from src.rlengine.renderers import EntityRenderer


class EntityMapState(MapState):
    def __init__(self, game, defaultmap):
        MapState.__init__(self, game, defaultmap)
        self.entity_renderer = EntityRenderer()
        self.entities = []

    def _step_entities(self):
        for entity in self.entities:
            entity.step()

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
