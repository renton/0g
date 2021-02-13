import pygame
from pygame.locals import *

from config import CONFIG
from src.rlengine.states import State
from src.rlengine.widgets import MenuWidget

class MenuState(State):
    def __init__(self, game, draw_x = CONFIG['widget_default_menu_draw_x'], draw_y = CONFIG['widget_default_menu_draw_y']):
        State.__init__(self, game)
        self.menu = MenuWidget(draw_x, draw_y)
        self.add_widget(self.menu)

    def input(self, im):
        if self.im.is_key_event(KEYDOWN, K_w) or self.im.is_key_event(KEYDOWN, K_UP):
            self.menu.cycle_last()
            self._force_draw()
        if self.im.is_key_event(KEYDOWN, K_s) or self.im.is_key_event(KEYDOWN, K_DOWN):
            self.menu.cycle_next()
            self._force_draw()
        if self.im.is_key_event(KEYDOWN, K_RETURN) or self.im.is_key_event(KEYDOWN, K_KP_ENTER):
            if hasattr(self.menu.item_select_event(), '__call__'):
                self.menu.item_select_event()()
                self._force_draw()
