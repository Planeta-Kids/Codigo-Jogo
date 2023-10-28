import pygame
import os
class Bin(pygame.sprite.Sprite):

    def __init__(self, lixeiro):
        pygame.sprite.Sprite.__init__(self)     
        original = pygame.image.load(os.path.join('Arquivos/lixeiros', lixeiro +'.png')).convert_alpha()
        self.image = pygame.transform.scale(original, (200, 200))
        self.rect = self.image.get_rect()
        
    def spawn(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.visible = True
