import math
from src.rlengine.game.entities import MapFloatEntity


class Hero(MapFloatEntity):
    def __init__(self, cur_map, x, y):
        MapFloatEntity.__init__(self, 0, cur_map, x, y, {})

        self.first_launch_speed = 6
        self.second_launch_speed = 8

        self.is_first_launched = False
        self.is_second_launched = False
        self.just_hit_wall = False
        self.just_launched = False
        self.large_wall_force = False
        self.on_wall = True

        self.launch_coord_x = 0
        self.launch_coord_y = 0

    # TODO support for multiple primitives with different positions
    def get_sprites_to_draw(self):
        return [['block']]

    def step(self, next_x, next_y):
        MapFloatEntity.step(self, next_x, next_y)

    def hit_wall(self):
        if not self.on_wall:
            if self.is_second_launched:
                self.large_wall_force = True
            self.is_first_launched = False
            self.is_second_launched = False
            self.just_hit_wall = True
            self.on_wall = True

    def get_launch_coords(self):
        return (self.launch_coord_x, self.launch_coord_y)

    def action_launch(self, dest_x, dest_y):
        if not self.is_first_launched:
            x, y = self.get_xy()
            self.launch_coord_x = x
            self.launch_coord_y = y
            self._launch(dest_x, dest_y, self.first_launch_speed)
            self.just_launched = True
            self.is_first_launched = True
        else:
            if not self.is_second_launched:
                self._launch(dest_x, dest_y, self.second_launch_speed)
                self.is_second_launched = True

    def _launch(self, dest_x, dest_y, speed):
        self.on_wall = False
        orig_x, orig_y = self.get_xy()

        adj_large = dest_x - orig_x
        opp_large = dest_y - orig_y
        hyp_large = math.sqrt(math.pow(opp_large, 2) + math.pow(adj_large, 2))

        if hyp_large == 0:
            self.set_ddx(0)
            self.set_ddy(speed * -1)
        else:
            self.set_ddx((adj_large/hyp_large) * speed)
            self.set_ddy((opp_large/hyp_large) * speed)
