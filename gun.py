import pygame
from pygame.sprite import Sprite

class Gun(Sprite):

    def __init__(self,screen):
        """Инициализация пушки."""
        super(Gun,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False


    def output(self):
        """Отрисовка пушки."""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Oбновление позиции пушки."""
        if self.mright and self.rect.right < self.screen_rect.right:
            # Перемещаем по координате х вправо на 1 пиксель.
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            # Перемещаем по координате х влево на 1 пиксель.
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        """Размещение пушки внизу по центру экрана."""
        self.center = self.screen_rect.centerx

