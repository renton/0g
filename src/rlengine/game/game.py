import sys
import pygame

from pygame.locals import *
from src.rlengine.config import \
    EVENT_CUSTOM_SWITCH_STATE,  \
    EVENT_CUSTOM_CREATE_STATE


class Game():
    def __init__(
        self,
        sys_config,
        rl_config,
    ):
        self.sys_config = sys_config
        self.rl_config = rl_config

        self._init_time()
        self._init_utils()
        self._init_screen()
        self._init_mouse()
        self._init_player()
        self._init_debug_states()
        self._init_start_state()

    def _init_debug_states(self):
        pass

    def _init_utils(self):
        self.rm = self.rl_config['klass_resource_manager']()
        self.im = self.rl_config['klass_input_manager']()
        self.am = self.rl_config['klass_audio_manager']()
        self.log = None

    def _init_time(self):
        self.clock = pygame.time.Clock()
        self.fps = self.sys_config['default_fps']
        self.playtime = 0.0

    def _init_screen(self):
        flags = pygame.FULLSCREEN if self.sys_config['fullscreen_mode'] else 0
        self.screen = pygame.display.set_mode(
            (
                self.sys_config['window_x_size'],
                self.sys_config['window_y_size']
            ),
            flags
        )
        pygame.display.set_caption(self.sys_config['window_name'])

    def bind_player_entity(self, entity):
        self.player1.bind_entity(entity)

    def _init_player(self):
        self.player1 = self.rl_config['klass_player']()

    def _init_mouse(self):
        self.mouse_x, self.mouse_y = (0, 0)

    def _init_start_state(self):
        self._set_cur_state(self.rl_config['klass_init_state'](self))

    def _set_cur_state(self, state):
        self.cur_state = state

    # TODO pass spread params
    def _evoke_new_state(self, state):
        self._set_cur_state(state(self))

    def _set_mouse_coords(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def mainloop(self):
        while(1):

            # do not go faster than the framerate
            msec = self.clock.tick(self.fps)
            self.playtime += msec / 1000.0

            # reset im key events
            self.im.reset_events()

            # set mouse coords
            self._set_mouse_coords()

            # handle events
            for event in pygame.event.get():
                if event.type == EVENT_CUSTOM_SWITCH_STATE:
                    self._set_cur_state(event.loadstate)
                if event.type == EVENT_CUSTOM_CREATE_STATE:
                    self._evoke_new_state(event.createstate)
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.im.set_key_event(event.type, event.key)
                if event.type == pygame.JOYBUTTONDOWN:
                    self.im.set_joy_button_event(event.type, event.button)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.im.set_mouse_event(event.type, event.button)

            # let state handle input
            self.im.update()
            self.cur_state.input(self.im)

            keystate = pygame.key.get_pressed()

            # emergency exit
            if keystate[K_q] and (keystate[K_LCTRL] or keystate[K_RCTRL]):
                pygame.display.quit()
                sys.exit()

            self.cur_state.set_fps(self.clock.get_fps())
            self.cur_state.run_mainloop()
