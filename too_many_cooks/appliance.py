from too_many_cooks.tile import Tile


class Appliance(Tile):
    def __init__(self, image_path):
        super().__init__(image=image_path, is_colliding=True)

    def use(self):
        pass


class Grill(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


class Fryer(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


class ChoppingBlock(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


class Oven(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


class CounterTop(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


class Barrel(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


class Fridge(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


class VegieFreezer(Appliance):
    def __init__(self, image_path):
        super().__init__(image_path)


class DessertFreezer(Appliance)
    def __init__(self, image_path):
        super().__init__(image_path)


