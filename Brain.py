import random, copy

from pygame import Vector2

from Move import Move
from MoveTags import *

class Brain:

    VARYING = 0.1 # 10%

    def __init__(self, nb_moves):
        self.move_pool = []
        self.movement_speed = 5
        self.movement_speed_vari = self.movement_speed * self.VARYING
        for i in range(0, nb_moves):
            self.nb_moves = nb_moves
            random_x = random.uniform(-self.movement_speed, self.movement_speed)
            random_y = random.uniform(-self.movement_speed, self.movement_speed)
            self.move_pool.append(Move(vector=Vector2(random_x, random_y)))

    def set_move_score(self, move_object):
        '''Compute and stores the score for the given move'''
        if move_object.move_number > 0:
            move_object.move_score = self.compute_move_score(move_object)
        move_object.vector = self.move_pool[move_object.move_number].vector
        self.move_pool[move_object.move_number] = move_object

    def compute_move_score(self, move_object):
        #TODO: Make actual use of the move_score
        '''Compare different data to output a move score'''
        # move_object.isflagged = True if move_object.iskilling_move else False
        move_score = 1000 if not move_object.iswinning_move else 0
        move_object.isflagged = True if move_object.distance_to_win_initial < move_object.distance_to_win_final else False
        return move_score

    def mutate(self):
        '''return the slightly mutated copy of the instance'''
        for index, move in enumerate(self.move_pool):
            if index > 0 and (move.isflagged or move.iskilling_move): # Check if the move have been flagged or is killing the dot
                random_x = random.uniform(-self.movement_speed, self.movement_speed)
                random_y = random.uniform(-self.movement_speed, self.movement_speed)
                move.vector = Vector2(random_x, random_y)
            else:
                randome_value = random.randint(1, 4)
                if randome_value == 1:
                    move.vector.x += random.uniform(0, self.movement_speed_vari)
                elif randome_value == 2:
                    move.vector.x -= random.uniform(0, self.movement_speed_vari)
                elif randome_value == 3:
                    move.vector.y += random.uniform(0, self.movement_speed_vari)
                elif randome_value == 4:
                    move.vector.y -= random.uniform(0, self.movement_speed_vari)
        return copy.deepcopy(self)

    def copy(self):
        '''Returns a deep copy of the instance'''
        return copy.deepcopy(self)