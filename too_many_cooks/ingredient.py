
class Ingredient(object):
    def __init__(self, image, name):
        super().__init__()
        self.image = image
        self.name = name
        self.is_fresh = True
