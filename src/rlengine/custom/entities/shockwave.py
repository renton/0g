import time, pygame
from src.rlengine.game.entities import Effect

SHOCKWAVE_SPEED = 12
SHOCKWAVE_LIFESPAN_SMALL = 10
SHOCKWAVE_LIFESPAN_LARGE = 20


class Shockwave(Effect):
    def __init__(self, cur_map, x, y, is_large=False):
        shockwave_lifespan = SHOCKWAVE_LIFESPAN_LARGE if is_large else SHOCKWAVE_LIFESPAN_SMALL
        Effect.__init__(self, 0, cur_map, x, y, shockwave_lifespan, {})

        self.block_colour = (0, 0, 255)
        self.w = 5
        self.h = 5
        self.ddx = 0
        self.ddy = 0
        self.is_large = is_large

    def get_hitbox(self):
        x, y = self.get_xy()
        return pygame.Rect(x-(self.w/2), y-(self.h/2), self.w, self.h)

    def step(self, next_x, next_y):
        Effect.step(self, next_x, next_y)
        
        self.w += SHOCKWAVE_SPEED
        self.h += SHOCKWAVE_SPEED