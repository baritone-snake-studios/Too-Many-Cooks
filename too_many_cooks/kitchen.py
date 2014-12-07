import os
import pygame
from too_many_cooks.appliance import Stove, Storage
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

        self.appliances = []

        self.tiles = []
        for w in range(0, width+1):
            tile_row = []
            for h in range(0, height+1):
                tile_row.append(Tile(image=floor_image, is_colliding=False))
            self.tiles.append(tile_row)

    def render(self, screen):
        tile_x = 0
        tile_y = 0

        for tile_row in self.tiles:
            tile_y = 0
            for tile in tile_row:
                screen.blit(tile.image, (tile_x, tile_y))
                tile_y += Tile.size_px
            tile_x += Tile.size_px

        for appliance in self.appliances:
            appliance.render(screen=screen)

    def refresh_scale(self):
        self.tile_scale = GlobalVars.scale * Tile.scale
        floor_image = pygame.transform.scale(self.base_floor_image,
                                             (int(self.base_floor_image.get_width() * self.tile_scale),
                                              int(self.base_floor_image.get_height() * self.tile_scale)))
        Tile.size_px = floor_image.get_width()

        for tile_row in self.tiles:
            for tile in tile_row:
                tile.image = floor_image

    def make_tile_collidable(self, x, y, is_colliding=True):
        self.tiles[x][y].is_colliding = is_colliding

    def is_walkable(self, x, y):
        try:
            if x < 0 or y < 0:
                raise ValueError
            return not self.tiles[x][y].is_colliding
        except (IndexError, ValueError):
            return False

    def setup_level(self, level):
        if level == 1:
            self.setup_level_one()
        elif level == 2:
            self.setup_level_two()
        elif level == 3:
            self.setup_level_three()
        elif level == 4:
            self.setup_level_four()

    def setup_level_one(self):
        stove = Stove(5, 3)
        self.make_tile_collidable(5, 3)
        self.tiles[5][3].appliance = stove
        self.appliances.append(stove)

        freezer = Storage(5,0, type= "freezer")
        self.make_tile_collidable(5, 0)
        self.tiles[5][0].appliance = freezer
        self.appliances.append(freezer)

    def setup_level_two(self):
        raise NotImplementedError

    def setup_level_three(self):
        raise NotImplementedError

    def setup_level_four(self):
        raise NotImplementedError