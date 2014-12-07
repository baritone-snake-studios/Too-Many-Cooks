import os
import pygame
from too_many_cooks.globals import GlobalVars


class Player(object):
    def __init__(self):
        super().__init__()
        self.scale = GlobalVars.scale * .1
        image = pygame.image.load(os.path.join('sprites', 'player.png'))
        self.image = pygame.transform.scale(image,
                                            (int(image.get_width() * self.scale),
                                            int(image.get_height() * self.scale)))
        self.current_tile = None
        self.vel_x = 0.0
        self.vel_y = 0.0

<<<<<<< HEAD
    def render(self, screen):
        screen.blit(self.image, (1, 5))
=======
    def refresh_scale(self):
        raise NotImplementedError
>>>>>>> origin/master
