import pygame
import sys
from pygame.locals import *

from src.rlengine.config.system import GAME_CONFIGS
from src.rlengine.config.constants import *

from .mapstate import MapState
from src.rlengine.renderers import EntityRenderer
from src.rlengine.game.entities import EntityManager


class EntityMapState(MapState):
    def __init__(self, game, defaultmap):
        MapState.__init__(self, game, defaultmap)
        self.entity_renderer = EntityRenderer(game.rm)
        self.em = EntityManager()
        # TODO use self.entity_manager / self.em

    def _step_entities(self):
        # TODO clear out active=False entities from em
        for entity in self.em.get_ordered_step_entities():
            if entity.is_active:
                (did_move, next_x, next_y) = entity.calculate_step()
                if did_move:

                    if entity.ignore_walls:
                        walls_hit = []
                    else:
                        walls_hit = self.can_entity_move(next_x, next_y, entity.w, entity.h)                        
                                        
                    # free to move - no wall
                    if (len(walls_hit) == 0):
                        new_x = next_x
                        new_y = next_y

                    # hit wall
                    else:
                        # TODO CCD if direction > tile size then check for hits in between
                        new_x, new_y = entity.get_xy()
                        if abs(entity.ddx) + abs(entity.ddy) > 0:
                            total_dd = abs(entity.ddx) + abs(entity.ddy)
                            ddx_incr_test = entity.ddx / total_dd
                            ddy_incr_test = entity.ddy / total_dd

                            # TODO don't have infinite loop here
                            # get as close as you can to wall
                            while True:
                                walls_hit = self.can_entity_move(
                                    new_x + ddx_incr_test,
                                    new_y + ddy_incr_test,
                                    entity.w,
                                    entity.h
                                )
                                if len(walls_hit) > 0:
                                    break
                                else:
                                    new_x += ddx_incr_test
                                    new_y += ddy_incr_test

                        # TODO sometimes entities need to clear ddx/ddy after hit
                        entity.hit_wall(walls_hit)
                else:
                    new_x, new_y = entity.get_xy()

                entity.step(new_x, new_y)
                # TODO check entity-to-entity collision detection
                # TODO general way determine which types of objects should check collisions with each other?
                # entity groups? each group supplies a group type to check collisions against and a function to call when collision happens?
                # TODO CCD
                # TODO objects greater w+h than 1 tile

            self.em.step_collisions()

    def _draw_entities(self):
        for entity in self.em.get_ordered_draw_entities():
            if entity.is_visible and entity.is_active:
                self.entity_renderer.draw_entity(
                    self.screen,
                    entity,
                    self.camera_tile_x,
                    self.camera_tile_y,
                    self.zoom_level
                )

    def can_entity_move(self, x, y, w, h):
        touching_tiles = [
            self.get_tile_at_coords(x+(w/2), y),
            self.get_tile_at_coords(x+w-1, y+(h/2)),
            self.get_tile_at_coords(x+(w/2), y+h-1),
            self.get_tile_at_coords(x, y+(h/2))
        ]

        wall_hit_directions = []

        for index, touching_tile in enumerate(touching_tiles):
            if not touching_tile.is_walkable:
                wall_hit_directions.append(index)

        return wall_hit_directions

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
