import pygame
import sys
from src.rlengine.config import GAME_CONFIGS, SYS_CONFIGS


class ResourceManager():
    def __init__(self):
        self.tilesets = {}
        self.sounds = {}
        self.fonts = {}
        self.music = {}
        self._load_system_fonts()

    def get_num_tiles_loaded(self):
        total = {}
        for k, v in self.tilesets.items():
            for ck, cv in v.items():
                if k not in total:
                    total[k] = 0
                total[k] += len(cv)
        return total

    def load_tileset_by_id(self, id):
        self._load_tileset(GAME_CONFIGS['tile_configs']['tilesets'][id])

    def _load_tileset(
        self,
        tileset
    ):
        width = tileset['tile_width']
        height = tileset['tile_height']

        if tileset['filename'] in self.tilesets:
            return

        self.tilesets[tileset['filename']] = {}

        image = pygame.image.load(SYS_CONFIGS['tileset_path'] + tileset['filename']).convert()
        image.set_colorkey(tileset['colorkey'])
        image_width, image_height = image.get_size()

        col = 0
        for tile_x in range(0, image_width // width):
            for tile_y in range(0, image_height // height):
                rect = (tile_x * width, tile_y * height, width, height)
                count = 0
                self.tilesets[tileset['filename']][col] = {}
                for i in GAME_CONFIGS['tile_configs']['zoom_levels']:
                    self.tilesets[tileset['filename']][col][i] = pygame.transform.scale(image.subsurface(rect), (width * i, height * i))
                    count += 1
                col += 1

    # TODO if tile doesn't exists, have an error tile
    def get_tile(self, filename, tile_id, scale=1):
        return self.tilesets[filename][tile_id][scale]

    def get_tile_by_id(self, tileset_id, tile_id, scale=1):
        if GAME_CONFIGS['tile_configs']['tilesets'][tileset_id]['filename'] not in self.tilesets:
            print("Loading tileset: " + str(tileset_id))
            self.load_tileset_by_id(tileset_id)
        return self.tilesets[GAME_CONFIGS['tile_configs']['tilesets'][tileset_id]['filename']][tile_id][scale]

    def unload_tileset(self, filename):
        del self.tilesets[filename]

    def load_font_by_id(self, font_id):
        if font_id not in self.fonts:
            font_name = GAME_CONFIGS['font_configs']['system_fonts'][font_id]
            self.fonts[font_id] = {
                        'filename' : font_name[0],
                        'size' : font_name[1],
                        'obj' : pygame.font.Font(GAME_CONFIGS['font_configs']['font_path'] + font_name[0], font_name[1]),
                    }

    def unload_font_by_id(self, font_id):
        if font_id in self.fonts:
            del self.fonts[font_id]

    def _load_system_fonts(self):
        for k, font in GAME_CONFIGS['font_configs']['system_fonts'].items():
            self.load_font_by_id(k)

    def get_sysfont(self):
        return self.fonts[0]['obj']

    def _get_font(self, id):
        if id in self.fonts:
            return self.fonts[id]['obj']
        else:
            return self.get_sysfont()

    def get_font(self, id):
        cur_font = self._get_font(id)
        cur_font.set_bold(False)
        return cur_font

    def get_bold_font(self, id):
        cur_font = self._get_font(id)
        cur_font.set_bold(True)
        return cur_font
