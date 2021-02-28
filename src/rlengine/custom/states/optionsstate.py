import pygame

from src.rlengine.states import MenuState
from src.rlengine.config import EVENT_CUSTOM_SWITCH_STATE
from src.rlengine.widgets import ToggleOption

OPTIONS_MENU_DRAW_X = 50
OPTIONS_MENU_DRAW_X = 50


class OptionsState(MenuState):
    def __init__(self, game, back_state=None):
        MenuState.__init__(self, game, draw_x=OPTIONS_MENU_DRAW_X, draw_y=OPTIONS_MENU_DRAW_X)


        self.menu.add_option_item(ToggleOption(0, 0, 'Music', self.toggle_music))
        self.menu.add_option_item(ToggleOption(0, 0, 'Sound', self.toggle_sound))
        self.menu.add_menu_item('back', self.exec_back)
        self.menu.select(0)
        if back_state:
            self.back_state = back_state

    def toggle_music(self):
        self.game.am.mfx_enabled = not self.game.am.mfx_enabled

    def toggle_sound(self):
        self.game.am.sfx_enabled = not self.game.am.sfx_enabled

    def exec_back(self):
        if self.back_state:
            pygame.event.post(pygame.event.Event(EVENT_CUSTOM_SWITCH_STATE, loadstate=self.back_state))
