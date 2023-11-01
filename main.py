import os
import pygame
import time
import math
import button

from sprites import Player
from trash import Trash  
from timer import Timer
from screens import Screens


def main():
    pygame.init()

    # Janela e fundo
    window_size = (1280, 720)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Planeta Kids")

    # Cria cronometro   
    font = pygame.font.Font(None, 36)
    timer = Timer(font, (10, 10), 4000)     

    clock = pygame.time.Clock()
    clock.tick(60)

    # Cria personagem
    player = Player()   # spawn player
    player.rect.x = 605 # go to x
    player.rect.y = 415 # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    # Cria lixo
    trash = Trash(window_size[0], window_size[1])
    trash_list = pygame.sprite.Group()
    trash_list.add(trash)

    #Carrega os botões
    start_img = pygame.image.load('Arquivos/BotaoVoltar.png').convert_alpha()
    exit_img = pygame.image.load('Arquivos/BotaoProximo.png').convert_alpha()

    running = True
    acabouTempo = False
    trocou = False
    pontuacao = 0

    while running:
        if acabouTempo == False:

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            background = pygame.image.load(os.path.join("Arquivos", "FundoGame.jpg"))
            background = pygame.transform.scale(background, (1280, 720))
            window.blit(background, (0, 0))

            # Obtenha as teclas pressionadas
            keys = pygame.key.get_pressed()

            player.update(keys, window_size[0], window_size[1])

            player_position = (player.rect.x, player.rect.y)         
            trash_position = ((trash.rect.x + 70),( trash.rect.y + 10) )
            
            dist = distance(player_position, trash_position)

            if dist < 18:
                timer.get_elapsed_time(2)
                trash.respawn() 
            else:
                timer.get_elapsed_time(0) 
            window.blit(background, (0, 0)) 
            player_list.draw(window)  

            if trash.visible:
                trash.update()
                trash_list.draw(window)

            timer.display(window)
            pygame.display.flip()       
            finish_time = timer.display(window)

            if finish_time:
                trocou = False
                acabouTempo = True 
                pontuacao = timer.get_punctuation()      

            clock.tick(120)   

            pygame.display.flip()

        else:


            start_button = button.Button(30, 600, start_img, 1)
            exit_button = button.Button(1050, 600, exit_img, 1)


            if start_button.draw(window):
                print('START')
                timer = Timer(font, (10, 10), 4000) 
                acabouTempo = False
                        
            if exit_button.draw(window): 
                running = False
                print('EXIT')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen = Screens()
            timer_text = font.render('MENU INICIAL', True, (255, 255, 255))
            
            if (trocou == False):
                screen.changeBackground(window=window, player_list=player_list, text=timer_text, nameBackground="FundoMain.jpg")

                screen.displayPunctuation(window=window, text=timer_text, punctuation=pontuacao)
                trocou = True

            clock.tick(120)     

            pygame.display.flip()
       
    # Fecha o jogo após loop terminar
    pygame.quit()

def distance(point1, point2):    
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

if __name__ == '__main__':
    main()
