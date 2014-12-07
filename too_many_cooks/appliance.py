import os
import pygame
from too_many_cooks import player
from too_many_cooks.globals import GlobalVars
from too_many_cooks.tile import Tile


class Appliance(object):
    def __init__(self, image_path, start_x, start_y):
        super().__init__()
        self.scale = GlobalVars.scale * 4

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,
                               (int(self.image.get_width() * self.scale),
                                int(self.image.get_height() * self.scale)))

        self.current_tile = {
            'x': start_x,
            'y': start_y
        }

    def render(self, screen):
        x, y = Tile.tile_to_pixel(current_tile=self.current_tile)
        screen.blit(self.image, (x, y))

    def use(self, user):
        pass


class CantGetItem(Exception):
    pass


class Storage(Appliance):
    def __init__(self, start_x, start_y, type,contents=None):
        image_path = (os.path.join('sprites', '{}.png'.format(type)))
        super().__init__(image_path, start_x, start_y)
        self.contents = contents

    def use(self, user):
        if user.hands_are_full():
            raise CantGetItem


        user.get_ingredient(self.contents[0])

class Grill(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'grill.png'))
        super().__init__(image_path, start_x, start_y)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class Fryer(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'fryer.png'))
        super().__init__(image_path, start_x, start_y)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()
        print('You have {} in your left hand, and {} in your right hand'.format(ingr_1, ingr_2))


class ChoppingBlock(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'choppingblock.png'))
        super().__init__(image_path, start_x, start_y)


    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class Oven(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'oven.png'))
        super().__init__(image_path, start_x, start_y)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class CounterTop(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'countertop.png'))
        super().__init__(image_path, start_x, start_y)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class Stove(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'stove.png'))
        super().__init__(image_path, start_x, start_y)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()
        print('You have {} in your left hand, and {} in your right hand'.format(ingr_1, ingr_2))




