import pygame
from src.rlengine.widgets import MenuItemWidget
from src.rlengine.config import GAME_CONFIGS, WIDGET_CONFIGS

HIGHLIGHT_COLOUR = (0, 100, 0)

METER_MARGIN = 400
METER_HEIGHT = 50
METER_WIDTH = 400

DEFAULT_INCR_PERCENT = 10


# TODO decrease
class MeterOption(MenuItemWidget):
    def __init__(
        self,
        x,
        y,
        label,
        min=0.0,
        max=1.0,
        select_event=None,
        incr_perc=DEFAULT_INCR_PERCENT,
        get_value_fn=None,
        set_value_fn=None,
        hover_event=None,
        label_fn=None,
    ):
        MenuItemWidget.__init__(self, x, y, label, select_event=lambda: self.increase())
        self.min = min
        self.max = max
        self.incr_perc = incr_perc
        self.current_fill = 0.0
        self.set_value_fn = set_value_fn
        self.get_value_fn = get_value_fn
        self.update_value()

    def update_value(self):
        self.value = self.get_value_fn()
        self.current_fill = self.value / self.max
        return self.value        

    def set_value(self, new_value):
        self.set_value_fn(new_value)

    def increase(self):
        incr = self.max / self.incr_perc
        new_value = self.value + incr
        if new_value > self.max:
            new_value = 0
        self.set_value(new_value)

    def draw(self, screen, rm):
        MenuItemWidget.draw(self, screen, rm)

        self.update_value()

        pygame.draw.rect(
            screen,
            HIGHLIGHT_COLOUR,
            (
                self.x + METER_MARGIN,
                self.y,
                METER_WIDTH * self.current_fill,
                METER_HEIGHT,
            ),
            0
        )

        pygame.draw.rect(
            screen,
            WIDGET_CONFIGS['widget_default_menu_font_colour'],
            (
                self.x + METER_MARGIN,
                self.y,
                METER_WIDTH,
                METER_HEIGHT,
            ),
            1
        )
