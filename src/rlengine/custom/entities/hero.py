import math
import pygame
import src.rlengine.utils.algos.rl_math as rl_math
from src.rlengine.game.entities import AnimatedMapFloatEntity
from src.rlengine.config.constants import *
from src.rlengine.game.entities.entity_states import EMapStatefulMixin, EMapState
from src.rlengine.config.constants import *


STATE_START = 0
STATE_JUMP1 = 1
STATE_JUMP2 = 2
STATE_LAND = 3
STATE_DIE = 4

FIRST_LAUNCH_SPEED = 8
SECOND_LAUNCH_SPEED = 14


class HeroStartState(EMapState):
    def __init__(self):
        super().__init__()

    def enter_estate(self, e):
        e.switch_animation_state(0)

    def get_estate_sprite_draw_offset(self, e):
        return (-4, -18)


class HeroJump1State(EMapState):
    def __init__(self):
        super().__init__()
        self.angle = 0

    def enter_estate(self, e, dest_x, dest_y):
        e.switch_animation_state(2, None, 'freeze')
        x, y = e.get_center_point()
        e.launch_coord_x = x
        e.launch_coord_y = y
        self.angle = rl_math.get_angle_between_line_and_x_axis(x, y, dest_x, dest_y)
        e.launch(dest_x, dest_y, FIRST_LAUNCH_SPEED)

    def get_estate_sprite_draw_offset(self, e):
        return (-8, -18)

    def get_estate_sprite_draw_transform(self, e, sprite):
        print(self.angle)
        return pygame.transform.rotate(sprite, (self.angle+90) * -1)


class HeroJump2State(EMapState):
    def __init__(self):
        super().__init__()
        self.angle = 0

    def enter_estate(self, e, dest_x, dest_y):
        x, y = e.get_xy()
        self.angle = rl_math.get_angle_between_line_and_x_axis(x, y, dest_x, dest_y)
        e.launch(dest_x, dest_y, SECOND_LAUNCH_SPEED)

    def get_estate_sprite_draw_offset(self, e):
        return (-4, -18)

    def get_estate_sprite_draw_transform(self, e, sprite):
        return pygame.transform.rotate(sprite, (self.angle+90) * -1)


class HeroLandState(EMapState):
    def __init__(self):
        super().__init__()
        self.wall_dir = RL_BOTTOM

    def enter_estate(self, e, prev_state_id, wall_dir):
        e.switch_animation_state(1, 0)
        self.wall_dir = wall_dir

    def get_estate_sprite_draw_offset(self, e):
        if e.get_current_a_state_id() == 1:
            return (-8, -18)
        elif e.get_current_a_state_id() == 0:
            return (-4, -18)

    def get_estate_sprite_draw_transform(self, e, sprite):
        if e.get_current_a_state_id() == 1:
            if self.wall_dir == RL_TOP:
                angle = 0
            elif self.wall_dir == RL_BOTTOM:
                angle = -180
            elif self.wall_dir == RL_LEFT:
                angle = -270
            elif self.wall_dir == RL_RIGHT:
                angle = -90
        elif e.get_current_a_state_id() == 0:
            if self.wall_dir == RL_TOP:
                angle = -180
            elif self.wall_dir == RL_BOTTOM:
                angle = 0
            elif self.wall_dir == RL_LEFT:
                angle = -90
            elif self.wall_dir == RL_RIGHT:
                angle = -270
        return pygame.transform.rotate(sprite, angle)


class HeroDieState(EMapState):
    def __init__(self):
        super().__init__()

    def enter_estate(self, e):
        e.switch_animation_state(3)
        e.ddx = 0
        e.ddy = 0

    def get_estate_sprite_draw_offset(self, e):
        return (-4, -18)

    def get_estate_sprite_draw_transform(self, e, sprite):
        return pygame.transform.scale(sprite, (400, 400))


# TODO in animation DATA file
# TODO animation constants
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
        (0, 3, 2),
        (1, 3, 2),
        (2, 3, 2),
        (3, 3, 2),
        (4, 3, 2),
        (5, 3, 2),
        (6, 3, 2),
        (7, 3, 2),
        (8, 3, 5),
        (9, 3, 5),
    ],
    [
        (2, 2, 3),
        (3, 2, 3),
        (4, 2, 3),
        (5, 2, 3),
    ],
]


class Hero(EMapStatefulMixin, AnimatedMapFloatEntity):
    def __init__(self, cur_map, x, y):
        # TODO is there a better way to do mixin inits??
        AnimatedMapFloatEntity.__init__(self, 0, cur_map, x, y, ANIMATION_FRAMES, {})
        EMapStatefulMixin.__init__(self)

        self.add_estate(STATE_START, HeroStartState())
        self.add_estate(STATE_JUMP1, HeroJump1State())
        self.add_estate(STATE_JUMP2, HeroJump2State())
        self.add_estate(STATE_LAND, HeroLandState())
        self.add_estate(STATE_DIE, HeroDieState())

        self.w = 28
        self.h = 28

        self.tile_id = 1
        self.tileset_id = 1

        self.launch_coord_x = 0
        self.launch_coord_y = 0

        self.set_estate(STATE_START)

    def take_hit(self):
        if self.get_cur_estate_id() != STATE_DIE:
            self.set_estate(STATE_DIE)

    def step(self, next_x, next_y):
        super().step(next_x, next_y)

    def hit_wall(self, walls_hit):
        if self.get_cur_estate_id() not in [STATE_START, STATE_LAND]:
            self.set_estate(STATE_LAND, self.get_cur_estate_id(), walls_hit[0])

    def get_launch_coords(self):
        return (self.launch_coord_x, self.launch_coord_y)

    def action_launch(self, dest_x, dest_y):
        if self.get_cur_estate != STATE_DIE:
            if self.get_cur_estate_id() in [STATE_START, STATE_LAND]:
                self.set_estate(STATE_JUMP1, dest_x, dest_y)
            elif self.get_cur_estate_id() == STATE_JUMP1:
                self.set_estate(STATE_JUMP2, dest_x, dest_y)

    def launch(self, dest_x, dest_y, speed):
        orig_x, orig_y = self.get_center_point()

        nx, ny = rl_math.get_normalized_vector(orig_x, orig_y, dest_x, dest_y)

        self.set_ddx(nx * speed)
        self.set_ddy(ny * speed)

