from src.rlengine.widgets import Widget
from src.rlengine.config import GAME_CONFIGS, WIDGET_CONFIGS


class ListWidget(Widget):
    def __init__(self, x, y, select_event=None):
        Widget.__init__(self, x, y, select_event)
        self.data = {}

    def add_data(self, data):
        self.data = data

    def clear_data(self):
        self.data = {}

    def draw(self, screen, rm):
        count = 0
        for k, v in self.data.items():
            text = rm.get_font(GAME_CONFIGS['font_configs']['system_font_default']).render(str(k) + " : " + str(v), 1, GAME_CONFIGS['font_configs']['system_font_colour'])
            screen.blit(text, (
                                        self.x,
                                        self.y + (WIDGET_CONFIGS['widget_list_line_spacing'] * count),
                                    )
                            )
            count += 1
