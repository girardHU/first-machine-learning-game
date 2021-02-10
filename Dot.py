import math

import pygame

from Brain import Brain

class Dot:

    def __init__(self, brain, winning_area, x=500, y=50, radius=10, color=(255, 255, 255), screen=None):
        self.x = x
        self.y = y
        self.brain = brain
        self.sprite = None
        self.current_move = 0
        self.max_move = 100
        self.radius = radius
        self.color = color
        self.screen = screen
        self.winning_area = winning_area

        self.fitness_score = None
        self.won = False
        self.died = False

    def draw(self):
        if self.screen is not None:
            self.sprite = pygame.draw.ellipse(self.screen, self.color, (self.x, self.y, self.radius, self.radius))

    def change_direction(self):
        # self.score()
        if not self.won and not self.died:
            if self.current_move < self.max_move:
                self.current_move += 1

    def move(self):
        if not self.won and not self.died:
            self.x += self.brain.move_pool[self.current_move].x
            self.y += self.brain.move_pool[self.current_move].y

    def bounce(self, axis):
        if not self.won and not self.died:
            self.brain.move_pool[self.current_move][axis] *= -1

    def check_win(self):
        if self.winning_area is not None and self.sprite is not None:
            self.won = self.sprite.colliderect(self.winning_area)

    def score(self):
        #TODO: check if at the end of each move, the fitness score is better
        if self.sprite is not None:
            dist_to_win = math.hypot(self.sprite.centerx - self.winning_area.centerx, self.sprite.centery - self.winning_area.centery)
            sqrt_nb_steps = self.current_move ** 3
            won_bonus = 0 if self.won else 1000
            fitness_score = 1 / (dist_to_win + sqrt_nb_steps + won_bonus)
            self.fitness_score = fitness_score
            # print('dist_to_win', dist_to_win)
            # print('sqrt_nb_steps', sqrt_nb_steps)
            # print('won_bonus', won_bonus)
            # print('fitness_score', fitness_score)
            # print()