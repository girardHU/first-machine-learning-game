import math

import pygame

from Brain import Brain

class Dot:

    def __init__(self, x=500, y=50, radius=5, color=(255, 255, 255), screen=None):
        self.x = x
        self.y = y
        self.brain = Brain(nb_moves=100)
        self.sprite = None
        self.current_move = 0
        self.max_move = 100
        self.radius = radius
        self.color = color
        self.screen = screen

        self.fitness_score = None
        self.won = False
        self.died = False

    def draw(self):
        if self.screen:
            # pygame.draw.ellipse(self.screen, self.color, (self.x, self.y, 10, 10))
            self.sprite = pygame.draw.ellipse(self.screen, self.color, (self.x, self.y, self.radius, self.radius))
            return
        raise ValueError('no screen passed to instance')

    def change_direction(self, winning_zone):
        self.compute_fitness(winning_zone)
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

    def is_winning(self, winning_zone):
        self.won = self.sprite.colliderect(winning_zone)

    def compute_fitness(self, winning_zone=None):
        if winning_zone is not None:
            dist_to_win = math.hypot(self.sprite.centerx - winning_zone.centerx, self.sprite.centery - winning_zone.centery)
            sqrt_nb_steps = self.current_move ** 3
            won_bonus = 0 if self.won else 1000
            fitness_score = 1 / (dist_to_win + sqrt_nb_steps + won_bonus)
            self.fitness_score = fitness_score
            # print('dist_to_win', dist_to_win)
            # print('sqrt_nb_steps', sqrt_nb_steps)
            # print('won_bonus', won_bonus)
            # print('fitness_score', fitness_score)
            # print()