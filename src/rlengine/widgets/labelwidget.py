from src.rlengine.widgets import Widget
from src.rlengine.config import GAME_CONFIGS, WIDGET_CONFIGS


class LabelWidget(Widget):
    def __init__(self, x, y, label, select_event=None, hover_event=None, label_fn=None):
        Widget.__init__(self, x, y, select_event, hover_event)
        self.label = label
        self.label_fn = label_fn

    def update_label(self):
        if self.label_fn:
            self.label = self.label_fn()
        return self.label

    def draw(self, screen, rm):
        label = self.update_label()
        text = rm.get_font(WIDGET_CONFIGS['widget_default_menu_font']).render(
            str(label),
            1,
            WIDGET_CONFIGS['widget_default_menu_font_colour']
        )
        screen.blit(
            text,
            (
                self.x,
                self.y
            )
        )
