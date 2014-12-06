from too_many_cooks.tile import Tile


class Appliance(Tile):
    def __init__(self, image_path):
        super().__init__(image=image_path, is_colliding=True)

    def use(self, user):
        pass


class CantGetItem(Exception):
    pass


class Storage(Tile):
    def __init__(self, image, contents=None):
        super().__init__(self, image)
        self.contents = contents

    def use(self, user):
        if user.hands_are_full():
            raise CantGetItem

        ingr_1, ingr_2 = user.get_ingredients()


class Grill(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class Fryer(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class ChoppingBlock(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class Oven(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()


class CounterTop(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)

    def use(self, user):
        ingr_1, ingr_2 = user.get_ingredients()



