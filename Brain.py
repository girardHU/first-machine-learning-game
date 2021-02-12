import random, copy

from pygame import Vector2

from Move import Move

class Brain:

    VARYING = 0.3 # 30%
    MAX_STEP = 1.0

    def __init__(self, nb_moves):
        self.movepool = []
        # self.movement_speed = self.MAX_STEP
        self.movement_speed_vari = self.MAX_STEP * self.VARYING
        self.nb_moves = nb_moves
        for i in range(0, self.nb_moves):
            self.movepool.append(Move(vector=self.create_random_vector()))

    def set_move_object(self, move_object):
        '''Compute and stores the score for the given move'''
        move_object.vector = self.movepool[move_object.move_number].vector
        self.movepool[move_object.move_number] = move_object

    def create_random_vector(self):
        random_x = random.uniform(-1, 1)
        random_y = random.uniform(-1, 1)
        while random_x == 0 and random_y == 0:
            random_x = random.uniform(-1, 1)
            random_y = random.uniform(-1, 1)
        # random_x = random.uniform(-self.MAX_STEP, self.MAX_STEP)
        # random_y = random.uniform(-self.MAX_STEP, self.MAX_STEP)
        return Vector2(random_x, random_y)

    def add_moves(self, step_nb_moves):
        for i in range(step_nb_moves):
            self.movepool.append(Move(vector=self.create_random_vector()))

    def mutate(self):
        '''return the slightly mutated copy of the instance'''
        movepool_clone = copy.deepcopy(self.movepool)
        for index, move in enumerate(movepool_clone):
            # if index > 0 and (move.isflagged or move.iskilling_move): # Check if the move have been flagged or is killing the dot
            # if index > 0 and move.iskilling_move: # Check if the move is killing the dot
            #     random_x = random.uniform(-self.MAX_STEP, self.MAX_STEP)
            #     random_y = random.uniform(-self.MAX_STEP, self.MAX_STEP)
            #     move.vector = Vector2(random_x, random_y)
            # else:
            randomeval1 = random.randint(1, 4)
            # randomeval2 = random.randint(1, 10)
            if randomeval1 == 1:
                move.vector.x += random.uniform(0, self.movement_speed_vari)
            if randomeval1 == 2:
                move.vector.x -= random.uniform(0, self.movement_speed_vari)
            if randomeval1 == 3:
                move.vector.y += random.uniform(0, self.movement_speed_vari)
            if randomeval1 == 4:
                move.vector.y -= random.uniform(0, self.movement_speed_vari)
            # if randomeval2 == 10:
            #     move.vector = self.create_random_vector()
                
        brain_clone = copy.deepcopy(self)
        brain_clone.movepool = movepool_clone
        return brain_clone

    def copy(self):
        '''Returns a deep copy of the instance'''
        return copy.deepcopy(self)