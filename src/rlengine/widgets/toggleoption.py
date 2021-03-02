from src.rlengine.widgets import MenuItemWidget
from src.rlengine.config import GAME_CONFIGS, WIDGET_CONFIGS

STATE_ON_TEXT = 'On'
STATE_OFF_TEXT = 'Off'

HIGHLIGHT_COLOUR = (0, 100, 0)

TOGGLE_MARGIN = 400
TOGGLE_SEPARATOR_WIDTH = 200


class ToggleOption(MenuItemWidget):
    def __init__(self, x, y, label, select_event=None, hover_event=None, label_fn=None, default_state=True):
        MenuItemWidget.__init__(self, x, y, label, lambda: self.toggle(select_event))
        self.toggle_state = default_state

    def toggle(self, fn):
        self.toggle_state = not self.toggle_state
        fn()

    def draw(self, screen, rm):
        MenuItemWidget.draw(self, screen, rm)

        highlight = HIGHLIGHT_COLOUR if self.toggle_state else None
        text_on = rm.get_font(WIDGET_CONFIGS['widget_default_menu_font']).render(STATE_ON_TEXT, 1, WIDGET_CONFIGS['widget_default_menu_font_colour'], highlight)

        screen.blit(
            text_on,
            (
                self.x + TOGGLE_MARGIN,
                self.y,
            )
        )

        highlight = HIGHLIGHT_COLOUR if not self.toggle_state else None
        text_off = rm.get_font(WIDGET_CONFIGS['widget_default_menu_font']).render(STATE_OFF_TEXT, 1, WIDGET_CONFIGS['widget_default_menu_font_colour'], highlight)

        screen.blit(
            text_off,
            (
                self.x + TOGGLE_MARGIN + TOGGLE_SEPARATOR_WIDTH,
                self.y,
            )
        )
