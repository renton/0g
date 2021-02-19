import pygame
import sys
from pygame.locals import *

from src.rlengine.config.system import GAME_CONFIGS

from .mapstate import MapState
from src.rlengine.renderers import EntityRenderer
from src.rlengine.game.entities import EntityManager


class EntityMapState(MapState):
    def __init__(self, game, defaultmap):
        MapState.__init__(self, game, defaultmap)
        self.entity_renderer = EntityRenderer()
        self.em = EntityManager()
        # TODO use self.entity_manager / self.em

    def _step_entities(self):
        for entity in self.em.get_ordered_draw_entities():
            (did_move, next_x, next_y) = entity.calculate_step()
            if did_move:
                if self.can_entity_move(next_x, next_y, entity.w, entity.h):
                    new_x = next_x
                    new_y = next_y
                else:
                    # CCD TODO
                    # TODO if direction > tile size then check for hits in between
                    # TODO hit_wall should send the direction hit
                    # if entity.ddx + entity.ddy > 0:
                    #     ddx_test = entity.ddx / (entity.ddx + entity.ddy)
                    #     ddy_test = entity.ddy / (entity.ddx + entity.ddy)
                    #     x_test, y_text = entity.get_xy()


                    # TODO make x,y equal vectors of length 1 then check each step
                    # TODO get as close as you can for CCD
                    new_x, new_y = entity.get_xy()
                    # TODO bool for top,left,down right?
                    entity.hit_wall()

                entity.step(new_x, new_y)
            # TODO check entity-to-entity collision detection
            # TODO general way determine which types of objects should check collisions with each other?
            # entity groups? each group supplies a group type to check collisions against and a function to call when collision happens?
            # TODO CCD
            # TODO objects greater w+h than 1 tile

        self.em.step_collisions()

    def _draw_entities(self):
        for entity in self.em.get_ordered_draw_entities():
            ex, ey = entity.get_xy()
            self.entity_renderer.draw_entity(
                self.screen,
                entity.block_colour,
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

    def add_entity_to_map(self, entity, group_id):
        self.em.add_entity_to_group(entity, group_id)

    def step(self):
        self._step_entities()
        MapState.step(self)

    def run_mainloop(self):
        self._step()

    def draw(self):
        MapState.draw(self)
        self._draw_entities()
