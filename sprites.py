import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        self.imgFront = pygame.image.load(os.path.join('Arquivos/personagem/', 'Frente.png')).convert_alpha()
        self.imgBack = pygame.image.load(os.path.join('Arquivos/personagem/', 'Atras.png')).convert_alpha()
        self.imgLeft = pygame.image.load(os.path.join('Arquivos/personagem/', 'Esquerda.png')).convert_alpha()
        self.imgRight = pygame.image.load(os.path.join('Arquivos/personagem/', 'Direita.png')).convert_alpha()

        self.size = self.imgFront.get_size()
        self.smaller1 = pygame.transform.scale(self.imgFront, (int(self.size[0] * 0.50), int(self.size[1] * 0.50)))

        self.size = self.imgBack.get_size()
        self.smaller2 = pygame.transform.scale(self.imgBack, (int(self.size[0] * 0.50), int(self.size[1] * 0.50)))

        self.size = self.imgLeft.get_size()
        self.smaller3 = pygame.transform.scale(self.imgLeft, (int(self.size[0] * 0.50), int(self.size[1] * 0.50)))

        self.size = self.imgRight.get_size()
        self.smaller4 = pygame.transform.scale(self.imgRight, (int(self.size[0] * 0.50), int(self.size[1] * 0.50)))

        self.images.append(self.smaller1)
        self.images.append(self.smaller2)
        self.images.append(self.smaller3)
        self.images.append(self.smaller4)

        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def update(self, keys, screen_width, screen_height, col): 
        if keys[pygame.K_LEFT] and not col == "left":
            self.image = self.images[2]
            self.rect.x -= 6
            if self.rect.right < 0:
                self.rect.left = screen_width
                
        if keys[pygame.K_RIGHT] and not col == "right":
            self.image = self.images[3]
            self.rect.x += 6
            if self.rect.left > screen_width:
                self.rect.right = 0

        if keys[pygame.K_UP] and not col == "up":
            self.image = self.images[1]
            self.rect.y -= 6
            if self.rect.bottom < 0:
                self.rect.top = screen_height

        if keys[pygame.K_DOWN] and not col == "down":
            self.image = self.images[0]
            self.rect.y += 6
            if self.rect.top > screen_height:
                self.rect.bottom = 0