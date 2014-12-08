import os

import pygame

from too_many_cooks.errors import HandsFullError, NoIngredientError
from too_many_cooks.globals import GlobalVars
from too_many_cooks.tile import Tile


class Player(object):
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

        ###

        if self.pos_in_tile['x'] > Tile.size_px - self.collision_fudge:
            if self.kitchen.is_walkable(self.current_tile['x']+1, self.current_tile['y']):
                if self.pos_in_tile['x'] > Tile.size_px:
                    self.pos_in_tile['x'] -= Tile.size_px
                    self.current_tile['x'] += 1
            else:
                self.pos_in_tile['x'] = Tile.size_px - self.collision_fudge
        if self.pos_in_tile['x'] < 0 + self.collision_fudge:
            if self.kitchen.is_walkable(self.current_tile['x']-1, self.current_tile['y']):
                if self.pos_in_tile['x'] < 0:
                    self.pos_in_tile['x'] += Tile.size_px
                    self.current_tile['x'] -= 1
            else:
                self.pos_in_tile['x'] = 0 + self.collision_fudge

        if self.pos_in_tile['y'] > Tile.size_px - self.collision_fudge * 1.8:
            if self.kitchen.is_walkable(self.current_tile['x'], self.current_tile['y']+1):
                if self.pos_in_tile['y']:
                    self.pos_in_tile['y'] -= Tile.size_px
                    self.current_tile['y'] += 1
            else:
                self.pos_in_tile['y'] = Tile.size_px - self.collision_fudge * 1.8
        if self.pos_in_tile['y'] < 0 + self.collision_fudge:
            if self.kitchen.is_walkable(self.current_tile['x'], self.current_tile['y']-1):
                if self.pos_in_tile['y'] < 0:
                    self.pos_in_tile['y'] += Tile.size_px
                    self.current_tile['y'] -= 1
            else:
                self.pos_in_tile['y'] = 0 + self.collision_fudge

        # print('Tile: {}, {}  |  Offset: {}, {}'.format(self.current_tile['x'], self.current_tile['y'], self.pos_in_tile['x'], self.pos_in_tile['y']))

    def hands_are_full(self):
        if self.ingredient_1 and self.ingredient_2:
            return False

    def set_direction(self, direction):
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
        y -= self.image.get_height() / 2
        screen.blit(self.image, (x, y))

        # rect = self.image.get_rect()
        # rect = rect.move(Tile.tile_to_pixel(current_tile=self.current_tile))
        # pygame.draw.rect(screen, (255, 50, 255), rect, 3)

        if self.direction == "up":
            if self.ingredient_1:
                screen.blit(self.ingredient_1.image,(x,y +50))
            if self.ingredient_2:
                screen.blit(self.ingredient_2.image,(x+50,y +50))
        if self.direction == "down":
            if self.ingredient_1:
                screen.blit(self.ingredient_1.image,(x+50,y +50))
            if self.ingredient_2:
                screen.blit(self.ingredient_2.image,(x,y +50))
        if self.direction == "left":
            if self.ingredient_1:
                screen.blit(self.ingredient_1.image,(x+25,y +50))

        if self.direction == "right":
            if self.ingredient_2:
                screen.blit(self.ingredient_2.image,(x+25,y +50))



    def refresh_scale(self):
        move_speed = Player.base_move_speed * GlobalVars.scale
        raise NotImplementedError

    def get_ingredient(self, ingredient):
        if not self.ingredient_1:
            self.ingredient_1 = ingredient
            return
        if not self.ingredient_2:
            self.ingredient_2 = ingredient
            return
        raise HandsFullError

    def use_ingredient(self, ingredient_name):
        ingr = None
        if self.ingredient_1 and self.ingredient_1.name == ingredient_name:
            ingr = self.ingredient_1
            self.ingredient_1 = None
        elif self.ingredient_2 and self.ingredient_2.name == ingredient_name:
            ingr = self.ingredient_2
            self.ingredient_2 = None
        if ingr is not None:
            return ingr
        raise NoIngredientError

    def use_item(self):
        try:
            if self.direction == 'up':
                x = self.current_tile['x']
                y = self.current_tile['y'] - 1
                if y < 0:
                    return
                self.kitchen.tiles[x][y].use(self)
            elif self.direction == 'down':
                x = self.current_tile['x']
                y = self.current_tile['y'] + 1
                self.kitchen.tiles[x][y].use(self)
            elif self.direction == 'right':
                x = self.current_tile['x'] + 1
                y = self.current_tile['y']
                self.kitchen.tiles[x][y].use(self)
            elif self.direction == 'left':
                x = self.current_tile['x'] - 1
                y = self.current_tile['y']
                if x < 0:
                    return
                self.kitchen.tiles[x][y].use(self)
        except IndexError:
            pass

    def get_ingredients(self):
        return self.ingredient_1, self.ingredient_2

