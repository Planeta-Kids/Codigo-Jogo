import os
import pygame

from sprites import Player

class Screens:

    def __init__(self):
        self.controllPunctuation = [
            {'background': '0Estrelas.png',   'points': 0},
            {'background': '0.5Estrelas.png', 'points': 5},
            {'background': '1Estrela.png',    'points': 10},
            {'background': '1.5Estrelas.png', 'points': 15},
            {'background': '2Estrelas.png',   'points': 20},    
            {'background': '2.5Estrelas.png', 'points': 25},    
            {'background': '3Estrelas.png',   'points': 30}
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


    def displayPunctuation(self, window, text, punctuation):
        print("displayPunctuation")
        print("lista: ", self.controllPunctuation)


        for stars in self.controllPunctuation:
            print("Pontução da vez: ", stars.get('points'))
            if (punctuation == stars.get('points')):
                print("Qual estrela mostrar: ", stars.get('background'))

                displayStar = pygame.image.load(os.path.join("Arquivos", stars.get('background')))
                displayStar = pygame.transform.scale(displayStar, (400, 100))
                window.blit(displayStar, (450, 150))
                pygame.display.update()
                return
