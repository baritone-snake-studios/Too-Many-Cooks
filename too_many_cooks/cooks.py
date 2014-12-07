import os
import pygame
from too_many_cooks import GlobalVars
from too_many_cooks.tile import Tile


class Cook(object):
    base_move_speed = 5
    move_speed = base_move_speed * GlobalVars.scale

    def __init__(self, start_x, start_y, kitchen):
        super().__init__()
        self.kitchen = kitchen
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
        self.collision_fudge = self.image.get_width() * 0.25

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
        self.direction = 'down'

        self.ingredient_1 = None
        self.ingredient_2 = None

    def update(self):
        if self.moving_up:
            self.pos_in_tile['y'] -= Cook.move_speed
            self.image = self.up_image
        if self.moving_down:
            self.pos_in_tile['y'] += Cook.move_speed
            self.image = self.down_image

        if self.moving_left:
            self.pos_in_tile['x'] -= Cook.move_speed
            self.image = self.left_image
        if self.moving_right:
            self.pos_in_tile['x'] += Cook.move_speed
            self.image = self.right_image

        # ##

        if self.pos_in_tile['x'] > Tile.size_px - self.collision_fudge:
            if self.kitchen.is_walkable(self.current_tile['x'] + 1, self.current_tile['y']):
                if self.pos_in_tile['x'] > Tile.size_px:
                    self.pos_in_tile['x'] -= Tile.size_px
                    self.current_tile['x'] += 1
            else:
                self.pos_in_tile['x'] = Tile.size_px - self.collision_fudge
        if self.pos_in_tile['x'] < 0 + self.collision_fudge:
            if self.kitchen.is_walkable(self.current_tile['x'] - 1, self.current_tile['y']):
                if self.pos_in_tile['x'] < 0:
                    self.pos_in_tile['x'] += Tile.size_px
                    self.current_tile['x'] -= 1
            else:
                self.pos_in_tile['x'] = 0 + self.collision_fudge

        if self.pos_in_tile['y'] > Tile.size_px - self.collision_fudge * 1.8:
            if self.kitchen.is_walkable(self.current_tile['x'], self.current_tile['y'] + 1):
                if self.pos_in_tile['y']:
                    self.pos_in_tile['y'] -= Tile.size_px
                    self.current_tile['y'] += 1
            else:
                self.pos_in_tile['y'] = Tile.size_px - self.collision_fudge * 1.8
        if self.pos_in_tile['y'] < 0 + self.collision_fudge:
            if self.kitchen.is_walkable(self.current_tile['x'], self.current_tile['y'] - 1):
                if self.pos_in_tile['y'] < 0:
                    self.pos_in_tile['y'] += Tile.size_px
                    self.current_tile['y'] -= 1
            else:
                self.pos_in_tile['y'] = 0 + self.collision_fudge
