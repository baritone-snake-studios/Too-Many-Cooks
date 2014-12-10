import os

import pygame
import random
from too_many_cooks import ingredient

from too_many_cooks.errors import CantGetItem, NoIngredientError
from too_many_cooks.globals import GlobalVars
from too_many_cooks.recipe import BurgerRecipe, CantMakeRecipeError, FryRecipe, ChickenRecipe, CheeseBurgerRecipe
from too_many_cooks.tile import Tile


class Appliance(object):
    def __init__(self, image_path, start_x, start_y):
        super(Appliance, self).__init__()
        self.scale = GlobalVars.scale * 4

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,
                                            (int(self.image.get_width() * self.scale),
                                             int(self.image.get_height() * self.scale)))

        self.current_tile = {
            'x': start_x,
            'y': start_y
        }
        self.contents = []

    def render(self, screen):
        x, y = Tile.tile_to_pixel(current_tile=self.current_tile)
        screen.blit(self.image, (x, y))

    def use(self, user):
        pass

    def recieve_ingredients(self, user, ingredients, keep_ingredients=False):
        recieved_ingredients = False
        for ingredient in ingredients:
            try:
                ingr = user.use_ingredient(ingredient)
                if keep_ingredients:
                    self.contents.append(ingr)
                recieved_ingredients = True
                print('Used {}'.format(ingredient))
            except NoIngredientError:
                pass

        if not recieved_ingredients:
            print("You're not holding any {}".format(' or '.join(ingredients)))
            GlobalVars.show_menu('No Ingredient')
            return False
        else:
            return True


class Storage(Appliance):
    def __init__(self, start_x, start_y, type, contents=None, allowed_directions=None):
        image_path = (os.path.join('sprites', '{}.png'.format(type)))
        super(Storage, self).__init__(image_path, start_x, start_y)

        self.contents = contents
        self.allowed_directions = allowed_directions

    def use(self, user):
        if user.hands_are_full():
            raise CantGetItem
        if not self.allowed_directions or user.direction in self.allowed_directions:
            GlobalVars.show_menu('Show Ingredients', contents=self.contents)


class Grill(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'grill.png'))
        super(Grill, self).__init__(image_path, start_x, start_y)

    def use(self, user):
        if self.recieve_ingredients(user, ['Beef Patty', 'Bacon']):
            GlobalVars.player.get_ingredient(ingredient.cooked_beef_patty)

class Fryer(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'fryer.png'))
        super(Fryer, self).__init__(image_path, start_x, start_y)

    def use(self, user):
        if self.recieve_ingredients(user, ['Potato']):
            GlobalVars.player.get_ingredient(ingredient.fries)





class ChoppingBlock(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'chopping_block.png'))
        super(ChoppingBlock, self).__init__(image_path, start_x, start_y)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class Oven(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'oven.png'))
        super(Oven, self).__init__(image_path, start_x, start_y)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()




class CounterTop(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'countertop.png'))
        super(CounterTop, self).__init__(image_path, start_x, start_y)

    def use(self, user):
        if self.recieve_ingredients(user, ['Cheese', 'Cooked Chicken','Cooked Patty', 'Burger Buns', 'Lettuce', 'Tomato', 'Fries'], keep_ingredients=True):
            try:
                self.contents = CheeseBurgerRecipe.make(self.contents)
                print("Made a cheese burger. Current Score: {}".format(GlobalVars.score))
            except CantMakeRecipeError:
                pass

            try:
                self.contents = BurgerRecipe.make(self.contents)
                print("Made a burger. Current Score: {}".format(GlobalVars.score))
            except CantMakeRecipeError:
                pass

            try:
                self.contents = FryRecipe.make(self.contents)
                print("Made french fries. Current Score: {}".format(GlobalVars.score))
            except CantMakeRecipeError:
                pass
            try:
                self.contents =  ChickenRecipe.make(self.contents)
                print("Made chicken sandwich. Current Score: {}".format(GlobalVars.score))
            except CantMakeRecipeError:
                pass

    def render(self, screen):
        super(CounterTop, self).render(screen)
        x, y = Tile.tile_to_pixel(current_tile=self.current_tile)

        i = 0
        for ingredient in self.contents:
            offset_x, offset_y = self.item_offset(i)
            i += 1
            screen.blit(ingredient.image, (x + offset_x, y + offset_y))

    def item_offset(self, i):
        random.seed(i * 2)
        x = random.randint(0, 50)
        y = random.randint(-5, 30)
        return x, y


class Stove(Appliance):
    def __init__(self, start_x, start_y):
        image_path = (os.path.join('sprites', 'stove.png'))
        super(Stove, self).__init__(image_path, start_x, start_y)

    def use(self, user):
        if self.recieve_ingredients(user, ['Tomato', 'Chicken', 'Noodles']):
            GlobalVars.player.get_ingredient(ingredient.cooked_chicken)




