import random, copy

from pygame import Vector2

from Move import Move

class Brain:

    VARYING = 0.2 # 20%
    MAX_STEP = 5

    def __init__(self, nb_moves):
        self.movepool = []
        # self.movement_speed = 5
        self.movement_speed_vari = self.MAX_STEP * self.VARYING
        self.nb_moves = nb_moves
        for i in range(0, self.nb_moves):
            self.movepool.append(self.create_move())

    def set_move_score(self, move_object):
        '''Compute and stores the score for the given move'''
        if move_object.move_number > 0:
            move_object.move_score = self.compute_move_score(move_object)
        move_object.vector = self.movepool[move_object.move_number].vector
        self.movepool[move_object.move_number] = move_object

    def compute_move_score(self, move_object):
        '''Compare different data to output a move score'''
        #TODO: Make actual use of the move_score
        # move_object.isflagged = True if move_object.iskilling_move else False
        move_score = 1000 if not move_object.iswinning_move else 0
        move_object.isflagged = True if move_object.distance_to_win_initial < move_object.distance_to_win_final else False
        return move_score

    def create_move(self):
        random_x = random.uniform(-self.MAX_STEP, self.MAX_STEP)
        random_y = random.uniform(-self.MAX_STEP, self.MAX_STEP)
        return Move(vector=Vector2(random_x, random_y))

    def add_moves(self, step_nb_moves):
        for i in range(step_nb_moves):
            self.movepool.append(self.create_move())

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
            randome_value = random.randint(1, 4)
            if randome_value == 1:
                move.vector.x += random.uniform(0, self.movement_speed_vari)
            elif randome_value == 2:
                move.vector.x -= random.uniform(0, self.movement_speed_vari)
            elif randome_value == 3:
                move.vector.y += random.uniform(0, self.movement_speed_vari)
            elif randome_value == 4:
                move.vector.y -= random.uniform(0, self.movement_speed_vari)
        brain_clone = copy.deepcopy(self)
        brain_clone.movepool = movepool_clone
        return brain_clone

    def copy(self):
        '''Returns a deep copy of the instance'''
        return copy.deepcopy(self)