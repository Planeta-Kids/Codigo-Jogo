import pygame
import time
class Timer:
    def __init__(self, font, position):
        self.font = font
        self.position = position
        self.start_time = pygame.time.get_ticks() // 1000  # Record the start time
        self.start = 15
        self.final = 0 

    def get_elapsed_time(self, point):        
        self.start_time += point 
        current_time = (pygame.time.get_ticks() // 1000) - self.start_time
        self.final = (current_time - self.start_time)            
            
    def display(self, screen):
        timer_text = self.font.render(f'Time: {self.start - self.final} seconds', True, (255, 255, 255))
        screen.blit(timer_text, self.position)


   