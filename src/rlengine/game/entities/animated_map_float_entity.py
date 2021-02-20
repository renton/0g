from .map_float_entity import MapFloatEntity


class AnimationState():
    def __init__(self, frames):

        # tile_id, tileset_id, num_frames
        self.frames = frames
        self.reset()

    def set_type(self):
        self.type = type

    def reset(self):
        self.state_counter = 0
        self.cur_frame = 0

    def reset_last_frame(self):
        self.state_counter = 0
        self.cur_frame = len(self.frames) - 1

    def step(self):
        if self.state_counter > self.frames[self.cur_frame][2]:
            self._switch_frame(self._get_next_frame())

        if self.cur_frame is None:
            return False

        self.state_counter += 1
        return True

    def get_current_tile(self):
        return (self.frames[self.cur_frame][0],  self.frames[self.cur_frame][1])

    def _get_next_frame(self):
        if (len(self.frames) - 1) >= (self.cur_frame + 1):
            return self.cur_frame + 1
        else:
            return None

    def _switch_frame(self, new_frame):
        self.cur_frame = new_frame
        self.state_counter = 0


# TODO Animated should be mixin to be used by grid+float
# TODO Animation data can be shared across entities, does not need to be instanced each time
# TODO w/h in states?
class AnimatedMapFloatEntity(MapFloatEntity):
    def __init__(self, e_id, cur_map, x, y, animation_frames, attr_data=None):
        MapFloatEntity.__init__(self, e_id, cur_map, x, y, attr_data)
        self.a_states = {}
        self.cur_a_state = 0
        self.next_state = None

        for index, animation_frame in enumerate(animation_frames):
            self.a_states[index] = AnimationState(animation_frame)

    def _get_current_sprite(self):
        return self.get_current_a_state().get_current_tile()

    def get_current_a_state(self):
        return self.a_states[self.cur_a_state]

    def step(self, next_x, next_y):
        if not self.get_current_a_state().step():
            if self.next_state is None:
                if self.state_type == 'cycle':
                    self.get_current_a_state().reset()
                if self.state_type == 'freeze':
                    self.get_current_a_state().reset_last_frame()
            else:
                self.switch_animation_state(self.next_state, None, self.state_type)

        MapFloatEntity.step(self, next_x, next_y)

    def switch_animation_state(self, a_state, next_state=None, type='cycle'):
        self.cur_a_state = a_state
        self.next_state = next_state
        self.state_type = type
        self.a_states[self.cur_a_state].reset()
