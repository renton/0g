import pygame
import sys
from pygame.locals import *

from random import randrange, choice, randint

from src.rlengine.states import State
from src.rlengine.config import GAME_CONFIGS
from src.rlengine.renderers import MapRenderer


# TODO heavy refactoring. this should never be instanced. entity drawing should have it's own renderer. the instanced subclass can define that
# TODO entities on map is an abstraction up


class MapState(State):
    def __init__(self, game, defaultmap):
        State.__init__(self, game)

        self._set_camera(0, 0)
        self.zoom_level = GAME_CONFIGS['tile_configs']['zoom_levels'][0]
        self.fixed_camera = True
        self.camera_target = None
        self._set_map_renderer()
        self.set_map(defaultmap)

        # self.entity_renderer = EntityRenderer(self.screen, self.rm)

    def _set_map_renderer(self):
        self.map_renderer = MapRenderer(self.game.rm)

    def set_map(self, newmap):
        self.cur_map = newmap

    def step(self):
        # self._step_entities()
        State.step(self)
        self._force_draw()

    # map state only draws implicitly
    def run_mainloop(self):
        self._step()

    # def _step_entities(self):
    #     for entity in self.entities:
    #         entity.step(self.cur_map)

    def draw(self):
        State.draw(self)
        self._draw_map()

    def _draw_map(self):
        self.map_renderer.draw_map(
            self.screen,
            self.cur_map,
            self.camera_tile_x,
            self.camera_tile_y,
            self.zoom_level
        )

    # def set_follow_camera(self, e):
    #     self.fixed_camera = False
    #     self.camera_target = e

    def _set_camera(self, x, y):
        self.camera_tile_x, self.camera_tile_y = (x, y)

    def input(self, im):
        # TODO why is this needed?
        keystate = pygame.key.get_pressed()

        # TODO camera should be able to pan to blackness at any zoom level
        if self.im.is_key_event(KEYDOWN, K_w) or keystate[K_w]:
            self._set_camera(self.camera_tile_x, self.camera_tile_y - 1)
            self._force_draw()
        if self.im.is_key_event(KEYDOWN, K_d) or keystate[K_d]:
            self._set_camera(self.camera_tile_x + 1, self.camera_tile_y)
            self._force_draw()
        if self.im.is_key_event(KEYDOWN, K_s) or keystate[K_s]:
            self._set_camera(self.camera_tile_x, self.camera_tile_y + 1)
            self._force_draw()
        if self.im.is_key_event(KEYDOWN, K_a) or keystate[K_a]:
            self._set_camera(self.camera_tile_x - 1, self.camera_tile_y)
            self._force_draw()

        # if self.im.is_key_event(KEYDOWN, K_UP) or keystate[K_UP]:
        #     self.p1.e.delta_dir = 0
        # if self.im.is_key_event(KEYDOWN, K_DOWN) or keystate[K_DOWN]:
        #     self.p1.e.delta_dir = 2
        # if self.im.is_key_event(KEYDOWN, K_LEFT) or keystate[K_LEFT]:
        #     self.p1.e.delta_dir = 3
        # if self.im.is_key_event(KEYDOWN, K_RIGHT) or keystate[K_RIGHT]:
        #     self.p1.e.delta_dir = 1

        # if self.im.is_key_event(KEYDOWN, K_v):
        #     self.fixed_camera = not self.fixed_camera
        #     self.log.add_log("camera: " + ("fixed" if self.fixed_camera else "follow")) 
        #     self._force_draw()

        if self.im.is_key_event(KEYDOWN, K_z):
            if self.zoom_level > GAME_CONFIGS['tile_configs']['min_zoom']:
                self.zoom_level -= 1
                self._force_draw()
        if self.im.is_key_event(KEYDOWN, K_x):
            if self.zoom_level < GAME_CONFIGS['tile_configs']['max_zoom']:
                self.zoom_level += 1
                self._force_draw()
        # if self.im.is_key_event(KEYDOWN, K_c):
        #     self.p1.bind_entity(self.test1)
        #     self.fixed_camera = False
        #     self.set_camera_to_entity(self.p1.e)
        #     self._force_draw()
        # if self.im.is_key_event(KEYDOWN, K_n):
        #     self.p1.unbind_entity()
        #     self._force_draw()
        # if self.im.is_key_event(KEYDOWN, K_p):
        #     self.p1.e.increment_length(1)
        #     self._force_draw()
        # if self.im.is_key_event(KEYDOWN, K_o):
        #     self.p1.e.increment_length(-1)
        #     self._force_draw()
        '''
        if self.im.is_key_event(KEYDOWN, K_g):
            # successfully picked up
            (pickedup, dropped) = self.p1.e.pickup(self.cur_map.tiles[self.p1.e.x][self.p1.e.y])
            for item in pickedup: 
                self.remove_entity_from_map(item)
            for item in dropped:
                self.add_entity_to_map(item, self.p1.e.x, self.p1.e.y)
            self._force_draw()
        '''
        # if self.im.is_key_event(KEYDOWN, K_e):
        #     self.toggle_expanded_logs()
        #     self._force_draw()

        '''
        if self.im.is_key_event(KEYDOWN, K_i):
            if self.p1.e:
                self.i_state.set_entity(self.p1.e)
                pygame.event.post(pygame.event.Event(CONFIG['EVENT_CUSTOM_SWITCH_STATE'], loadstate = self.i_state))
        if self.im.is_key_event(KEYDOWN, K_g):
            if self.p1.e:
                items = self.p1.e.pickup_all(self.get_player_current_tile())
                for item in items:
                    self.remove_entity_from_map(item)
                self._force_draw()
        '''

        State.input(self, self.im)

    # def get_player_current_tile(self):
    #     if self.p1.e and self.cur_map:
    #         return self.cur_map.tiles[self.p1.e.x][self.p1.e.y]

    # def add_entity_to_map(self, e, x=-1, y=-1):
    #     self.entities.append(e)

    #     if x == -1 and y == -1:
    #         if e.x:
    #             x = e.x
    #         if e.y:
    #             y = e.y

    #     e.add_to_map(x, y, self.cur_map)

    # TODO entities should be a key=>value for fast removals (and order drawing data)
    # def remove_entity_from_map(self, e):
    #     e.remove_from_map()
    #     self.entities.remove(e)

    # def set_camera_to_entity(self, e):
    #     if e and e.alive:
    #         self._set_camera(
    #                 e.x - ((CONFIG['map_window_size_x'] // CONFIG['zoom_levels'][self.zoom_level]) // 2),
    #                 e.y - ((CONFIG['map_window_size_y'] // CONFIG['zoom_levels'][self.zoom_level]) // 2)
    #                 )
