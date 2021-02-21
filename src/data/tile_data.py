TILE_DATA = {}

TILE_DATA['tilesets'] = {
        0: {
                'name': '',
                'filename': 'DungeonCrawl_ProjectUtumnoTileset.png',
                'colorkey': (0, 0, 0),
                'tile_width': 32,
                'tile_height': 32,
            },
        1: {
                'name': 'Robo Static',
                'filename': 'RoboStatic.png',
                'colorkey': (0, 0, 0),
                'tile_width': 32,
                'tile_height': 64,
            },
}

SPRITE_DATA = {
    0: {
        'name': 'robo_static_1',
        'tileset_id': 1,
        'tile_id': 0,
        'block_colour': None
    },
    1: {
        'name': 'robo_static_2',
        'tileset_id': 1,
        'tile_id': 0,
        'block_colour': None
    },
}

# TODO walkable, los etc. should be abstracted to a instance of tile
# TODO handle None tile_id for no draw
TILE_DATA['gametiles'] = {
                            0: {
                                    'name': 'default',
                                    'description': '',
                                    'tileset_id': 0,
                                    'tile_id': 1405,
                                    'block_colour': None,
                                    'is_walkable': True
                                },

                            1: {
                                    'name': 'stone wall 1',
                                    'description': '',
                                    'tileset_id': 0,
                                    'tile_id': 1069,
                                    'block_colour': (170, 170, 170),
                                    'is_walkable': False
                                },
                        }
