import pygame
from src.rlengine.game.entities import MapFloatEntity
from src.rlengine.config.constants import *
from src.rlengine.game.entities.entity_states import EMapStatefulMixin, EMapState

STATE_FADING_IN = 0
STATE_NORMAL = 1
STATE_SPEEDING_UP = 2

FADE_IN_STEPS = 40
SPEED_UP_STEPS = 20


# TODO colour consts
class ProjFadeInState(EMapState):
    def __init__(self):
        super().__init__()

    def get_estate_block_colour(self, e):
        return (25, 25, 25)


class ProjNormalState(EMapState):
    def __init__(self):
        super().__init__()


class ProjSpeedingUpState(EMapState):
    def __init__(self):
        super().__init__()

    def get_estate_block_colour(self, e):
        return (255, 255, 255)


class Projectile(EMapStatefulMixin, MapFloatEntity):
    def __init__(self, cur_map, x, y):
        MapFloatEntity.__init__(self, 1, cur_map, x, y, {})
        EMapStatefulMixin.__init__(self)

        self.add_estate(STATE_FADING_IN, ProjFadeInState())
        self.add_estate(STATE_NORMAL, ProjNormalState())
        self.add_estate(STATE_SPEEDING_UP, ProjSpeedingUpState())

        self.x = x
        self.y = y
        self.w = 10
        self.h = 10
        self.ddx = 0
        self.ddy = 0
        self.block_colour = (255, 255, 20)
        self.is_colliding = False

        self.fading_in = True

        self.set_estate(STATE_FADING_IN)

    # TODO pass x and y offsets?
    def hit_wall(self, walls_hit):
        if RL_TOP in walls_hit or RL_BOTTOM in walls_hit:
            self.ddy = self.ddy * (-1)

        if RL_LEFT in walls_hit or RL_RIGHT in walls_hit:
            self.ddx = self.ddx * (-1)

    # TODO support for multiple primitives with different positions
    def get_sprites_to_draw(self):
        return [['circle']]

    def step(self, next_x, next_y):
        self.is_colliding = False
        if (
            (
                self.get_cur_estate_id() == STATE_FADING_IN and
                self.get_num_estate_steps() >= FADE_IN_STEPS
            ) or
            (
                self.get_cur_estate_id() == STATE_SPEEDING_UP and
                self.get_num_estate_steps() >= SPEED_UP_STEPS
            )
        ):
            self.set_estate(STATE_NORMAL)

        MapFloatEntity.step(self, next_x, next_y)

    def speed_up(self, new_ddx, new_ddy):       
        self.ddx = new_ddx
        self.ddy = new_ddy
        self.set_estate(STATE_SPEEDING_UP)
