# TODO absolute or relative pos
class Widget():
    def __init__(self, x, y, select_event=None, hover_event=None):
        self.select_event = select_event
        self.hover_event = hover_event
        self.x = x
        self.y = y

    def get_select_event(self):
        if self.select_event:
            return self.select_event()
        return False

    def get_hover_event(self):
        if self.hover_event:
            return self.hover_event()
        return False

    def draw(self, screen, rm):
        pass
