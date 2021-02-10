import random, copy

from pygame import Vector2

class Brain:

    def __init__(self, nb_moves=100):
        self.move_pool = []
        for i in range(0, nb_moves):
            self.nb_moves = nb_moves
            self.move_pool.append(Vector2(random.uniform(-5., 5.), random.uniform(-5., 5.)))

    def mutate(self):
        for i in range(0, self.nb_moves):
            randome_value = random.randint(1, 20)
            if randome_value == 5:
                if self.move_pool[i].x < -1 or self.move_pool[i].x > 0:
                    self.move_pool[i].x += 1
                else:
                    self.move_pool[i].x -= 1
            elif randome_value == 10:
                if self.move_pool[i].x > 1 or self.move_pool[i].x < 0:
                    self.move_pool[i].x -= 1
                else:
                    self.move_pool[i].x += 1
            elif randome_value == 15:
                if self.move_pool[i].y < -1 or self.move_pool[i].y > 0:
                    self.move_pool[i].y += 1
                else:
                    self.move_pool[i].y -= 1
            elif randome_value == 20:
                if self.move_pool[i].y > 1 or self.move_pool[i].y < 0:
                    self.move_pool[i].y -= 1
                else:
                    self.move_pool[i].y += 1
        return copy.deepcopy(self)