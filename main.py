import os
import pygame

from sprites import Player


def main():
   pygame.init()

   #Janela e fundo
   window_size = (1200, 700)
   window = pygame.display.set_mode(window_size)
   
   pygame.display.set_caption("Planeta Kids")
   background = pygame.image.load(os.path.join("Arquivos", "FundoGame.jpg"))
   background = pygame.transform.scale(background, (1280, 720))
   window.blit(background, (0,0))

   clock = pygame.time.Clock()
   clock.tick(60)

   #Criar Personagem
   player = Player()   # spawn player
   player.rect.x = 0   # go to x
   player.rect.y = 0   # go to y
   player_list = pygame.sprite.Group()
   player_list.add(player)


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
      player.update(keys, window_size[0], window_size[1])

      window.blit(background, (0, 0))  #Desenhe o fundo novamente para limpar a tela
      player_list.draw(window)  #Desenhe o jogador
      pygame.display.flip()
      clock.tick(60)
      


      pygame.display.flip()
   
   #Fechar jogo após loop terminar
   pygame.quit()

if __name__ == '__main__':
   main()