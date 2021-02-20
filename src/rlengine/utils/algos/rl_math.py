import math


def get_normalized_vector(orig_x, orig_y, dest_x, dest_y):
    adj_large = dest_x - orig_x
    opp_large = dest_y - orig_y
    hyp_large = math.sqrt(math.pow(opp_large, 2) + math.pow(adj_large, 2))

    if hyp_large == 0:
        return (0, 1)
    else:
        return ((adj_large/hyp_large), (opp_large/hyp_large))
