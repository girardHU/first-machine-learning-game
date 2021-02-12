import math, random, copy

import pygame

from Brain import Brain
from Move import Move
from Utils import normalize_vector

from pprint import pprint

class Player:

    SPEED = 3

    def __init__(self, brain, winning_area, screen, x=500.0, y=50.0, radius=5, color=(255, 0, 0)):
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
        '''Draw the current dot'''
        if self.screen is not None:
            self.sprite = pygame.draw.ellipse(self.screen, self.color, (self.x, self.y, self.radius, self.radius))

    def change_direction(self):
        '''Pass to the next move in the brain's movelist'''
        # self.score()
        if not self.won and not self.died:
            if self.current_move < self.max_move:
                self.current_move += 1

    def move(self): #TODO: add only one by one to better collision
        '''Move by the value corresponding to the current_move in the brain's movelist'''
        if not self.won and not self.died:
            # pprint(vars(self.brain.movepool[self.current_move]))
            if self.brain.movepool[self.current_move].vector is not None:
                new_x, new_y = normalize_vector((self.x + self.brain.movepool[self.current_move].vector.x) - self.x, (self.y + self.brain.movepool[self.current_move].vector.y) - self.y)
                self.x += (new_x * self.SPEED)
                self.y += (new_y * self.SPEED)

    #TODO: Fix bouncing -> need to keep brain.movepool as it was before
    # def bounce(self, axis):
    #     '''Change the direction in the given axis (x or y)'''
    #     if not self.won and not self.died:
    #         self.brain.movepool[self.current_move].vector[axis] *= -1

    def check_win(self):
        '''update the won variable if there is a collision with the Winning Area'''
        if self.winning_area is not None and self.sprite is not None:
            self.won = True if self.sprite.colliderect(self.winning_area) else False
            return self.won

    def score(self):
        #TODO: check if at the end of each move, the fitness score is better
        if self.sprite is not None:
            if self.won:
                self.fitness_score = 20000 / (self.current_move ** 2)
            else:
                dist_to_win = self.get_distance_to_goal()
                if self.died:
                    dist_to_win *= 1.3 # May require some tweaking
                    # dist_to_win *= 2.5 # May require some tweaking
                self.fitness_score = 10000 / dist_to_win
            # self.fitness_score += 1000
            # print(self.fitness_score)

    # def score(self):
    #     '''IMPORTANT : function actually scoring the player'''
    #     #TODO: check if at the end of each move, the fitness score is better
    #     if self.sprite is not None:

    #         if self.won: # Calculate the fitness score by nb of turns took to reach
    #             self.fitness_score = 1.0/ (10000.0 / (self.current_move ** 2))
    #             self.fitness_score += 0.5
    #         else:
    #             dist_to_win = self.get_distance_to_goal()
    #             if self.died:
    #                 dist_to_win *= 0.9
    #             self.fitness_score = 1.0/(dist_to_win ** 2)
    #         self.fitness_score *= self.fitness_score

    def reset(self):
        self.x = 500
        self.y = 50
        self.current_move = 0

        self.fitness_score = None
        self.won = False
        self.died = False

    def get_distance_to_goal(self):
        '''get the distance to the Winning Area'''
        if self.sprite is not None: # Get Distance to the closest angle
            dist_to_bottomleft = math.hypot(self.sprite.centerx - self.winning_area.sprite.bottomleft[0], self.sprite.centery - self.winning_area.sprite.bottomleft[1])
            dist_to_bottomright = math.hypot(self.sprite.centerx - self.winning_area.sprite.bottomright[0], self.sprite.centery - self.winning_area.sprite.bottomright[1])
            dist_to_topleft = math.hypot(self.sprite.centerx - self.winning_area.sprite.topleft[0], self.sprite.centery - self.winning_area.sprite.topleft[1])
            dist_to_topright = math.hypot(self.sprite.centerx - self.winning_area.sprite.topright[0], self.sprite.centery - self.winning_area.sprite.topright[1])
            lst = [dist_to_bottomleft, dist_to_bottomright, dist_to_topleft, dist_to_topright]
            lst.sort()
            return lst[0]