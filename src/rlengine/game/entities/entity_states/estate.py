

# TODO ability to figure out step that state entered to get rid of just_x bools
# pass step value from game state?
class EState():
    def __init__(self):
        pass

    def exit_estate(self, e):
        pass

    def enter_estate(self, e):
        pass


class EStatefulMixin():
    def __init__(self):
        self.cur_estate_id = None
        self.prev_estate_id = None
        self.estates = {}
        self.state_enter_step = -1

    def add_estate(self, estate_id, estate):
        self.estates[estate_id] = estate

    def get_cur_estate(self):
        return self.estates[self.cur_estate_id]

    def get_cur_estate_id(self):
        return self.cur_estate_id

    def get_prev_estate_id(self):
        return self.prev_estate_id

    def just_entered_state_id(self, id):
        return (self.state_enter_step == (self.life_steps - 1)) and (self.cur_estate_id == id)

    def set_estate(self, estate_id, *args):
        if self.cur_estate_id:
            self.get_cur_estate().exit_estate(self)
            self.prev_estate_id = self.cur_estate_id
        self.cur_estate_id = estate_id
        self.get_cur_estate().enter_estate(self, *args)
        self.state_enter_step = self.life_steps
