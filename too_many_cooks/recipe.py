
class Recipe(object):
    required_ingredients_names = []

    @classmethod
    def can_make(cls, ingredients):
        for ingr in ingredients:
            if ingr.name not in cls.required_ingredients_names:
                return False
        return True


class BurgerRecipe(Recipe):
    required_ingredients_names = ['Cooked Patty', 'Burger Buns', 'Lettuce', 'Tomato']
    pass


class FryRecipe(Recipe):
    required_ingredients_names = ['French Fries']
    pass