import os

_author__ = 'Pablo'
import cx_Freeze


os.chdir("./too_many_cooks")

executables = [cx_Freeze.Executable("__init__.py", targetName='TooManyCooks.exe',
                                    shortcutName='Too Many Cooks.lnk', shortcutDir='../')]

# NOTE: You may have to move the sprites in the newly created build folder
# From the root into a ./sprites/ folder. Sometimes it does this, sometimes it doesn't.
# You will also need to include freesansbold.ttf in the directory,
# or edit globals.py (line 102, myfont = ...) to a different font, and then include that
# cx_Freeze doesn't copy the pygame default fonts, for some reason

# At the time of writing, there is a bug in the python3.4 build of cx_Freeze from pip
# Use this instead:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze


cx_Freeze.setup(
    name="Too Many Cooks",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["sprites/barrel.png",
                                             "sprites/beef_patty.png",
                                             "sprites/burger_bun.png",
                                             "sprites/cheese.png",
                                             "sprites/chicken.png",
                                             "sprites/chopping_block.png",
                                             "sprites/cook_down.png",
                                             "sprites/cook_left.png",
                                             "sprites/cook_right.png",
                                             "sprites/cook_up.png",
                                             "sprites/cooked_beef_patty.png",
                                             "sprites/cooked_chicken.png",
                                             "sprites/countertop.png",
                                             "sprites/floor.png",
                                             "sprites/freezer.png",
                                             "sprites/fries.png",
                                             "sprites/fryer.png",
                                             "sprites/fridge.png",
                                             "sprites/full_hands.png",
                                             "sprites/grill.png",
                                             "sprites/ingredient_list.png",
                                             "sprites/no_ingredients.png",
                                             "sprites/pantry.png",
                                             "sprites/player_down.png",
                                             "sprites/player_left.png",
                                             "sprites/player_right.png",
                                             "sprites/player_up.png",
                                             "sprites/potato.png",
                                             "sprites/stove.png",
                                             "sprites/tomato.png",
                                             "sprites/lettuce.png"
                           ]}},
    executables=executables


)