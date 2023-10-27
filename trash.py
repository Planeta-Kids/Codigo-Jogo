import random
import pygame
import os
import time

class Trash(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.lixo = ["peixe", "rad", "remedio", "seringa"]
        self.i = 0
        self.controlPont = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.respawn()

    def respawn(self):
        original = pygame.image.load(os.path.join('Arquivos/lixos', self.lixo[self.i] + '.png')).convert_alpha()
        self.image = pygame.transform.scale(original, (200, 200))
        self.rect = self.image.get_rect()
        arrayX = [200, 400, 500, 650, 750, 850, 1000, 50, 500, 710, 1000, 150, 350, 800, 50, 460, 650, 200, 400, 710, 850, 50, 500, 710, 200, 200, 400, 430, 650]
        arrayY = [0, 0, -50, 0, 0, 0, -50, 110, 100, 110, 110, 140, 160, 160, 230, 200, 220, 300, 300, 300, 300, 390, 390, 390, 420, 500, 500, 530, 550]
        aleatorio = random.randint(0, 28)
        self.rect.x = arrayX[aleatorio]
        self.rect.y = arrayY[aleatorio]
        self.visible = True
        self.spawn_time = time.time()
        self.i = (self.i + 1) % len(self.lixo)

    def update(self):
        if self.visible and time.time() - self.spawn_time >= 6:
            self.controlPont = 0
            self.visible = False
            self.respawn()
    