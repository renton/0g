import time, pygame
from src.rlengine.game.entities import Effect

SHOCKWAVE_SPEED = 26
SHOCKWAVE_LIFESPAN_SMALL = 12
SHOCKWAVE_LIFESPAN_LARGE = 18


class Shockwave(Effect):
    def __init__(self, cur_map, x, y, is_large=False):
        shockwave_lifespan = SHOCKWAVE_LIFESPAN_LARGE if is_large else SHOCKWAVE_LIFESPAN_SMALL
        Effect.__init__(self, 0, cur_map, x, y, shockwave_lifespan, {})

        self.block_colour = (120, 120, 120)
        self.w = 5
        self.h = 5
        self.ddx = 0
        self.ddy = 0
        self.is_large = is_large

    def step(self, next_x, next_y):
        Effect.step(self, next_x, next_y)
        
        self.x -= SHOCKWAVE_SPEED / 2
        self.y -= SHOCKWAVE_SPEED / 2
        self.w += SHOCKWAVE_SPEED
        self.h += SHOCKWAVE_SPEED
