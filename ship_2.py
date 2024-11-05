import pygame.image


class Ship_2:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/space_ship.png')
        self.rect = self.image.get_rect()

        # self.rect.center = self.screen_rect.center
        self.rect.bottomleft = self.screen_rect.bottomleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)
