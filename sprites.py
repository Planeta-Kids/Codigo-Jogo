import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.img = pygame.image.load(os.path.join('Arquivos', 'pixil-frame-0.png')).convert_alpha()
        self.size = self.img.get_size()
        self.smaller = pygame.transform.scale(self.img, (int(self.size[0] * 0.15), int(self.size[1] * 0.15)))
        self.images.append(self.smaller)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

     
    def update(self, keys, screen_width, screen_height):     
        if keys[pygame.K_LEFT]:

    def update(self, keys, screen_width, screen_height, col):
        # print("EIXO X: ", self.rect.x)   
        # print("EIXO Y: ", self.rect.y)  
        if keys[pygame.K_LEFT] and not col == "left":
            self.rect.x -= 6
            if self.rect.right < 0:
                self.rect.left = screen_width
                
        if keys[pygame.K_RIGHT] and not col == "right":
            self.rect.x += 6
            if self.rect.left > screen_width:
                self.rect.right = 0

        if keys[pygame.K_UP] and not col == "up":
            self.rect.y -= 6
            if self.rect.bottom < 0:
                self.rect.top = screen_height

        if keys[pygame.K_DOWN] and not col == "down":
            self.rect.y += 6
            if self.rect.top > screen_height:
                self.rect.bottom = 0



