from too_many_cooks import GlobalVars


class CantMakeRecipeError(Exception):
    pass


class Recipe(object):
    required_ingredients_names = []
    score = 0

    @classmethod
    def make(cls, ingredients):
        if not ingredients:
            raise CantMakeRecipeError

        ingredients_names = [i.name for i in ingredients]

        for ingr in cls.required_ingredients_names:
            if ingr not in ingredients_names:
                raise CantMakeRecipeError

        GlobalVars.score += cls.score
        GlobalVars.render_score = True
        return [item for item in ingredients if item.name not in cls.required_ingredients_names]


class BurgerRecipe(Recipe):
    required_ingredients_names = ['Cooked Patty', 'Burger Buns', 'Lettuce', 'Tomato']
    score = 20
    pass


class FryRecipe(Recipe):
    required_ingredients_names = ['Fries']
    score = 5
    pass