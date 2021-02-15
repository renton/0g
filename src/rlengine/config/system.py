import pygame
from pygame.locals import *

SYS_CONFIGS = {
    'default_fps': 60,
    'fullscreen_mode': False,
    'window_x_size': 1280,
    'window_y_size': 1024,
    'window_name': '0g',
    'tileset_path': 'assets/tilesets/',
    'fps_draw_x': 10,
    'fps_draw_y': 10,
    'tool_tileviewer_max_col_size': 16,
    'tool_tileviewer_font_colour': (0, 0, 0)
}

GAME_CONFIGS = {
    'map_configs': {
        'sample_map_x_size': 10,
        'sample_map_y_size': 10,
        'map_x': 0,
        'map_y': 0,
    },
    'tile_configs': {
        'zoom_levels': (1, 2, 4),
        'tile_size': 16,
        'tilesets': {
            0: {
                'name': '',
                'filename': 'DungeonCrawl_ProjectUtumnoTileset.png',
                'colorkey': (0, 0, 0),
            },
        }
    },

    'font_configs': {
        'font_path': 'assets/fonts/',
        'system_fonts': {
            0: ('DejaVuSans.ttf', 20),
            1: ('DejaVuSans.ttf', 18),
        },
        'system_font_default': 0,
        'system_font_size': 20,
        'system_font_colour': (255, 255, 255),
    },
    'default_background_colour': (0, 0, 0)
}

GAME_CONFIGS['tile_configs']['min_zoom'] = 0
GAME_CONFIGS['tile_configs']['max_zoom'] = len(GAME_CONFIGS['tile_configs']['zoom_levels'])-1

GAME_CONFIGS['map_configs']['map_window_size_x'] = SYS_CONFIGS['window_x_size'] // GAME_CONFIGS['tile_configs']['tile_size']
GAME_CONFIGS['map_configs']['map_window_size_y'] = SYS_CONFIGS['window_y_size'] // GAME_CONFIGS['tile_configs']['tile_size']

WIDGET_CONFIGS = {
    'widget_list_line_spacing': 40,
    'widget_default_menu_line_spacing': 40,
    'widget_default_menu_bg_colour': (40, 40, 40),
    'widget_default_menu_font': 0,
    'widget_default_menu_font_colour': (255, 255, 255)
}

EVENT_CUSTOM_SWITCH_STATE = USEREVENT + 2
EVENT_CUSTOM_CREATE_STATE = USEREVENT + 3
