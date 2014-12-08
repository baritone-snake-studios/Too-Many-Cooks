
class CantMakeRecipeError(Exception):
    pass


class Recipe(object):
    required_ingredients_names = []

    @classmethod
    def make(cls, ingredients):
        if not ingredients:
            raise CantMakeRecipeError

        new_contents = []
        ingredients_names = [i.name for i in ingredients]

        for ingr in cls.required_ingredients_names:
            if ingr not in ingredients_names:
                raise CantMakeRecipeError

        return [item for item in ingredients if item.name not in cls.required_ingredients_names]


class BurgerRecipe(Recipe):
    required_ingredients_names = ['Cooked Patty', 'Burger Buns', 'Lettuce', 'Tomato']
    pass


class FryRecipe(Recipe):
    required_ingredients_names = ['Fries']
    pass