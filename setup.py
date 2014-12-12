import os

_author__ = 'Pablo'
import cx_Freeze



os.chdir("./too_many_cooks")


executables = [cx_Freeze.Executable("__init__.py")]

cx_Freeze.setup(
    name = "Too Many Cooks",
    options = {"build_exe": {"packages":["pygame"],
         "include_files":["sprites/barrel.png", "sprites/beef_patty.png",
         "sprites/burger_bun.png","sprites/cheese.png","sprites/chicken.png","sprites/chopping_block.png","sprites/cook_down.png",
        "sprites/cook_left.png","sprites/cook_right.png","sprites/cook_up.png","sprites/cooked_beef_patty.png", "sprites/cooked_chicken.png",
         "sprites/countertop.png", "sprites/floor.png", "sprites/freezer.png", "sprites/fries.png","sprites/fryer.png","sprites/fridge.png","sprites/full_hands.png",
         "sprites/grill.png","sprites/ingredient_list.png","sprites/pantry.png","sprites/player_down.png","sprites/player_left.png","sprites/player_right.png",
         "sprites/player_up.png","sprites/potato.png","sprites/stove.png","sprites/tomato.png"]}},
    executables = executables


)