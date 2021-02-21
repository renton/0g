import math


def distance_between_points(orig_x, orig_y, dest_x, dest_y):
    adj = dest_x - orig_x
    opp = dest_y - orig_y
    return math.sqrt(math.pow(opp, 2) + math.pow(adj, 2))


def get_normalized_vector(orig_x, orig_y, dest_x, dest_y):
    adj = dest_x - orig_x
    opp = dest_y - orig_y
    hyp = distance_between_points(orig_x, orig_y, dest_x, dest_y)

    if hyp == 0:
        return (0, 1)
    else:
        return ((adj/hyp), (opp/hyp))


def get_angle_between_line_and_x_axis(orig_x, orig_y, dest_x, dest_y):
    return math.atan2(dest_y - orig_y, dest_x - orig_x) * 180 / math.pi
