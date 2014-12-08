import pygame
import sys
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
    kitchen.setup_level(current_level)

    player = Player(start_x=2, start_y=2, kitchen=kitchen)
    GlobalVars.register_game_obj(player)
    GlobalVars.player = player

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

        player.update()

        DISPLAY_SURFACE.fill((155, 180, 200))

        kitchen.render(screen=DISPLAY_SURFACE)
        player.render(screen=DISPLAY_SURFACE)

        GlobalVars.render(screen=DISPLAY_SURFACE)

        pygame.display.update()
        FpsClock.tick(FPS)


def get_window_size():
    return 800, 600  # TODO

def get_max_fps():
    return 60  # TODO

if __name__ == '__main__':
    run_game()