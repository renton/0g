import pygame
import sys
from pygame.locals import *

from random import randrange, choice, randint

import src.rlengine.utils.algos.rl_math as rl_math
from src.rlengine.states import EntityMapState
from src.rlengine.config import GAME_CONFIGS
from src.rlengine.renderers import MapRenderer
from src.rlengine.custom.entities import Hero, Projectile, Shockwave
from src.rlengine.custom.entities.hero import STATE_START, STATE_LAND, STATE_JUMP1, STATE_JUMP2

START_CAMERA_X = -6
START_CAMERA_Y = -4

ENTITY_GROUP_HERO = 'HERO'
ENTITY_GROUP_PROJECTILES = 'PROJS'
ENTITY_GROUP_EFFECTS = 'EFFECTS'


def hero_proj_collision(hero, proj):
    if not proj.fading_in:
        proj.is_colliding = True
        hero.take_hit()


def shockwave_proj_collision(wave, proj):
    if not proj.fading_in:
        proj.is_colliding = True
        orig_x, orig_y = wave.get_center_point()
        dest_x, dest_y = proj.get_center_point()
        nx, ny = rl_math.get_normalized_vector(orig_x, orig_y, dest_x, dest_y)
        proj.ddx = nx * 8
        proj.ddy = ny * 8


# TODO step override to plant projectiles
class ZeroGMapState(EntityMapState):
    def __init__(self, game, defaultmap):
        EntityMapState.__init__(self, game, defaultmap)
        self.em.add_entity_group(ENTITY_GROUP_HERO)
        self.em.add_entity_group(ENTITY_GROUP_PROJECTILES)
        self.em.add_entity_group(ENTITY_GROUP_EFFECTS)
        self.em.add_entity_collision_group(
            ENTITY_GROUP_HERO,
            [ENTITY_GROUP_PROJECTILES],
            hero_proj_collision,
        )

        self.em.add_entity_collision_group(
            ENTITY_GROUP_EFFECTS,
            [ENTITY_GROUP_PROJECTILES],
            shockwave_proj_collision,
        )

        self._set_camera(START_CAMERA_X, START_CAMERA_Y)
        self.game.bind_player_entity(Hero(defaultmap, 40, 40))
        self.player = self.game.player1
        self.score = 0

        self.add_entity_to_map(self.player.e, ENTITY_GROUP_HERO)

    def _step_entities(self):
        EntityMapState._step_entities(self)
        if self.player.e.just_entered_state_id(STATE_LAND):
            self.score += 1
            print('score: ', self.score)
            x, y = self.player.e.get_xy()
            self.add_entity_to_map(
                Shockwave(
                    self.cur_map,
                    x,
                    y,
                    self.player.e.get_prev_estate_id() == STATE_JUMP2),
                ENTITY_GROUP_EFFECTS
            )

        if self.player.e.just_entered_state_id(STATE_JUMP1):
            x, y = self.player.e.get_launch_coords()
            self.add_entity_to_map(Projectile(self.cur_map, x, y), ENTITY_GROUP_PROJECTILES)

    def input(self, im):
        if self.im.is_key_event(KEYDOWN, K_UP):
            # self.player.e.move_tile_y = -1
            self.player.e.set_ddy(-0.6)
            self.player.e.set_ddx(0)
        if self.im.is_key_event(KEYDOWN, K_DOWN):
            # self.player.e.move_tile_y = 1
            self.player.e.set_ddy(0.6)
            self.player.e.set_ddx(0)
        if self.im.is_key_event(KEYDOWN, K_LEFT):
            # self.player.e.move_tile_x = -1
            self.player.e.set_ddx(-0.6)
            self.player.e.set_ddy(0)
        if self.im.is_key_event(KEYDOWN, K_RIGHT):
            # self.player.e.move_tile_x = 1
            self.player.e.set_ddx(0.6)
            self.player.e.set_ddy(0)

        if self.im.is_key_event(KEYDOWN, K_o):
            print(self.em.entity_collision_groups)
            print(self.em.entity_groups)
            print(self.em.get_ordered_draw_entities())
            print(self.em.get_ordered_step_entities())

        if self.im.is_key_event(KEYDOWN, K_p):
            mouse_map_x, mouse_map_y = self.mouse_to_map_coords()
            self.add_entity_to_map(Projectile(self.cur_map, mouse_map_x, mouse_map_y), ENTITY_GROUP_PROJECTILES)

        if self.im.is_key_event(KEYDOWN, K_q):
            self.entity_renderer.draw_hitboxes = not self.entity_renderer.draw_hitboxes

        if self.im.is_lmouse_pressed():
            self.player.e.action_launch(self.game.mouse_map_x, self.game.mouse_map_y)

        if self.im.is_cmouse_pressed():
            self.player.e.action_launch(self.game.mouse_map_x, self.game.mouse_map_y)

        EntityMapState.input(self, im)

