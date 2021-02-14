import pygame
import sys
from pygame.locals import *

from .mapstate import MapState
from src.rlengine.renderers import EntityRenderer


class EntityMapState(MapState):
    def __init__(self, game, defaultmap):
        MapState.__init__(self, game, defaultmap)

        grid_entities = []
        float_entities = []
