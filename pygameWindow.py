#Creating class for pygame window
import pygame
from constants import pygameWindowWidth
from constants import pygameWindowDepth

class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((pygameWindowWidth, pygameWindowDepth))

    def Prepare(self):
        pygame.event.get()
        self.screen.fill((255,255,255))

    def Draw_Black_Circle(self, x, y):
        pygame.draw.circle(self.screen, (0,0,0), (x, y), 14)
        
        

    def Reveal(self):
        pygame.display.update()
