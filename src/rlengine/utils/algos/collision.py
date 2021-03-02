from .rl_math import distance_between_points


def collide_circle_to_circle(c1_x, c1_y, c1_r, c2_x, c2_y, c2_r):
    dist = distance_between_points(c1_x, c1_y, c2_x, c2_y)
    return dist < (c1_r + c2_r)


def collide_rect_to_rect(rect1, rect2):
    return rect1.colliderect(rect2)


# clamping
def collide_rect_to_circle():
    pass
