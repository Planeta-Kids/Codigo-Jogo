import pygame
import time
class Timer:

    def __init__(self, font, position, time):
        self.font = font
        self.position = position
        self.time = time
        self.finish_time = False
        self.punctuation = 0
        print('Time passado: ', self.time)


    def get_elapsed_time(self, point):
        if (point > 0):
            print('Minutos Adicionados: ', point)
            self.time +=  point
            self.punctuation += 1

    def get_punctuation(self):
        return self.punctuation

    def display(self, screen):
        clock = pygame.time.Clock()

        if (self.finish_time) :
            timer_text = self.font.render('ACABOU O TEMPO', True, (255, 255, 255))
            print('ACABOU O TEMPO');
        else :
            mins, secs = divmod(self.time, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            clock.tick(120)

            timer_text = self.font.render(f'Time: {timer}', True, (255, 255, 255))

            screen.blit(timer_text, self.position)  
            pygame.display.update()

            if (mins == 0 and secs == 0):
                self.finish_time = True
            else: 
                self.time -= 1
        return self.finish_time
   