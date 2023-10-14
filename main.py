import os
import pygame
import time
import math
from sprites import Player
from trash import Trash  
from timer import Timer

def main():
    pygame.init()

    # Janela e fundo
    window_size = (1200, 700)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Planeta Kids")
    background = pygame.image.load(os.path.join("Arquivos", "FundoGame.jpg"))
    background = pygame.transform.scale(background, (1280, 720))
    window.blit(background, (0, 0))

    # setting timer    
    font = pygame.font.Font(None, 36)
    timer = Timer(font, (10, 10))     

    clock = pygame.time.Clock()
    clock.tick(60)

    # Criar Personagem
    player = Player()   # spawn player
    player.rect.x = 0   # go to x
    player.rect.y = 0   # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    trash = Trash(window_size[0], window_size[1])
    trash_list = pygame.sprite.Group()
    trash_list.add(trash)  

    running = True
    while running:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Obtenha as teclas pressionadas
        keys = pygame.key.get_pressed()

        player.update(keys, window_size[0], window_size[1])

        player_position = (player.rect.x, player.rect.y)         
        trash_position = ((trash.rect.x + 70),( trash.rect.y + 10) )
        #debugging
        # print("player position")
        # print(player_position)
        # print("trash position")
        # print(trash_position)
        dist = distance(player_position, trash_position)


        # Se a distância for menor que um valor (ajustar conforme necessário)
        if dist < 18:
            #nao sei pq caralhos ele dobra o numero que coloca aqui pra ir a mais no timer
            timer.get_elapsed_time(2)
            print("Lixo capturado!")
            trash.respawn() 
        else:
            print("entrou no else")
            timer.get_elapsed_time(0) 
        window.blit(background, (0, 0))  # Desenhe o fundo novamente para limpar a tela
        player_list.draw(window)  # Desenhe o jogador
        if trash.visible:
            trash.update()
            trash_list.draw(window)
        
        timer.display(window)
        pygame.display.flip()       

        clock.tick(60)   

        pygame.display.flip()

    # Fechar jogo após loop terminar
    pygame.quit()

def distance(point1, point2):    
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

if __name__ == '__main__':
    main()
