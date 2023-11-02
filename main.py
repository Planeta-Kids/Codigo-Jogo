import os
import pygame
import time
import math
import button

from sprites import Player
from colisao import Colisao
from rects import Rect
from trash import Trash  
from timer import Timer
from points import Pontuation
from bin import Bin
from screens import Screens


#coordenadas dos retangulos de colisão
coords = [
[65,60,215,80], 
[575,70,140,65],
[1010,75,200,60],

[100,335,170,50],
[560,325,170,60],
[1050,320,175,70],

[75,585,180,50],
[600,550,90,110],
[1000,585,210,65]
]

#iterador para colisão
i = range(8)
from screens import Screens


def main():
    pygame.init()

    # Janela e fundo
    window_size = (1280, 720)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Planeta Kids")
    background = pygame.image.load(os.path.join("Arquivos", "FundoGame.jpg"))
    background = pygame.transform.scale(background, (1280, 720))
    window.blit(background, (0, 0))

    # Cria cronometro   
    font = pygame.font.Font(None, 36)
    timer = Timer(font, (10, 10), 4000)     

    #instanciando pontuação
    pontuation = Pontuation(font, (1000,10))
    clock = pygame.time.Clock()
    clock.tick(60)


    #Criar retangulos e colisão
    for i in range(len(coords)):
        x, y, width, height = coords[i]
        globals()["colis" + str(i)] = Rect(x, y, width, height)
        print(i)

    player = Player()   # spawn player
    player.rect.x = 605   # go to x
    player.rect.y = 415   # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)


    #Obtenha as teclas pressionadas
    keys = pygame.key.get_pressed()

    #Atualize o jogador com base nas teclas pressionadas
    

    window.blit(background, (0, 0))  #Desenhe o fundo novamente para limpar a tela
    player_list.draw(window)  #Desenhe o jogador
    pygame.display.flip()
    clock.tick(60)
    
    #x, y = pygame.mouse.get_pos()
    #pos = myfont.render(f'x = {x} y = {y}', False, (0, 0, 0))
    #window.blit(pos, (990, 30))

    trash = Trash(window_size[0], window_size[1])
    trash_list = pygame.sprite.Group()    
    trash_list.add(trash)
    # Cria lixo
    trash = Trash(window_size[0], window_size[1])
    trash_list = pygame.sprite.Group()
    trash_list.add(trash)

    #Carrega os botões
    start_img = pygame.image.load('Arquivos/BotaoVoltar.png').convert_alpha()
    exit_img = pygame.image.load('Arquivos/BotaoProximo.png').convert_alpha()


    binContami = Bin("lixeiroContami")
    bin_list = pygame.sprite.Group()
    bin_list.add(binContami)

    binHosp = Bin("lixeiroHosp")
    bin_list.add(binHosp)


    binOrg = Bin("lixeiroOrg")
    bin_list.add(binOrg)

    binPlast = Bin("lixeiroPlast")
    bin_list.add(binPlast)

    binRad = Bin("lixeiroRad")
    bin_list.add(binRad)

    controlPont = 0
    tempo = time.time()
    lixo = ["garrafa", "maça", "pilha", "peixe", "rad", "seringa"]
    running = True

    x = 60
    y = 50

    acabouTempo = False
    trocou = False
    pontuacao = 0

    while running:
        if acabouTempo == False:
            i = trash.i

            #Eventos    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            background = pygame.image.load(os.path.join("Arquivos", "FundoGame.jpg"))
            background = pygame.transform.scale(background, (1280, 720))
            window.blit(background, (0, 0))

            keys = pygame.key.get_pressed()

            #colisão
            if player.rect.colliderect(colis0):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col0", player.rect, colis0.rect, 10))
            elif player.rect.colliderect(colis1):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col1", player.rect, colis1.rect, 10))
            elif player.rect.colliderect(colis2):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col2", player.rect, colis2.rect, 10))
            elif player.rect.colliderect(colis3):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col3", player.rect, colis3.rect, 10))
            elif player.rect.colliderect(colis4):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col4", player.rect, colis4.rect, 10))
            elif player.rect.colliderect(colis5):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col5", player.rect, colis5.rect, 10))
            elif player.rect.colliderect(colis6):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col6", player.rect, colis6.rect, 10))
            elif player.rect.colliderect(colis7):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col7", player.rect, colis7.rect, 10))
            elif player.rect.colliderect(colis8):
                player.update(keys, window_size[0], window_size[1], Colisao.zerarVel("col8", player.rect, colis8.rect, 10))
            else:
                player.update(keys, window_size[0], window_size[1], 0)
          
            if trash.controlPont == 1:
                trash.rect.x = player.rect.x
                trash.rect.y = player.rect.y

            binOrg_position     = ((binOrg.rect.x + x), (binOrg.rect.y + y))    
            binPlast_position   = ((binPlast.rect.x + x),(binPlast.rect.y + y))
            binRad_position     = ((binRad.rect.x + x),(binRad.rect.y + y))
            binContami_position = ((binContami.rect.x + x), (binContami.rect.y + y))
            binHosp_position    = ((binHosp.rect.x + x), (binHosp.rect.y + y))
            player_position     = (player.rect.x, player.rect.y)         
            trash_position      = ((trash.rect.x + 10), (trash.rect.y + 10))

            distPlTr   = distance(player_position, trash_position)
            distContam = distance(binContami_position, player_position)
            distHosp   = distance(binHosp_position, player_position)  
            distOrg    = distance(binOrg_position, player_position)  
            distPlast  = distance(binPlast_position, player_position)        
            distRad    = distance(binRad_position, player_position)  

            if distPlTr < 18 and trash.controlPont == 0:
                #pontuation gera um ponto, tem que mudar dps pra verificação se jogou no lixo, esse foi só pra teste 
                timer.get_elapsed_time(0)
                trash.controlPont = 1
                # tempo = time.time()
                trash.spawn_time = time.time()
            elif controlPont == 1 and (time.time() - trash.spawn_time  >= 6):
                trash.respawn()        
                controlPont = 0
                timer.get_elapsed_time(0)
            else:
                timer.get_elapsed_time(0)

            # if (dist < 18 or dist0 < 18) and controlPont == 1:
            #     tempo = time.time()
            #     pontuation.get_point() 
            #     trash.respawn()
            #     controlPont = 0
            #     timer.get_elapsed_time(2)

            if (distContam < 18) and (lixo[i-1] == "pilha"):
                trash.spawn_time = time.time()
                pontuation.get_point()        
                trash.respawn()
                trash.controlPont = 0
                timer.get_elapsed_time(2)

            if (distHosp < 18) and (lixo[i-1]== "seringa"):
                trash.spawn_time = time.time()
                pontuation.get_point() 
                trash.respawn()
                trash.controlPont = 0
                timer.get_elapsed_time(2)

            if (distOrg < 18) and ((lixo[i-1]== "peixe") or (lixo[i-1]== "maça")):            
                trash.spawn_time = time.time()
                pontuation.get_point() 
                trash.controlPont = 0
                trash.respawn()
                timer.get_elapsed_time(2)

            if (distPlast < 18) and (lixo[i-1]== "garrafa"):
                trash.spawn_time = time.time()
                pontuation.get_point() 
                trash.controlPont = 0
                trash.respawn()
                timer.get_elapsed_time(2)

            if (distRad < 18) and (lixo[i-1]== "rad"):
                trash.spawn_time = time.time()
                pontuation.get_point() 
                trash.controlPont = 0
                trash.respawn()
                timer.get_elapsed_time(2)

            window.blit(background, (0, 0))  #Desenhe o fundo novamente para limpar a tela
            
            binHosp.spawn(840, -50)    
            binContami.spawn(265, 0)
            binRad.spawn(710, 230)
            binOrg.spawn(10, 310)
            binPlast.spawn(450, 500)

            bin_list.draw(window)
            player_list.draw(window) 
            pontuation.display(window)
            trash.update()
            trash_list.draw(window)
            timer.display(window)
            pygame.display.flip()       

            clock.tick(60)        
            # timer.display(window)
            # pygame.display.flip()       
            finish_time = timer.display(window)

            if finish_time:
                trocou = False
                acabouTempo = True 
                pontuacao = timer.get_punctuation()      
                window.blit(background, (0, 0))  #Desenhe o fundo novamente para limpar a tela

            clock.tick(60)   

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
