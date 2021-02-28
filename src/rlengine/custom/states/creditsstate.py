import pygame

from src.rlengine.states import MenuState
from src.rlengine.config import EVENT_CUSTOM_SWITCH_STATE
from src.rlengine.widgets import LabelWidget

CREDITS_MENU_DRAW_X = 50
CREDITS_MENU_DRAW_Y = 800

CREDITS_TEXT_START_X = 50
CREDITS_TEXT_START_Y = 40
CREDITS_SECTION_MARGIN = 110
CREDITS_SECTION_LINE_HEIGHT = 60

LABEL_X_OFFSET = 40


class CreditsState(MenuState):
    def __init__(self, game, back_state=None):
        MenuState.__init__(self, game, CREDITS_MENU_DRAW_X, CREDITS_MENU_DRAW_Y)

        y_cursor = CREDITS_TEXT_START_Y
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X, y_cursor, 'Programming:'))
        y_cursor += CREDITS_SECTION_LINE_HEIGHT
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X + LABEL_X_OFFSET, y_cursor, 'rentonl'))

        y_cursor += CREDITS_SECTION_MARGIN
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X, y_cursor, 'Graphics+Animation:'))
        y_cursor += CREDITS_SECTION_LINE_HEIGHT
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X + LABEL_X_OFFSET , y_cursor, 'Finch'))

        y_cursor += CREDITS_SECTION_MARGIN
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X, y_cursor, 'Game Design:'))
        y_cursor += CREDITS_SECTION_LINE_HEIGHT
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X + LABEL_X_OFFSET, y_cursor, 'rentonl'))
        y_cursor += CREDITS_SECTION_LINE_HEIGHT
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X + LABEL_X_OFFSET, y_cursor, 'Finch'))

        y_cursor += CREDITS_SECTION_MARGIN
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X, y_cursor, 'Music:'))
        y_cursor += CREDITS_SECTION_LINE_HEIGHT
        self.add_widget(LabelWidget(CREDITS_TEXT_START_X + LABEL_X_OFFSET, y_cursor, 'rentonl'))

        self.menu.add_menu_item('back', self.exec_back)
        self.menu.select(0)
        if back_state:
            self.back_state = back_state

    def exec_back(self):
        if self.back_state:
            pygame.event.post(pygame.event.Event(EVENT_CUSTOM_SWITCH_STATE, loadstate=self.back_state))
