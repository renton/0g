import pygame

DEFAULT_VOLUME_SOUND = 1.0
DEFAULT_VOLUME_MUSIC = 1.0


# TODO channel management?
class AudioManager():
    def __init__(self):
        self.sfx = {}
        self.mfx = {}
        self.cur_music = None

        self.mfx_enabled = True
        self.sfx_enabled = True

        self.adjust_sfx_volume(DEFAULT_VOLUME_SOUND)
        self.adjust_mfx_volume(DEFAULT_VOLUME_MUSIC)

    def adjust_sfx_volume(self, new_vol):
        self.sfx_volume = new_vol

    def adjust_mfx_volume(self, new_vol):
        self.mfx_volume = new_vol
        pygame.mixer.music.set_volume(self.mfx_volume)

    def load_sounds(self, sound_data):
        for k, v in sound_data.items():
            self.load_sound(k, v)

    def load_musics(self, music_data):
        for k, v in music_data.items():
            self.load_music(k, v)

    def load_music(self, id, filename):
        self.mfx[id] = filename

    def load_sound(self, id, filename):
        self.sfx[id] = pygame.mixer.Sound(filename)

    def start_music(self, id, loops=-1, start=0, fade_ms=0):
        if self.cur_music is None and id in self.mfx and self.mfx_enabled:
            self.cur_music = id
            pygame.mixer.music.load(self.mfx[id])
            pygame.mixer.music.play(loops, start, fade_ms)

    def pause_music(self):
        if self.cur_music:
            pygame.mixer.music.pause()

    def unpause_music(self):
        if self.cur_music:
            pygame.mixer.music.unpause()

    def stop_music(self, fade_ms=0):
        if self.cur_music:
            self.cur_music = None
            pygame.mixer.music.fadeout(fade_ms)

    def transition_music(self, id):
        pass

    def play_sound(self, id):
        if id in self.sfx and self.sfx_enabled:
            if self.sfx[id].get_volume() != self.sfx_volume:
                self.sfx[id].set_volume(self.sfx_volume)
            self.sfx[id].play()
