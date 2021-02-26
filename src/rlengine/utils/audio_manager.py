import pygame


# TODO channel management?
class AudioManager():
    def __init__(self):
        self.sfx = {}
        self.mfx = {}
        self.cur_music = None

        # TODO volume controls
        self.sfx_volume = 100
        self.mfx_volume = 100

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
        if self.cur_music is None and id in self.mfx:
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
        if id in self.sfx:
            self.sfx[id].play()
