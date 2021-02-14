import pygame
import sys
from pygame.locals import *

from random import randrange, choice, randint

from src.rlengine.states import EntityMapState
from src.rlengine.config import GAME_CONFIGS
from src.rlengine.renderers import MapRenderer


class ZeroGMapState(EntityMapState):
    def __init__(self, game, defaultmap):
        EntityMapState.__init__(self, game, defaultmap)