import pygame
import time
class Timer:
    def __init__(self, font, position):
        self.font = font
        self.position = position
        self.start_time = pygame.time.get_ticks() // 1000  # Record the start time
        self.start=15
        self.final = 0 

    def get_elapsed_time(self, point):
        print(self.start_time)
        self.start_time += point 
        current_time = (pygame.time.get_ticks() // 1000) - self.start_time
        self.final = (current_time - self.start_time)    
        print(self.final) 

    def display(self, screen):
        elapsed_time = self.final 
        timer_text = self.font.render(f'Time: {self.start - self.final  } seconds', True, (255, 255, 255))
        screen.blit(timer_text, self.position)


   # #Loop do jogo
   # running = True
   # while running:
   #    #Eventos
   #    for event in pygame.event.get():
   #       if event.type == pygame.USEREVENT: 
   #          counter -= 1
   #          text = str(counter).rjust(3) if counter > 0 else 'boom!'
   #       if event.type == pygame.QUIT:
   #          running = False


   #    player_list.draw(window) #Desenhar personagem

   #    pygame.init()

   #    #Janela e fundo
   #    window_size = (1280, 720)
   #    window = pygame.display.set_mode(window_size)
      
   #    pygame.display.set_caption("Planeta Kids")
   #    background = pygame.image.load(os.path.join("Arquivos", "FundoGame.jpg"))
   #    background = pygame.transform.scale(background, (1280, 720))
   #    window.blit(background, (0,0))

   #    clock = pygame.time.Clock()
   #    clock.tick(60)

   #    #Criar Personagem
   #    player = Player()   # spawn player
   #    player.rect.x = 0   # go to x
   #    player.rect.y = 0   # go to y
   #    player_list = pygame.sprite.Group()
   #    player_list.add(player)

      # trash = Trash(window_size[0], window_size[1])
      # trash_list = pygame.sprite.Group()
      # trash_list.add(trash)    

      #Loop do jogo