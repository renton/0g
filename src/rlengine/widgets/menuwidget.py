from src.rlengine.widgets import MenuItemWidget, Widget
from src.rlengine.config import WIDGET_CONFIGS


class MenuWidget(Widget):
    def __init__(self, x, y, select_event=None):
        Widget.__init__(self, x, y, select_event)
        self.menu_items = []
        self.cur_target = 0

    def add_option_item(self, option_widget):
        option_widget.x = self.x
        option_widget.y = self.y + (WIDGET_CONFIGS['widget_default_menu_line_spacing'] * len(self.menu_items))
        self.menu_items.append(option_widget)

    def add_menu_item(self, label, select_event=None):
        self.menu_items.append(MenuItemWidget(self.x, self.y + (WIDGET_CONFIGS['widget_default_menu_line_spacing'] * len(self.menu_items)), label, select_event))

    def draw(self, screen, rm):
        for menu_item in self.menu_items:
            menu_item.draw(screen, rm)

    def select(self, index):
        if len(self.menu_items) > index:
            self.cur_target = index
            self.unset_highlight()
            self.menu_items[index].selected = True

    def clear(self):
        self.menu_items = []

    def item_select_event(self):
        return self.menu_items[self.cur_target].select_event

    def unset_highlight(self):
        for menu_item in self.menu_items:
            menu_item.selected = False

    def cycle_next(self):
        if self.cur_target >= len(self.menu_items) - 1:
            self.select(0)
        else:
            self.select(self.cur_target + 1)

    def cycle_last(self):
        if self.cur_target <= 0:
            self.select(len(self.menu_items) - 1)
        else:
            self.select(self.cur_target - 1)
