import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('Arquivos', 'pixil-frame-0.png')).convert_alpha()
        self.size = img.get_size()
        self.smaller = pygame.transform.scale(img, (int(self.size[0]*0.15), int(self.size[1]*0.15)))
        self.images.append(self.smaller)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

     
    def update(self, keys, screen_width, screen_height):        
        if keys[pygame.K_LEFT]:
            self.rect.x -= 3
            if self.rect.right < 0:
                self.rect.left = screen_width
        if keys[pygame.K_RIGHT]:
            self.rect.x += 3
            if self.rect.left > screen_width:
                self.rect.right = 0
        if keys[pygame.K_UP]:
            self.rect.y -= 3
            if self.rect.bottom < 0:
                self.rect.top = screen_height
        if keys[pygame.K_DOWN]:
            self.rect.y += 3
            if self.rect.top > screen_height:
                self.rect.bottom = 0

