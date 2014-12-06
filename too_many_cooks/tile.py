
class Tile(object):
    scale = 4.0

    def __init__(self, image, is_colliding):
        super().__init__()
        self.image = image
        self.is_colliding = is_colliding
