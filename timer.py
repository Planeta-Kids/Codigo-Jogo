import pygame
import time
class Timer:

    def __init__(self, font, position, time):
        self.font = font
        self.position = position
        self.time = time
        self.finish_time = False
        self.punctuation = 0


    def get_elapsed_time(self, point):
        self.time += point 
        self.punctuation += point

    def get_punctuation(self):
        return self.punctuation

    def display(self, screen):
        if (self.finish_time) :
            timer_text = self.font.render('ACABOU O TEMPO', True, (255, 255, 255))
            print('acabou');
        else :
            seconds = self.time % 60
            minutes = int(self.time / 60) % 60
                # hours = int(x / 3600)
                # print(f"Time: {hours:02}: {minutes: 02} : {seconds:02}")
            # print('minutos: ', minutes)
            # print('segundos: ', seconds)
            timer_text = self.font.render(f'Time: {minutes : 02} : {seconds : 02}', True, (255, 255, 255))

            screen.blit(timer_text, self.position)  
            pygame.display.update()

            if (seconds == 0 and minutes == 0):
                self.finish_time = True
            else: 
                print("OPAAAA")
                self.time -= 1

                print("Tempo: ", self.time)
        return self.finish_time
   