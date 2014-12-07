import os
import pygame
from too_many_cooks.errors import HandsFullError


class GlobalVars(object):
    contents = None
    scale = 1.5
    registered_objects = []
    menu_x = 80 * scale
    menu_y = 80 * scale
    menu = ""
    menu_scale = 4.0 * scale
    player = None

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
    def show_menu(cls, menu_type, contents=None):
        print('setting menu: {}'.format(menu_type))
        GlobalVars.contents = contents
        GlobalVars.menu = menu_type

    @classmethod
    def load_menu(cls):
        GlobalVars.no_ingredient_image = pygame.image.load(os.path.join('sprites', 'no_ingredients.png'))
        size = GlobalVars.no_ingredient_image.get_width()
        GlobalVars.no_ingredient_image = pygame.transform.scale(GlobalVars.no_ingredient_image,
                                                                (int(size * GlobalVars.menu_scale),
                                                                 int(size * GlobalVars.menu_scale)))

        GlobalVars.ingredient_list_image = pygame.image.load(os.path.join('sprites', 'ingredient_list.png'))
        GlobalVars.ingredient_list_image = pygame.transform.scale(GlobalVars.ingredient_list_image,
                                                                  (int(size * GlobalVars.menu_scale),
                                                                   int(size * GlobalVars.menu_scale)))
        GlobalVars.full_hands_image = pygame.image.load(os.path.join('sprites', 'full_hands.png'))
        GlobalVars.full_hands_image = pygame.transform.scale(GlobalVars.full_hands_image,
                                                                  (int(size * GlobalVars.menu_scale),
                                                                   int(size * GlobalVars.menu_scale)))

        # GlobalVars.recipe_list_image= pygame.image.load(os.path.join('sprites', 'recipe_list.png'))
        # GlobalVars.new_order= pygame.image.load(os.path.join('sprites', 'new_order.png'))

    @classmethod
    def render(cls, screen):
        if GlobalVars.menu == "No Ingredient":
            screen.blit(GlobalVars.no_ingredient_image, (GlobalVars.menu_x, GlobalVars.menu_y))

        if GlobalVars.menu == "Full Hands":
            screen.blit(GlobalVars.full_hands_image, (GlobalVars.menu_x, GlobalVars.menu_y))

        if GlobalVars.menu == "Show Ingredients":
            if GlobalVars.contents is None:
                raise ValueError('Cannot use Show Ingredients Menu without contents argument.')
            screen.blit(GlobalVars.ingredient_list_image, (GlobalVars.menu_x, GlobalVars.menu_y))

            menu_start_x = GlobalVars.menu_x + 95
            menu_start_y = GlobalVars.menu_y + 95
            menu_offset_x = 160  # TODO: Hard-coding numbers is bad
            menu_offset_y = 125

            if len(GlobalVars.contents):
                screen.blit(GlobalVars.contents[0].image,
                            (menu_start_x, menu_start_y))
            if len(GlobalVars.contents) >= 2:
                screen.blit(GlobalVars.contents[1].image,
                            (menu_start_x + menu_offset_x, menu_start_y))
            if len(GlobalVars.contents) >= 3:
                screen.blit(GlobalVars.contents[2].image,
                            (menu_start_x + menu_offset_x, menu_start_y + menu_offset_y))
            if len(GlobalVars.contents) >= 4:
                screen.blit(GlobalVars.contents[3].image,
                            (menu_start_x + menu_offset_x, menu_start_y + menu_offset_y))

    @classmethod
    def send_message(cls, option):
        if GlobalVars.menu == 'Show Ingredients':
            try:
                option -= 1  # Because we count from 0
                GlobalVars.player.get_ingredient(GlobalVars.contents[option])
                GlobalVars.show_menu('')
            except IndexError:
                pass
            except HandsFullError:
                print("my hands are full")
                GlobalVars.show_menu('Full Hands')

