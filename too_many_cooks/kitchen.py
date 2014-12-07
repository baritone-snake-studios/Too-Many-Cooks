import os
import pygame
from too_many_cooks.globals import GlobalVars
from too_many_cooks.tile import Tile


class Kitchen(object):
    def __init__(self, width, height):
        super().__init__()

        self.base_floor_image = pygame.image.load(os.path.join('sprites', 'floor.png'))
        self.tile_scale = GlobalVars.scale * Tile.scale
        floor_image = pygame.transform.scale(self.base_floor_image,
                                             (int(self.base_floor_image.get_width() * self.tile_scale),
                                              int(self.base_floor_image.get_height() * self.tile_scale)))
        Tile.size_px = floor_image.get_width()

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
            tile_x += Tile.size_px
            tile_y = 0
            for tile in tile_row:
                screen.blit(tile.image, (tile_x, tile_y))
                tile_y += Tile.size_px

    def refresh_scale(self):
        self.tile_scale = GlobalVars.scale * Tile.scale
        floor_image = pygame.transform.scale(self.base_floor_image,
                                             (int(self.base_floor_image.get_width() * self.tile_scale),
                                              int(self.base_floor_image.get_height() * self.tile_scale)))
        Tile.size_px = floor_image.get_width()

        for tile_row in self.tiles:
            for tile in tile_row:
                tile.image = floor_image


