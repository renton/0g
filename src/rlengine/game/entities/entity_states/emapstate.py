from .estate import EState, EStatefulMixin


class EMapState(EState):
    def __init__(self):
        EState.__init__(self)

    def get_estate_sprite(self, e):
        return [e._generate_base_tile()]

    def get_estate_sprite_draw_offset(self, e):
        return (0, 0)

    def get_estate_sprite_draw_transform(self, e, sprite):
        return sprite

    def get_estate_block_colour(self, e):
        return e.block_colour


# TODO organize inheritance better
class EMapStatefulMixin(EStatefulMixin):
    def __init__(self):
        EStatefulMixin.__init__(self)

    def get_sprites_to_draw(self):
        if self.cur_estate_id is None:
            return [self._generate_base_tile()]
        else:
            return self.get_cur_estate().get_estate_sprite(self)

    def get_sprite_draw_offset_xy(self):
        if self.cur_estate_id is None:
            return (0, 0)
        else:
            return self.get_cur_estate().get_estate_sprite_draw_offset(self)

    def get_sprite_draw_transform(self, sprite):
        if self.cur_estate_id is None:
            return sprite
        else:
            return self.get_cur_estate().get_estate_sprite_draw_transform(self, sprite)

    def get_block_colour(self):
        if self.cur_estate_id is None:
            return self.block_colour
        else:
            return self.get_cur_estate().get_estate_block_colour(self)
