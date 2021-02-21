import pygame


class MouseRenderer():
    def __init__(self):
        pygame.mouse.set_visible(False)
        self.block_mode = True
        self.mouse_image = None
        self.mouse_offset_x = 0
        self.mouse_offset_y = 0

    def draw_mouse(self, screen, x, y):
        if self.block_mode:
            blocks = self.get_blocks_to_draw()
            for block in blocks:
                x_offset, y_offset, w, h, colour = block
                pygame.draw.rect(
                    screen,
                    colour,
                    (
                        x + self.mouse_offset_x + x_offset,
                        y + self.mouse_offset_y + y_offset,
                        w,
                        h
                    ),
                    0
                )
        else:
            pass

    def get_blocks_to_draw(self):
        return [
            (-1, -1, 3, 3, (160, 160, 160)),
            (0, 0, 1, 1, (0, 0, 0)),
            (10, -3, 1, 7, (200, 200, 200)),
            (-10, -3, 1, 7, (200, 200, 200)),
            (-3, -10, 7, 1, (160, 160, 160)),
            (-3, 10, 7, 1, (160, 160, 160)),
        ]
