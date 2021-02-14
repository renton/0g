TILE_DATA = {}

TILE_DATA['tilesets'] = {
        0: {
                'name': '',
                'filename': 'DungeonCrawl_ProjectUtumnoTileset.png',
                'colorkey': (0, 0, 0),
            },
}

# TODO walkable, los etc. should be abstracted to a instance of tile
TILE_DATA['gametiles'] = {
                            0: {
                                    'name': 'default',
                                    'description': '',
                                    'tileset_id': 0,
                                    'tile_id': 3024,
                                    'block_colour': None
                                },

                            1: {
                                    'name': 'stone wall 1',
                                    'description': '',
                                    'tileset_id': 0,
                                    'tile_id': 1069,
                                    'block_colour': (10, 10, 60)
                                },
                            }
