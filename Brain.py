import random, copy

from pygame import Vector2

class Brain:

    VARYING = 0.3 # 30%
    MAX_STEP = 1.0 # has to be one (vector normalization)
    SPEED_VARY = MAX_STEP * VARYING

    def __init__(self, nb_moves):
        self.movepool = []
        # self.movement_speed_vari = self.MAX_STEP * self.VARYING
        self.nb_moves = nb_moves
        for i in range(0, self.nb_moves):
            self.movepool.append(self.create_random_vector())

    def set_move_object(self, move_object):
        '''Compute and stores the score for the given move'''
        move_object.vector = self.movepool[move_object.move_number].vector
        self.movepool[move_object.move_number] = move_object

    def create_random_vector(self):
        '''Create a random pygame.Vector2 between (-1, -1) and (1, 1)'''
        random_x = random.uniform(-1, 1)
        random_y = random.uniform(-1, 1)
        while random_x == 0 and random_y == 0:
            random_x = random.uniform(-1, 1)
            random_y = random.uniform(-1, 1)
        return Vector2(random_x, random_y)

    def add_moves(self, amount_to_add):
        '''Increase the number of moves periodically'''
        for i in range(amount_to_add):
            self.movepool.append(self.create_random_vector())

    def mutate(self):
        '''return the slightly mutated copy of the instance'''
        cloned_mp = copy.deepcopy(self.movepool)
        for index, move in enumerate(cloned_mp):
            randomeval1 = random.randint(1, 4)
            #TODO: maybe add full random move only on the n last moves (to not fuck up incremental learning)
            # randomeval2 = random.randint(1, 10)
            if randomeval1 == 1:
                move.x += random.uniform(0, self.SPEED_VARY)
            if randomeval1 == 2:
                move.x -= random.uniform(0, self.SPEED_VARY)
            if randomeval1 == 3:
                move.y += random.uniform(0, self.SPEED_VARY)
            if randomeval1 == 4:
                move.y -= random.uniform(0, self.SPEED_VARY)
            # if randomeval2 == 10:
            #     move.vector = self.create_random_vector()
        cloned_brain = self.copy()
        cloned_brain.movepool = cloned_mp
        return cloned_brain

    def copy(self):
        '''Returns a deep copy of the instance'''
        return copy.deepcopy(self)