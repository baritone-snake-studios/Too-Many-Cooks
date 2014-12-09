import os
import pygame
from too_many_cooks.appliance import Stove, Storage, Fryer, ChoppingBlock, Grill, Oven, CounterTop
from too_many_cooks.globals import GlobalVars
from too_many_cooks.ingredient import ingredients
from too_many_cooks.tile import Tile


class Kitchen(object):
    def __init__(self, width, height):
        super().__init__()

        self.base_floor_image = pygame.image.load(os.path.join('sprites', 'floor.png'))
        self.tile_scale = GlobalVars.scale * Tile.scale
        floor_image = pygame.transform.scale(self.base_floor_image,
                                             (int(self.base_floor_image.get_width() * self.tile_scale),
                                              int(self.base_floor_image.get_height() * self.tile_scale)))
        Tile.size_px = floor_image.get_width()

        self.appliances = []

        self.tiles = []
        for w in range(0, width + 1):
            tile_row = []
            for h in range(0, height + 1):
                tile_row.append(Tile(image=floor_image, is_colliding=False))
            self.tiles.append(tile_row)

    def render(self, screen):
        tile_x = 0
        tile_y = 0

        for tile_row in self.tiles:
            tile_y = 0
            for tile in tile_row:
                screen.blit(tile.image, (tile_x, tile_y))
                tile_y += Tile.size_px
            tile_x += Tile.size_px

        for appliance in self.appliances:
            appliance.render(screen=screen)

    def refresh_scale(self):
        self.tile_scale = GlobalVars.scale * Tile.scale
        floor_image = pygame.transform.scale(self.base_floor_image,
                                             (int(self.base_floor_image.get_width() * self.tile_scale),
                                              int(self.base_floor_image.get_height() * self.tile_scale)))
        Tile.size_px = floor_image.get_width()

        for tile_row in self.tiles:
            for tile in tile_row:
                tile.image = floor_image

    def make_tile_collidable(self, x, y, is_colliding=True):
        self.tiles[x][y].is_colliding = is_colliding

    def is_walkable(self, x, y):
        try:
            if x < 0 or y < 0:
                raise ValueError
            return not self.tiles[x][y].is_colliding
        except (IndexError, ValueError):
            return False

    def setup_level(self, level):
        if level == 1:
            self.setup_level_one()
        elif level == 2:
            self.setup_level_two()
        elif level == 3:
            self.setup_level_three()
        elif level == 4:
            self.setup_level_four()
        elif level == 5:
            self.setup_level_five()

    def setup_level_one(self):
        grill = Grill(2, 0)
        self.make_tile_collidable(2, 0)
        self.tiles[2][0].appliance = grill
        self.appliances.append(grill)

        stove = Stove(0, 0)
        self.make_tile_collidable(0, 0)
        self.tiles[0][0].appliance = stove
        self.appliances.append(stove)

        fryer = Fryer(1, 0)
        self.make_tile_collidable(1, 0)
        self.tiles[1][0].appliance = fryer
        self.appliances.append(fryer)

        countertop = CounterTop(3, 0)
        self.make_tile_collidable(3, 0)
        self.tiles[3][0].appliance = countertop
        self.appliances.append(countertop)

        fridge = Storage(0, 2, type="fridge", allowed_directions=['up'])
        self.make_tile_collidable(0, 2)
        self.tiles[0][2].appliance = fridge
        self.appliances.append(fridge)
        fridge.contents = [ingredients['Tomato'], ingredients['Lettuce']]
        # move fridge after second level

        freezer = Storage(4, 0, type="freezer")
        self.make_tile_collidable(4, 0)
        self.tiles[4][0].appliance = freezer
        self.appliances.append(freezer)
        freezer.contents = [ingredients['Beef Patty']]

        barrel = Storage(4, 3, type="barrel")
        self.make_tile_collidable(4, 3)
        self.tiles[4][3].appliance = barrel
        self.appliances.append(barrel)
        barrel.contents = [ingredients['Potato']]

        pantry = Storage(4, 2, type="pantry", allowed_directions=['right'])
        self.make_tile_collidable(4, 2)
        self.tiles[4][2].appliance = pantry
        self.appliances.append(pantry)
        pantry.contents = [ingredients['Burger Buns']]



    def setup_level_two(self):
        grill = Grill(2, 0)
        self.make_tile_collidable(2, 0)
        self.tiles[2][0].appliance = grill
        self.appliances.append(grill)

        stove = Stove(0, 0)
        self.make_tile_collidable(0, 0)
        self.tiles[0][0].appliance = stove
        self.appliances.append(stove)

        fryer = Fryer(1, 0)
        self.make_tile_collidable(1, 0)
        self.tiles[1][0].appliance = fryer
        self.appliances.append(fryer)

        countertop = CounterTop(3, 0)
        self.make_tile_collidable(3, 0)
        self.tiles[3][0].appliance = countertop
        self.appliances.append(countertop)

        fridge = Storage(0, 2, type="fridge", allowed_directions=['up'])
        self.make_tile_collidable(0, 2)
        self.tiles[0][2].appliance = fridge
        self.appliances.append(fridge)
        fridge.contents = [ingredients['Tomato'], ingredients['Lettuce'], ingredients['Cheese']]
        # move fridge after second level

        freezer = Storage(4, 0, type="freezer")
        self.make_tile_collidable(4, 0)
        self.tiles[4][0].appliance = freezer
        self.appliances.append(freezer)
        freezer.contents = [ingredients['Beef Patty']]

        barrel = Storage(4, 3, type="barrel")
        self.make_tile_collidable(4, 3)
        self.tiles[4][3].appliance = barrel
        self.appliances.append(barrel)
        barrel.contents = [ingredients['Potato']]

        pantry = Storage(4, 2, type="pantry", allowed_directions=['right'])
        self.make_tile_collidable(4, 2)
        self.tiles[4][2].appliance = pantry
        self.appliances.append(pantry)
        pantry.contents = [ingredients['Burger Buns']]

        choppingblock = ChoppingBlock(2, 2)
        self.make_tile_collidable(2, 2)
        self.tiles[2][2].appliance = choppingblock
        self.appliances.append(choppingblock)

    def setup_level_three(self):
        stove = Stove(0, 0)
        self.make_tile_collidable(0, 0)
        self.tiles[0][0].appliance = stove
        self.appliances.append(stove)

        grill = Grill(2, 0)
        self.make_tile_collidable(2, 0)
        self.tiles[2][0].appliance = grill
        self.appliances.append(grill)

        fryer = Fryer(1, 0)
        self.make_tile_collidable(1, 0)
        self.tiles[1][0].appliance = fryer
        self.appliances.append(fryer)

        countertop = CounterTop(3, 0)
        self.make_tile_collidable(3, 0)
        self.tiles[3][0].appliance = countertop
        self.appliances.append(countertop)

        choppingblock = ChoppingBlock(3, 2)
        self.make_tile_collidable(3, 2)
        self.tiles[3][2].appliance = choppingblock
        self.appliances.append(choppingblock)

        fridge = Storage(0, 2, type="fridge", allowed_directions=['up'])
        self.make_tile_collidable(0, 2)
        self.tiles[0][2].appliance = fridge
        self.appliances.append(fridge)
        fridge.contents = [ingredients['Tomato'], ingredients['Lettuce'], ingredients['Cheese']]

        freezer = Storage(5, 0, type="freezer",allowed_directions=['up'])
        self.make_tile_collidable(5, 0)
        self.tiles[5][0].appliance = freezer
        self.appliances.append(freezer)
        freezer.contents = [ingredients['Beef Patty'], ingredients['Chicken']]

        barrel = Storage(5, 3, type="barrel")
        self.make_tile_collidable(5, 3)
        self.tiles[5][3].appliance = barrel
        self.appliances.append(barrel)
        barrel.contents = [ingredients['Potato']]

        pantry = Storage(5, 2, type="pantry", allowed_directions=['right'])
        self.make_tile_collidable(5, 2)
        self.tiles[5][2].appliance = pantry
        self.appliances.append(pantry)
        pantry.contents = [ingredients['Burger Buns']]

    def setup_level_four(self):
        grill = Grill(0, 0)
        self.make_tile_collidable(0, 0)
        self.tiles[0][0].appliance = grill
        self.appliances.append(grill)

        stove = Stove(2, 0)
        self.make_tile_collidable(2, 0)
        self.tiles[2][0].appliance = stove
        self.appliances.append(stove)

        fryer = Fryer(1, 0)
        self.make_tile_collidable(1, 0)
        self.tiles[1][0].appliance = fryer
        self.appliances.append(fryer)

        countertop = CounterTop(4, 2)
        self.make_tile_collidable(4, 2)
        self.tiles[4][2].appliance = countertop
        self.appliances.append(countertop)

        choppingblock = ChoppingBlock(2, 2)
        self.make_tile_collidable(2, 2)
        self.tiles[2][2].appliance = choppingblock
        self.appliances.append(choppingblock)

        choppingblock = ChoppingBlock(4, 1)
        self.make_tile_collidable(4, 1)
        self.tiles[4][1].appliance = choppingblock
        self.appliances.append(choppingblock)

        # oven = Oven(1, 0)
        # self.make_tile_collidable(1, 0)
        # self.tiles[1][0].appliance = oven
        # self.appliances.append(oven)

        fridge = Storage(6, 2, type="fridge", allowed_directions=['up'])
        self.make_tile_collidable(6, 2)
        self.tiles[6][2].appliance = fridge
        self.appliances.append(fridge)
        fridge.contents = [ingredients['Tomato'], ingredients['Lettuce'], ingredients['Cheese']]

        freezer = Storage(6, 0, type="freezer", allowed_directions=['up'])
        self.make_tile_collidable(6, 0)
        self.tiles[6][0].appliance = freezer
        self.appliances.append(freezer)
        freezer.contents = [ingredients['Beef Patty'],ingredients['Chicken']]

        barrel = Storage(0, 4, type="barrel")
        self.make_tile_collidable(0, 4)
        self.tiles[0][4].appliance = barrel
        self.appliances.append(barrel)
        barrel.contents = [ingredients['Potato']]

        pantry = Storage(6, 4, type="pantry", allowed_directions=['right'])
        self.make_tile_collidable(6, 4)
        self.tiles[6][4].appliance = pantry
        self.appliances.append(pantry)
        pantry.contents = [ingredients['Burger Buns']]

        # Chicken = Storage(3, 3, type= "dessertfreezer")
        # self.make_tile_collidable(3,3)
        # self.tiles[3][3].appliance = dessertfreezer
        # self.appliances.append(dessertfreezer)

    def setup_level_five(self):
        grill = Grill(0, 0)
        self.make_tile_collidable(0, 0)
        self.tiles[0][0].appliance = grill
        self.appliances.append(grill)

        stove = Stove(2, 0)
        self.make_tile_collidable(2, 0)
        self.tiles[2][0].appliance = stove
        self.appliances.append(stove)

        fryer = Fryer(1, 0)
        self.make_tile_collidable(1, 0)
        self.tiles[1][0].appliance = fryer
        self.appliances.append(fryer)

        countertop = CounterTop(4, 2)
        self.make_tile_collidable(4, 2)
        self.tiles[4][2].appliance = countertop
        self.appliances.append(countertop)

        choppingblock = ChoppingBlock(2, 2)
        self.make_tile_collidable(2, 2)
        self.tiles[2][2].appliance = choppingblock
        self.appliances.append(choppingblock)

        choppingblock = ChoppingBlock(4, 1)
        self.make_tile_collidable(4, 1)
        self.tiles[4][1].appliance = choppingblock
        self.appliances.append(choppingblock)

        # oven = Oven(1, 0)
        # self.make_tile_collidable(1, 0)
        # self.tiles[1][0].appliance = oven
        # self.appliances.append(oven)

        fridge = Storage(6, 2, type="fridge", allowed_directions=['up'])
        self.make_tile_collidable(6, 2)
        self.tiles[6][2].appliance = fridge
        self.appliances.append(fridge)
        fridge.contents = [ingredients['Tomato'], ingredients['Lettuce'], ingredients['Cheese']]

        freezer = Storage(6, 0, type="freezer", allowed_directions=['up'])
        self.make_tile_collidable(6, 0)
        self.tiles[6][0].appliance = freezer
        self.appliances.append(freezer)
        freezer.contents = [ingredients['Beef Patty'],ingredients['Chicken']]

        barrel = Storage(0, 5, type="barrel")
        self.make_tile_collidable(0, 5)
        self.tiles[0][5].appliance = barrel
        self.appliances.append(barrel)
        barrel.contents = [ingredients['Potato']]

        pantry = Storage(6, 5, type="pantry", allowed_directions=['right'])
        self.make_tile_collidable(6, 5)
        self.tiles[6][5].appliance = pantry
        self.appliances.append(pantry)
        pantry.contents = [ingredients['Burger Buns']]

        # Chicken = Storage(3, 3, type= "dessertfreezer")
        # self.make_tile_collidable(3,3)
        # self.tiles[3][3].appliance = dessertfreezer
        # self.appliances.append(dessertfreezer)

    def clear_kitchen(self, and_the_kitchen_sink):
        pass