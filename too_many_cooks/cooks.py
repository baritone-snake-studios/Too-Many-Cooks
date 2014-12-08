import os
import pygame
from too_many_cooks.globals import GlobalVars
from too_many_cooks.tile import Tile


class Cook(object):
    base_move_speed = 3
    move_speed = base_move_speed * GlobalVars.scale

    def __init__(self, start_x, start_y, kitchen):
        super().__init__()
        self.kitchen = kitchen
        self.scale = GlobalVars.scale * 4

        image = pygame.image.load(os.path.join('sprites', 'cook_up.png'))
        self.up_image = pygame.transform.scale(image,
                                               (int(image.get_width() * self.scale),
                                                int(image.get_height() * self.scale)))

        image = pygame.image.load(os.path.join('sprites', 'cook_down.png'))
        self.down_image = pygame.transform.scale(image,
                                                 (int(image.get_width() * self.scale),
                                                  int(image.get_height() * self.scale)))

        image = pygame.image.load(os.path.join('sprites', 'cook_left.png'))
        self.left_image = pygame.transform.scale(image,
                                                 (int(image.get_width() * self.scale),
                                                  int(image.get_height() * self.scale)))

        image = pygame.image.load(os.path.join('sprites', 'cook_right.png'))
        self.right_image = pygame.transform.scale(image,
                                                  (int(image.get_width() * self.scale),
                                                   int(image.get_height() * self.scale)))
        self.image = self.down_image
        self.collision_fudge = self.image.get_width() * 0.25
        self.collision = False

        self.paths = []
        self.current_path = 0
        self.current_path_distance = 0
        self.move_speed = Cook.base_move_speed

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

    def add_path(self, direction, tiles, speed, wait_after):
        self.paths.append({
            'direction': direction,
            'distance':  tiles,
            'speed': speed,
            'wait_after': wait_after,
        })

    def update(self):
        old_tile = dict(self.current_tile)
        old_pos = dict(self.pos_in_tile)
        old_path_distance = self.current_path_distance

        if self.moving_up:
            self.pos_in_tile['y'] -= self.move_speed
            self.image = self.up_image
        if self.moving_down:
            self.pos_in_tile['y'] += self.move_speed
            self.image = self.down_image

        if self.moving_left:
            self.pos_in_tile['x'] -= self.move_speed
            self.image = self.left_image
        if self.moving_right:
            self.pos_in_tile['x'] += self.move_speed
            self.image = self.right_image

        ###
        if self.pos_in_tile['x'] > Tile.size_px - self.collision_fudge:
            if self.pos_in_tile['x'] > Tile.size_px:
                self.current_path_distance += 1
                if self.kitchen.is_walkable(self.current_tile['x'] + 1, self.current_tile['y']):
                    self.pos_in_tile['x'] -= Tile.size_px
                    self.current_tile['x'] += 1
                else:
                    self.pos_in_tile['x'] = Tile.size_px - self.collision_fudge
        elif self.pos_in_tile['x'] < 0 + self.collision_fudge:
            if self.pos_in_tile['x'] < 0:
                self.current_path_distance += 1
                if self.kitchen.is_walkable(self.current_tile['x'] - 1, self.current_tile['y']):
                    self.pos_in_tile['x'] += Tile.size_px
                    self.current_tile['x'] -= 1
                else:
                    self.pos_in_tile['x'] = 0 + self.collision_fudge

        if self.pos_in_tile['y'] > Tile.size_px - self.collision_fudge * 1.8:
            if self.pos_in_tile['y'] > Tile.size_px:
                self.current_path_distance += 1
                if self.kitchen.is_walkable(self.current_tile['x'], self.current_tile['y'] + 1):
                    self.pos_in_tile['y'] -= Tile.size_px
                    self.current_tile['y'] += 1
                else:
                    self.pos_in_tile['y'] = Tile.size_px - self.collision_fudge * 1.8
        elif self.pos_in_tile['y'] < 0 + self.collision_fudge:
            if self.pos_in_tile['y'] < 0:
                self.current_path_distance += 1
                if self.kitchen.is_walkable(self.current_tile['x'], self.current_tile['y'] - 1):
                    self.pos_in_tile['y'] += Tile.size_px
                    self.current_tile['y'] -= 1
                else:
                    self.pos_in_tile['y'] = 0 + self.collision_fudge

        if self.current_path_distance != old_path_distance:
            path = self.paths[self.current_path]
            if self.current_path_distance >= path['distance']:
                self.next_path()
                self.current_tile = old_tile
                self.pos_in_tile = old_pos

    def set_direction(self, direction):
        print('set_drection({})'.format(direction))
        self.direction = direction

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
        x, y = Tile.tile_to_pixel(current_tile=self.current_tile, pos_in_tile=self.pos_in_tile)
        x -= self.image.get_width() / 2
        y -= self.image.get_height()
        screen.blit(self.image, (x, y))

        if self.collision:
            rect = self.image.get_rect()
            rect = rect.move(Tile.tile_to_pixel(current_tile=self.current_tile))
            pygame.draw.rect(screen, (255, 50, 255), rect, 3)

        # rect = self.image.get_rect()
        # rect = rect.move(Tile.tile_to_pixel(current_tile=self.current_tile))
        # pygame.draw.rect(screen, (255, 50, 255), rect, 3)

        if self.direction == "up":
            if self.ingredient_1:
                screen.blit(self.ingredient_1.image, (x, y + 50))
            if self.ingredient_2:
                screen.blit(self.ingredient_2.image, (x + 50, y + 50))
        if self.direction == "down":
            if self.ingredient_1:
                screen.blit(self.ingredient_1.image, (x + 50, y + 50))
            if self.ingredient_2:
                screen.blit(self.ingredient_2.image, (x, y + 50))
        if self.direction == "left":
            if self.ingredient_1:
                screen.blit(self.ingredient_1.image, (x + 25, y + 50))

        if self.direction == "right":
            if self.ingredient_2:
                screen.blit(self.ingredient_2.image, (x + 25, y + 50))

    def go(self):
        path = self.paths[0]

        self.current_path_distance = 0
        self.set_direction(path['direction'])
        self.move_speed = path['speed']

    def next_path(self):
        self.current_path += 1
        if self.current_path >= len(self.paths):
            self.current_path = 0

        path = self.paths[self.current_path]

        self.current_path_distance = 0
        self.set_direction(path['direction'])
        self.move_speed = path['speed']


