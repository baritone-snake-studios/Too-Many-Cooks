import os
import pygame
from too_many_cooks import GlobalVars


class Ingredient(object):
    menu_scale = 0.5
    def __init__(self, name, image_path):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image_path)
        size = self.image.get_width()
        self.image = pygame.transform.scale(self.image,
                                            (int(size * GlobalVars.menu_scale * Ingredient.menu_scale),
                                             int(size * GlobalVars.menu_scale * Ingredient.menu_scale)))

    def __repr__(self):
        return self.name


beef_patty = Ingredient('Beef Patty', os.path.join('sprites', 'beef_patty.png'))
burger_bun = Ingredient('Buger Buns', os.path.join('sprites', 'burger_bun.png'))
Potato = Ingredient('Potato', os.path.join('sprites', 'potato.png'))
lettuce = Ingredient('Lettuce', os.path.join('sprites', 'lettuce.png'))
tomato = Ingredient('Tomato', os.path.join('sprites', 'tomato.png'))
fries = Ingredient('French Fries', os.path.join('sprites', 'fries.png'))

ingredients = {
    'Beef Patty': beef_patty,
    'Burger Buns': burger_bun,
    'Potato': Potato,
    'Lettuce': lettuce,
    'Tomato': tomato,
    'French Fries' : fries,
}