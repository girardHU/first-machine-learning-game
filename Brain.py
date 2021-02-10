import random, copy

from pygame import Vector2

class Brain:

    def __init__(self, nb_moves=100):
        self.move_pool = []
        self.movement_speed = 5
        self.movement_speed_vari = 5 * 10 / 100
        for i in range(0, nb_moves):
            self.nb_moves = nb_moves
            random_x = random.uniform(-self.movement_speed, self.movement_speed)
            random_y = random.uniform(-self.movement_speed, self.movement_speed)
            self.move_pool.append(Vector2(random_x, random_y))

    def mutate(self):
        for i in range(0, self.nb_moves):
            randome_value = random.randint(1, 4)
            if randome_value == 1:
                self.move_pool[i].x += random.uniform(0, self.movement_speed_vari)
            elif randome_value == 2:
                self.move_pool[i].x -= random.uniform(0, self.movement_speed_vari)
            elif randome_value == 3:
                self.move_pool[i].y += random.uniform(0, self.movement_speed_vari)
            elif randome_value == 4:
                self.move_pool[i].y -= random.uniform(0, self.movement_speed_vari)
        return copy.deepcopy(self)