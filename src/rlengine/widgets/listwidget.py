from src.rlengine.widgets import Widget
from src.rlengine.config import GAME_CONFIGS, WIDGET_CONFIGS


# TODO improve update lambda
# TODO formatting
# TODO passing in values instead of using consts
class ListWidget(Widget):
    def __init__(self, x, y, select_event=None, update_fn=None):
        Widget.__init__(self, x, y, select_event)
        self.data = []

    def add_data(self, update_fn):
        self.data.append(update_fn)

    def clear_data(self):
        self.data = []

    def draw(self, screen, rm):
        count = 0
        for v in self.data:
            text = rm.get_font(GAME_CONFIGS['font_configs']['system_font_default']).render(str(v()), 1, GAME_CONFIGS['font_configs']['system_font_colour'])
            screen.blit(text, (
                                        self.x,
                                        self.y + (WIDGET_CONFIGS['widget_list_line_spacing'] * count),
                                    )
                            )
            count += 1
