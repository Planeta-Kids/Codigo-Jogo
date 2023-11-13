import os
import pygame

from sprites import Player

class Screens:

    def __init__(self):
        self.controllPunctuation = [
            {'background': 'Arquivos/estrelas/0Estrelas.png',   'points': 14.3}, 
            {'background': 'Arquivos/estrelas/0.5Estrela.png',  'points': 28.6}, 
            {'background': 'Arquivos/estrelas/1Estrela.png',    'points': 42.9},
            {'background': 'Arquivos/estrelas/1.5Estrelas.png', 'points': 57.2},
            {'background': 'Arquivos/estrelas/2Estrelas.png',   'points': 71.5},
            {'background': 'Arquivos/estrelas/2.5Estrelas.png', 'points': 85.8},
            {'background': 'Arquivos/estrelas/3Estrelas.png',   'points': 100}
        ]

    def changeBackground(self, window, player_list, text, nameBackground):
        # Criar Personagem
        player = Player() # spawn player
        player_list = pygame.sprite.Group()
        player_list.add(player)

        window_size = (1280, 720)
        window = pygame.display.set_mode(window_size)
        
        backgroundUpdated = pygame.image.load(os.path.join("Arquivos", nameBackground))
        backgroundUpdated = pygame.transform.scale(backgroundUpdated, (1280, 720))

        player.rect.x = 605 # go to x
        player.rect.y = 415 # go to y

        window.blit(backgroundUpdated, (0, 0))
        pygame.display.update()
        window.blit(text, (560,100))  

        player_list.draw(window) 


    def changeTutorialScreen(self, window, nameBackground):
        window_size = (1280, 720)
        window = pygame.display.set_mode(window_size)
        
        backgroundUpdated = pygame.image.load(os.path.join("Arquivos/tutorial", nameBackground))
        backgroundUpdated = pygame.transform.scale(backgroundUpdated, (1280, 720))

        window.blit(backgroundUpdated, (0, 0))
        pygame.display.update()


    def displayPunctuation(self, window, text, punctuation):
        print("displayPunctuation")
        print("lista: ", self.controllPunctuation)
        percPunctuation = (punctuation * 100) / 100;
        print("porcentagem obtida: ", percPunctuation)
        for stars in self.controllPunctuation:
            print("Pontução da vez: ", stars.get('points'))
            if (percPunctuation < stars.get('points')):
                print("Qual estrela mostrar: ", stars.get('background'))

                displayStar = pygame.image.load(os.path.join(stars.get('background')))
                displayStar = pygame.transform.scale(displayStar, (400, 100))
                window.blit(displayStar, (450, 150))
                pygame.display.update()
                return
