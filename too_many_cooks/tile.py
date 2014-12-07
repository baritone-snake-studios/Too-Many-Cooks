
class Tile(object):
    scale = 4.0
    size_px = None

    def __init__(self, image, is_colliding):
        super().__init__()
        self.image = image
        self.is_colliding = is_colliding
        self.appliance = None

    def use(self, user):
        if self.appliance is not None:
            self.appliance.use(user)

    @staticmethod
    def tile_to_pixel(current_tile, pos_in_tile=None):
        if pos_in_tile is None:
            pos_in_tile = {'x': 0, 'y': 0}
        tile_x, tile_y = current_tile['x'], current_tile['y']
        offset_x, offset_y = pos_in_tile['x'], pos_in_tile['y']
        return Tile.size_px * tile_x + offset_x, Tile.size_px * tile_y + offset_y
