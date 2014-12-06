import os
import pygame
from too_many_cooks.globals import GlobalVars
from too_many_cooks.tile import Tile


class Kitchen(object):
    def __init__(self, width, height):
        super().__init__()

        floor_image = pygame.image.load(os.path.join('sprites', 'floor.png'))
        scale = GlobalVars.scale * Tile.scale
        floor_image = pygame.transform.scale(floor_image,
                                             (int(floor_image.get_width() * scale),
                                             int(floor_image.get_height() * scale)))
        self.tile_size = floor_image.get_width()

        self.tiles = []
        for w in range(0, width):
            tile_row = []
            for h in range(0, height):
                tile_row.append(Tile(image=floor_image, is_colliding=False))
            self.tiles.append(tile_row)

    def render(self, screen):
        tile_x = 0
        tile_y = 0

        for tile_row in self.tiles:
            tile_x += self.tile_size
            tile_y = 0
            for tile in tile_row:
                screen.blit(tile.image, (tile_x, tile_y))
                tile_y += self.tile_size


