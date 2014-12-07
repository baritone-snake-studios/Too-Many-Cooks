from collections import namedtuple
import os
import pygame
from too_many_cooks import Kitchen
from too_many_cooks.globals import GlobalVars
from too_many_cooks.tile import Tile


class Player(object):
    base_move_speed = 5
    move_speed = base_move_speed * GlobalVars.scale

    def __init__(self, start_x, start_y):
        super().__init__()
        self.scale = GlobalVars.scale * 4

        image = pygame.image.load(os.path.join('sprites', 'player_up.png'))
        self.up_image = pygame.transform.scale(image,
                                               (int(image.get_width() * self.scale),
                                                int(image.get_height() * self.scale)))

        image = pygame.image.load(os.path.join('sprites', 'player_down.png'))
        self.down_image = pygame.transform.scale(image,
                                               (int(image.get_width() * self.scale),
                                                int(image.get_height() * self.scale)))

        image = pygame.image.load(os.path.join('sprites', 'player_left.png'))
        self.left_image = pygame.transform.scale(image,
                                               (int(image.get_width() * self.scale),
                                                int(image.get_height() * self.scale)))

        image = pygame.image.load(os.path.join('sprites', 'player_right.png'))
        self.right_image = pygame.transform.scale(image,
                                               (int(image.get_width() * self.scale),
                                                int(image.get_height() * self.scale)))
        self.image = self.down_image

        self.current_tile = {
            'x': start_x,
            'y': start_y
        }
        self.pos_in_tile = {
            'x': 0,
            'y': 0
        }

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_up:
            self.pos_in_tile['y'] -= Player.move_speed
            self.image = self.up_image
        if self.moving_down:
            self.pos_in_tile['y'] += Player.move_speed
            self.image = self.down_image
        if self.moving_left:
            self.pos_in_tile['x'] -= Player.move_speed
            self.image = self.left_image
        if self.moving_right:
            self.pos_in_tile['x'] += Player.move_speed
            self.image = self.right_image

        if self.pos_in_tile['x'] > Tile.size_px:
            self.pos_in_tile['x'] -= Tile.size_px
            self.current_tile['x'] += 1
        if self.pos_in_tile['x'] < 0:
            self.pos_in_tile['x'] += Tile.size_px
            self.current_tile['x'] -= 1
        if self.pos_in_tile['y'] > Tile.size_px:
            self.pos_in_tile['y'] -= Tile.size_px
            self.current_tile['y'] += 1
        if self.pos_in_tile['y'] < 0:
            self.pos_in_tile['y'] += Tile.size_px
            self.current_tile['y'] -= 1

    def set_direction(self, direction):
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        if direction == 'up':
            self.moving_up = True
        if direction == 'down':
            self.moving_down = True
        if direction == 'left':
            self.moving_left = True
        if direction == 'right':
            self.moving_right = True

    def render(self, screen):
        x, y = Kitchen.tile_to_pixel(current_tile=self.current_tile, pos_in_tile=self.pos_in_tile)
        screen.blit(self.image, (x, y))

    def refresh_scale(self):
        move_speed = Player.base_move_speed * GlobalVars.scale
        raise NotImplementedError

