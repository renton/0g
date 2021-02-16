import pygame

from src.rlengine.states import MenuState

from src.rlengine.config import EVENT_CUSTOM_CREATE_STATE
from src.data import TILE_DATA, MAP_DATA
from src.rlengine.game.map import Map, Tile

from .zerog_mapstate import ZeroGMapState

MAIN_MENU_DRAW_X = 50
MAIN_MENU_DRAW_Y = 50


class MainMenuState(MenuState):
    def __init__(self, game):
        MenuState.__init__(self, game, draw_x=MAIN_MENU_DRAW_X, draw_y=MAIN_MENU_DRAW_Y)

        self.menu.add_menu_item('start', self.exec_new_game)
        self.menu.add_menu_item('options')
        self.menu.add_menu_item('credits')
        self.menu.add_menu_item('exit', self.exec_exit_game)
        self.menu.select(0)

    def exec_new_game(self):
        # TODO custom should be easier to use
        new_map = Map(TILE_DATA, Tile, gen_sample=False, map_data=MAP_DATA[0])
        pygame.event.post(pygame.event.Event(EVENT_CUSTOM_CREATE_STATE, createstate=lambda game: ZeroGMapState(game, new_map)))

    def exec_exit_game(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
