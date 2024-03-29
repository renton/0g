import pygame
from pygame.locals import *

from src.rlengine.renderers import MouseRenderer
from src.rlengine.config import \
    GAME_CONFIGS, \
    SYS_CONFIGS, \
    EVENT_CUSTOM_SWITCH_STATE


# TODO pass dynamic mouse_renderer class for custom mouse
class State():
    def __init__(self, game, prev_state=None):
        self.mouse_renderer = MouseRenderer()
        self.game = game
        self.screen = game.screen
        #self.p1 = game.p1
        self.im = game.im
        self.rm = game.rm
        #self.log = game.log

        self.ticks = 0
        self.show_logs = True
        self.show_expanded_logs = False
        self.set_prev_state(prev_state)

        # fps
        self.fps = 0
        self.display_fps = False

        self.bg_colour = GAME_CONFIGS['default_background_colour']
        self.widgets = []

    def run_mainloop(self):
        self._draw()
        self._step()

    def _force_draw(self):
        self._draw()

    def _draw(self):
        self._before_draw()
        self.draw()
        self._after_draw()

    def _step(self):
        self._before_step()
        self.step()
        self._after_step()

    def _before_step(self):
        pass

    def step(self):
        self.ticks += 1

    def _after_step(self):
        pass

    def _before_draw(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_colour)

    def draw_widgets(self):
        for widget in self.widgets:
            widget.draw(self.screen, self.rm)

    def add_widget(self, widget):
        self.widgets.append(widget)

    def _after_draw(self):
        self.draw_widgets()
        # self.draw_logs()

        if self.display_fps:
            self.draw_fps()

        self.mouse_renderer.draw_mouse(self.screen, self.game.mouse_x, self.game.mouse_y)

        pygame.display.flip()

    # TODO logs have their own state -- since logs are global this should work?
    # def draw_logs(self):
    #     if self.show_logs:
    #         count = 0
    #         num_visible = CONFIG['num_visible_logs_expanded'] if self.show_expanded_logs else CONFIG['num_visible_logs']

    #         for entry in self.log.logs:
    #             if count > num_visible:
    #                 break
    #             text = self.rm.get_sysfont().render(str(entry[0]), 1, CONFIG['log_colours'][entry[1]])
    #             self.screen.blit(text, (CONFIG['log_draw_x'], CONFIG['log_draw_y'] - (CONFIG['log_line_height'] * count)))
    #             # TODO last few lines should have transparency
    #             count += 1

    def set_fps(self, fps):
        self.fps = fps

    def draw_fps(self):
        text = self.rm.get_font(0).render(str(self.fps), 1, GAME_CONFIGS['font_configs']['system_font_colour'])
        self.screen.blit(text, (
                                    SYS_CONFIGS['fps_draw_x'],
                                    SYS_CONFIGS['fps_draw_y'],
                                )
                        )

    def toggle_expanded_logs(self):
        self.show_expanded_logs = not self.show_expanded_logs

    def input(self, im):
        if self.im.is_key_event(KEYDOWN, K_ESCAPE):
            if self.prev_state:
                self.close()

        if self.im.is_key_event(KEYDOWN, K_F1):
            self.display_fps = not self.display_fps

    def close(self):
        pygame.event.post(pygame.event.Event(EVENT_CUSTOM_SWITCH_STATE, loadstate=self.prev_state))

    def set_prev_state(self, state):
        self.prev_state = state
