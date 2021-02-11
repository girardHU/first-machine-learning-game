import pygame

class WinningArea:

    COLOR = (46, 139, 87)

    def __init__(self, rect, screen, color=COLOR):
        self.rect = rect
        self.color = color
        self. screen = screen

    def draw(self):
        '''Draw the Winning Area'''
        if self.screen is not None:
            self.sprite = pygame.draw.rect(self.screen, self.color, self.rect)
