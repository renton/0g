class Player():
    def __init__(self):
        self.e = None

    def bind_entity(self, e):
        if self.e:
            self.unbind_entity()    
        e.set_ai(False)
        self.e = e

    def unbind_entity(self):
        if self.e is not None:
            self.e.set_ai(False)
            self.e = None
