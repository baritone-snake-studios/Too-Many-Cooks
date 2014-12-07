import os
import pygame


class Ingredient(object):
    def __init__(self, name, image_path):
        super().__init__()
        self.name = name
        # self.image = pygame.image.load(image_path)


beef_patty = Ingredient('Beef Patty', os.path.join('sprites', 'beef_patty.png'))
burger_bun = Ingredient('Buger Buns', os.path.join('sprites', 'burger_bun.png'))
Potato = Ingredient('Potato', os.path.join('sprites', 'potato.png'))
lettuce = Ingredient('Lettuce', os.path.join('sprites', 'lettuce.png'))
tomato = Ingredient('Tomato', os.path.join('sprites', 'tomato.png'))



ingredients = {
    'Beef Patty': beef_patty,
    'Burger Buns': burger_bun,
    'Potato': Potato,
    'Lettuce': lettuce,
    'Tomato': tomato,
}