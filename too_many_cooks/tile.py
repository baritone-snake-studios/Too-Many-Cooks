
class Tile(object):
    def __init__(self, image, is_colliding):
        super().__init__()
        self.image = image
        self.is_colliding = is_colliding
