import pygame
pygame.init()

class Main:
    def __init__(self, width, height, bgColor, caption):
        self.width = width
        self.height = height
        self.bgColor = bgColor
        self.caption = caption
        self.run = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    def setDisplay(self):
        pygame.display.set_caption(self.caption)

    def bgdisplay(self):
        self.screen.fill(self.bgColor)