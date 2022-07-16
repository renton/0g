
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
        self.add_data(lambda: 'gameover :' + str(self.mapstate.is_game_over))
        self.add_data(lambda: 'player :' + str(self.mapstate.player.e.u_id))
        self.add_data(lambda: 'mx :' + str(self.mapstate.game.mouse_map_x))
        self.add_data(lambda: 'my :' + str(self.mapstate.game.mouse_map_y))
        self.add_data(lambda: 'sfx :' + str(self.mapstate.game.am.sfx_volume))
        self.add_data(lambda: 'mfx :' + str(self.mapstate.game.am.mfx_volume))
        
        self.add_data(lambda: 'off_x :' + str(self.mapstate.player.e.get_cur_estate().get_estate_sprite_draw_offset(self.mapstate.player.e)[0]))
        self.add_data(lambda: 'off_y :' + str(self.mapstate.player.e.get_cur_estate().get_estate_sprite_draw_offset(self.mapstate.player.e)[1]))
