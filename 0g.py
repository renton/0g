import sys
import pygame
from pygame.locals import *
from src.rlengine.game import Game
from src.rlengine.config import SYS_CONFIG

pygame.init()

game = Game(SYS_CONFIG)
game.mainloop()
