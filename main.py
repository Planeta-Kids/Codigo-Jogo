import os
import pygame

from sprites import Player
from colisao import Colisao
from rects import Rect

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

def main():
   pygame.init()
   pygame.font.init()

   #Janela e fundo
   window_size = (1280, 720)
   window = pygame.display.set_mode(window_size)
   pygame.display.set_caption("Planeta Kids")
   background = pygame.image.load(os.path.join("Arquivos", "FundoGame.jpg"))
   background = pygame.transform.scale(background, (1280, 720))
   window.blit(background, (0,0))

   #Travar fps em 60 
   clock = pygame.time.Clock()
   clock.tick(60)

   #Criar Personagem
   player = Player()
   player.rect.x = 605  # vai para x=0
   player.rect.y = 415  # vai para y=0
   player_list = pygame.sprite.Group()
   player_list.add(player)

   #Criar retangulos e colisão
   for i in range(len(coords)):
      x, y, width, height = coords[i]
      globals()["colis" + str(i)] = Rect(x, y, width, height)

   #Loop do jogo
   running = True
   while running:
      #Eventos
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False


      #Obtenha as teclas pressionadas
      keys = pygame.key.get_pressed()

      #Atualize o jogador com base nas teclas pressionadas
      

      window.blit(background, (0, 0))  #Desenhe o fundo novamente para limpar a tela
      player_list.draw(window)  #Desenhe o jogador
      pygame.display.flip()
      clock.tick(60)
      

      #Colisão com objetos
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
      #x, y = pygame.mouse.get_pos()
      #pos = myfont.render(f'x = {x} y = {y}', False, (0, 0, 0))
      #window.blit(pos, (990, 30))

      pygame.display.flip()
   
   #Fechar jogo após loop terminar
   pygame.quit()

if __name__ == '__main__':
   main()