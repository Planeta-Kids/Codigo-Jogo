import pygame
import time
class Pontuation:
    def __init__(self, font, position):
        self.font = font
        self.position = position
        self.points = 0 

    def get_point(self):
        self.points += 4 

    def display(self, screen):         
        timer_text = self.font.render(f'Pontuação: {self.points} ', True, (255, 255, 255))
        screen.blit(timer_text, self.position)


   