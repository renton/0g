from src.rlengine.widgets import LabelWidget
from src.rlengine.config import GAME_CONFIGS, WIDGET_CONFIGS


class MenuItemWidget(LabelWidget):
    def __init__(self, x, y, label, select_event=None):
        LabelWidget.__init__(self, x, y, label, select_event)
        self.selected = False

    def draw(self, screen, rm):
        highlight = WIDGET_CONFIGS['widget_default_menu_bg_colour'] if self.selected else GAME_CONFIGS['default_background_colour']
        text = rm.get_font(WIDGET_CONFIGS['widget_default_menu_font']).render(self.label, 1, WIDGET_CONFIGS['widget_default_menu_font_colour'], highlight)
        screen.blit(text, (
                                    self.x,
                                    self.y,
                                )
                        )
