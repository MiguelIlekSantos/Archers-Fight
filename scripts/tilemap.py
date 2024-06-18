import pygame

LOCATIONS = [(0, 1), (1, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

class Tilemap:
    def __init__(self, surf, game, tile_size=16):
        self.surf = surf
        self.game = game
        self.offgrid = []
        self.tilemap = {}
        self.tile_size = tile_size

        for x in range(10):    
            self.tilemap[str(x) + ';10'] = {"type": "grass", "variant": 1, "pos": [x, 10]}
            self.tilemap[str(x) + ';0'] = {"type": "grass", "variant": 1, "pos": [x, 0]}
        for y in range(10):    
            self.tilemap['10;' + str(y)] = {"type": "stone", "variant": 1, "pos": [10, y]}
            self.tilemap['0;' + str(y)] = {"type": "stone", "variant": 1, "pos": [0, y]}

    def tiles_around(self, player_pos):
        self.player_pos = list(player_pos)
        self.player_pos[0] = self.player_pos[0] // self.tile_size
        self.player_pos[1] = self.player_pos[1] // self.tile_size

        tiles = []

        for loc in LOCATIONS:
            tile = str(self.player_pos[0] + loc[0]) + ';' + str(self.player_pos[1] + loc[1])
            
            if tile in self.tilemap:
                tileInfo = self.tilemap[tile]
                tiles.append(pygame.Rect(tileInfo["pos"][0] * self.tile_size, tileInfo["pos"][1] * self.tile_size, self.tile_size, self.tile_size))
        
        return tiles

    def render(self):
        for key in self.tilemap:
            tile = self.tilemap[key]  
            img = self.game.assets[f'tiles/{tile["type"]}'][tile["variant"]]
            self.surf.blit(img, (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
    
