import os
import pygame


class GlobalVars(object):

    scale = 1.5
    registered_objects = []
    menu_x =20
    menu_y = 20

    @classmethod
    def register_game_obj(cls, obj):
        GlobalVars.registered_objects.append(obj)

    @classmethod
    def mult_scale(cls, multiplier):
        GlobalVars.change_scale(GlobalVars.scale * multiplier)

    @classmethod
    def change_scale(cls, new_scale):
        print('scale: {}'.format(new_scale))
        GlobalVars.scale = new_scale

        for obj in GlobalVars.registered_objects:
            obj.refresh_scale()
    @classmethod
    def show_menu(cls, menu_type):
        GlobalVars.menu= menu_type

    @classmethod
    def load_menu(cls, load_menu):
        GlobalVars.no_ingredient_image = pygame.image.load(os.path.join('sprites', 'no_ingredient.png'))
        GlobalVars.recipe_list_image= pygame.image.load(os.path.join('sprites', 'recipe_list.png'))
        GlobalVars.ingredient_list= pygame.image.load(os.path.join('sprites', 'ingredient_list.png'))
        GlobalVars.new_order= pygame.image.load(os.path.join('sprites', 'new_order.png'))

    @classmethod
    def render(cls, screen):
        if GlobalVars.menu== "No Ingredient":
            screen.blit(self.image, (menu_x, menu_y))