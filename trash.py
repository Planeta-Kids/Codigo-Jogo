import random
import pygame
import os
import time

class Trash(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)        
        original = pygame.image.load(os.path.join('Arquivos', 'peixeL.png')).convert_alpha()
        self.image = pygame.transform.scale(original, (200, 200))
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.respawn()

    def respawn(self):
        arrayX = [200, 400, 500, 650, 750, 850, 1000, 50, 500, 710, 1000, 150, 350, 800, 50, 460, 650, 200, 400, 710, 850, 50, 500, 710, 200, 200, 400, 430, 650]
        arrayY = [0,0, -50, 0, 0, 0, -50, 110, 100, 110, 110, 140, 160, 160, 230, 200, 220, 300, 300, 300, 300, 390, 390, 390, 420, 500, 500, 530, 550]
        # aleatorio = self.rand()
        aleatorio = random.randint(0, 28)        
        self.rect.x = arrayX[aleatorio]
        self.rect.y = arrayY[aleatorio]        
        # self.rect.x = 400
        # self.rect.y = -50
        self.visible = True
        self.spawn_time = time.time()

    # def rand(self):
    # 	global x
    # 	aleatorio = random.randint(0, 28)
    # 	if(aleatorio == x):
    # 		return rand()
    # 	x = aleatorio
    # 	return aleatorio

    def update(self):
        if self.visible and time.time() - self.spawn_time >= 6:
            self.visible = False
            self.respawn()
        