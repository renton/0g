import math
from src.rlengine.game.entities import MapFloatEntity


class Hero(MapFloatEntity):
    def __init__(self, cur_map, x, y):
        MapFloatEntity.__init__(self, 0, cur_map, x, y, {})

        self.first_launch_speed = 6
        self.second_launch_speed = 8

        self.is_first_launched = False
        self.is_second_launched = False

    def hit_wall(self):
        self.is_first_launched = False
        self.is_second_launched = False

    def action_launch(self, dest_x, dest_y):
        if not self.is_first_launched:
            self._launch(dest_x, dest_y, self.first_launch_speed)
            self.is_first_launched = True
        else:
            if not self.is_second_launched:
                self._launch(dest_x, dest_y, self.second_launch_speed)
                self.is_second_launched = True

    def _launch(self, dest_x, dest_y, speed):
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
