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


      player_list.draw(window) #Desenhar personagem
      


      pygame.display.flip()
   
   #Fechar jogo após loop terminar
   pygame.quit()

if __name__ == '__main__':
   main()