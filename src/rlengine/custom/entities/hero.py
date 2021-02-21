import math
import pygame
import src.rlengine.utils.algos.rl_math as rl_math
from src.rlengine.game.entities import AnimatedMapFloatEntity
from src.rlengine.config.constants import *

# TODO in animation DATA file
ANIMATION_FRAMES = [
    [
        (0, 1, 5),
        (1, 1, 5),
        (2, 1, 5),
        (3, 1, 5),
        (4, 1, 5),
        (5, 1, 5),
        (6, 1, 5),
        (7, 1, 5),
        (8, 1, 5),
        (9, 1, 5),
    ],
    [
        (0, 2, 5),
        (1, 2, 5),
        (2, 2, 5),
        (3, 2, 5),
        (4, 2, 5),
        (5, 2, 5),
        (6, 2, 5),
        (7, 2, 5),
        (8, 2, 5),
        (9, 2, 5),
    ],
    [
        (0, 3, 5),
        (1, 3, 5),
        (2, 3, 5),
        (3, 3, 5),
        (4, 3, 5),
        (5, 3, 5),
        (6, 3, 5),
        (7, 3, 5),
        (8, 3, 5),
        (9, 3, 5),
    ],
]


class Hero(AnimatedMapFloatEntity):
    def __init__(self, cur_map, x, y):
        AnimatedMapFloatEntity.__init__(self, 0, cur_map, x, y, ANIMATION_FRAMES, {})

        self.first_launch_speed = 8
        self.second_launch_speed = 14

        self.is_first_launched = False
        self.is_second_launched = False
        self.just_hit_wall = False
        self.just_launched = False
        self.large_wall_force = False
        self.on_wall = True

        self.w = 28
        self.h = 28

        self.tile_id = 1
        self.tileset_id = 1

        self.launch_coord_x = 0
        self.launch_coord_y = 0

        self.switch_animation_state(2)

    def get_sprite_draw_offset_xy(self):
        return (-4, -18)

    def get_sprites_to_draw(self):
        return [self._generate_base_tile()]

    def step(self, next_x, next_y):
        super().step(next_x, next_y)

    def hit_wall(self, walls_hit):
        if not self.on_wall:
            self.switch_animation_state(1, 0)
            if self.is_second_launched:
                self.large_wall_force = True
            self.is_first_launched = False
            self.is_second_launched = False
            self.just_hit_wall = True
            self.on_wall = True

    def get_launch_coords(self):
        return (self.launch_coord_x, self.launch_coord_y)

    def action_launch(self, dest_x, dest_y):
        if not self.is_first_launched:
            self.switch_animation_state(2, None, 'freeze')
            x, y = self.get_center_point()
            self.launch_coord_x = x
            self.launch_coord_y = y
            self._launch(dest_x, dest_y, self.first_launch_speed)
            self.just_launched = True
            self.is_first_launched = True
        else:
            if not self.is_second_launched:
                self._launch(dest_x, dest_y, self.second_launch_speed)
                self.is_second_launched = True

    def _launch(self, dest_x, dest_y, speed):
        self.on_wall = False
        orig_x, orig_y = self.get_center_point()

        nx, ny = rl_math.get_normalized_vector(orig_x, orig_y, dest_x, dest_y)

        self.set_ddx(nx * speed)
        self.set_ddy(ny * speed)

