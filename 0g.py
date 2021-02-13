import sys
import pygame
from pygame.locals import *
from src.rlengine.game import Game
from src.rlengine.config import SYS_CONFIGS, RL_CONFIGS

pygame.init()

game = Game(
    SYS_CONFIGS,
    RL_CONFIGS,
)
game.mainloop()
