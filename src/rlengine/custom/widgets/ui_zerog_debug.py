
from src.rlengine.widgets import ListWidget

UI_DEBUG_X = 20
UI_DEBUG_Y = 40


class UI_ZeroGDebug(ListWidget):
    def __init__(self, mapstate):
        ListWidget.__init__(self, UI_DEBUG_X, UI_DEBUG_Y)
        self.mapstate = mapstate
        self.add_data(lambda: 'x :' + str(self.mapstate.player.e.x))
        self.add_data(lambda: 'y :' + str(self.mapstate.player.e.y))
        self.add_data(lambda: '#projs :' + str(len(self.mapstate.em.entity_groups['PROJS'])))
