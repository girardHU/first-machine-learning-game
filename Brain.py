import random

from pygame import Vector2

class Brain:

    def __init__(self, nb_moves=100):
        self.move_pool = []
        for i in range(0, nb_moves):
            self.move_pool.append(Vector2(random.uniform(-10., 10.), random.uniform(-10., 10.)))