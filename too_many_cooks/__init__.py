import pygame
import sys
from too_many_cooks.cooks import Cook
from too_many_cooks.globals import GlobalVars
from too_many_cooks.kitchen import Kitchen
from too_many_cooks.player import Player


def run_game():
    current_level = 1
    pygame.init()
    window_width, window_height= get_window_size()
    DISPLAY_SURFACE = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Too Many Cooks!")

    FPS = get_max_fps()
    FpsClock = pygame.time.Clock()

    kitchen = Kitchen(width=4, height=3)
    GlobalVars.register_game_obj(kitchen)
    kitchen.setup_level(1)

    player = Player(start_x=2, start_y=2, kitchen=kitchen)
    player.pos_in_tile = {'x': 50, 'y': 50}
    GlobalVars.register_game_obj(player)
    GlobalVars.player = player

    cooks = []

    GlobalVars.load_menu()

    time_last_update = 0
    while True:
        time = FpsClock.get_time()
        # Check the keyboard & mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    GlobalVars.send_message(1)
                if event.key == pygame.K_2:
                    GlobalVars.send_message(2)
                if event.key == pygame.K_3:
                    GlobalVars.send_message(3)
                if event.key == pygame.K_4:
                    GlobalVars.send_message(4)

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_UP:
                    player.set_direction('up')
                    GlobalVars.show_menu("")
                if event.key == pygame.K_DOWN:
                    player.set_direction('down')
                    GlobalVars.show_menu("")
                if event.key == pygame.K_LEFT:
                    player.set_direction('left')
                    GlobalVars.show_menu("")
                if event.key == pygame.K_RIGHT:
                    player.set_direction('right')
                    GlobalVars.show_menu("")

                if event.key == pygame.K_SPACE:
                    if not GlobalVars.menu:
                        player.use_item()
                    else:
                        GlobalVars.show_menu("")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.moving_up = False
                if event.key == pygame.K_DOWN:
                    player.moving_down = False
                if event.key == pygame.K_LEFT:
                    player.moving_left = False
                if event.key == pygame.K_RIGHT:
                    player.moving_right = False

        player_old_tile = dict(player.current_tile)
        player_old_pos_in_tile = dict(player.pos_in_tile)
        player.update()

        cook_collision = False
        for cook in cooks:
            cook.update()
            if player.current_tile == cook.current_tile:
                cook.collision = True
                cook_collision = True
            else:
                cook.collision = False

        if cook_collision:
            player.current_tile = player_old_tile
            player.pos_in_tile = player_old_pos_in_tile

        DISPLAY_SURFACE.fill((155, 180, 200))

        kitchen.render(screen=DISPLAY_SURFACE)
        for cook in cooks:
            cook.render(screen=DISPLAY_SURFACE)
        player.render(screen=DISPLAY_SURFACE)

        GlobalVars.render(screen=DISPLAY_SURFACE)

        pygame.display.update()
        FpsClock.tick(FPS)

        if GlobalVars.go_to_next_level:
            GlobalVars.go_to_next_level = False

            if GlobalVars.level == 2:
                GlobalVars.deregister([kitchen])
                kitchen = Kitchen(4, 3)
                kitchen.setup_level_two()
                player.kitchen = kitchen

                GlobalVars.deregister(cooks)
                cook = Cook(start_x=1, start_y=1, kitchen=kitchen)
                cooks.append(cook)
                cook.add_path(direction='down', tiles=3, speed=2, wait_after=50)
                cook.add_path(direction='up', tiles=3, speed=2, wait_after=200)
                cook.go()

                GlobalVars.register_game_obj(cooks[0])
                cooks[0].pos_in_tile = {'x': 50, 'y': 50}

            if GlobalVars.level == 3:
                GlobalVars.deregister([kitchen])
                kitchen = Kitchen(5, 3)
                kitchen.setup_level_three()
                player.kitchen = kitchen

                GlobalVars.deregister(cooks)

            if GlobalVars.level == 4:
                GlobalVars.deregister([kitchen])
                kitchen = Kitchen(7, 5)
                kitchen.setup_level_four()

                GlobalVars.deregister(cooks)

def get_window_size():
    return 800, 600  # TODO

def get_max_fps():
    return 60  # TODO

if __name__ == '__main__':
    run_game()