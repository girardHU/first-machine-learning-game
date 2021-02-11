import pygame

class Level:

    # COLOR = (139, 0, 139) # Obstacle Color
    COLOR = (65, 105, 225) # Obstacle Color

    def __init__(self, screen, level_nb=0, color_obstacle=COLOR): # Blue
        self.level_nb = level_nb
        self.color_obstacle = color_obstacle
        self.screen = screen
        self.obstacles = []

    def draw_obstacles(self):
        self.obstacles = []
        if self.level_nb == 1:
            self.obstacles.append(pygame.draw.rect(self.screen, self.color_obstacle, (750, 400, 500, 25)))
            self.obstacles.append(pygame.draw.rect(self.screen, self.color_obstacle, (400, 750, 500, 25)))