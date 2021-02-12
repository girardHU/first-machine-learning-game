import random

import time

from Player import Player
from Move import Move
from Brain import Brain

from pprint import pprint

class Population:

    PASSING_PERCENT = 0.1 # Percentage of players which will pass their "genes"
    PLAYER_COLOR = (220, 20, 60) # Player Color
    BEST_PLAYER_COLOR = (0, 255, 0) # Player Color
    # BEST_PLAYER_COLOR = (139, 0, 0) # Player Color

    def __init__(self, screen, winning_area, nb_players, nb_moves, player_radius=5, color=PLAYER_COLOR):
        self.nb_players = nb_players
        self.players = []
        self.passing_number = int(nb_players * self.PASSING_PERCENT)
        if self.passing_number < 1:
            self.passing_number = 1
        self.players_color = color
        self.screen = screen
        self.winning_area = winning_area

        for i in range(0, self.nb_players):
            self.players.append(Player(Brain(nb_moves=nb_moves), winning_area, radius=player_radius, color=self.players_color, screen=screen))

    def change_players_direction(self):
        '''Function which changes all players directions'''
        for player in self.players:
            player.change_direction()

    def next_generation(self):
        '''Function which handle the generation swaping (n to n+1)'''
        passing_players = []
        self._sort_players_by_fitness() # sort players by best fitness score
        best_players = self.players[:self.passing_number]
        for i in range(0, self.nb_players - 1):
            ceil = len(best_players) - 1
            if ceil >= 1:
                brain = best_players[random.randint(0, len(best_players) - 1)].brain.mutate()
            else:
                brain = best_players[0].brain.mutate()
            passing_players.append(Player(brain=brain, winning_area=self.winning_area, color=self.players_color, screen=self.screen))
        passing_players.append(Player(brain=best_players[0].brain.copy(), winning_area=self.winning_area, color=self.BEST_PLAYER_COLOR, screen=self.screen)) # Create last Gen best player
        print('best score: ', best_players[0].fitness_score)
        self.players = passing_players

    def play_players_turn(self, screen_width, screen_height, level):
        '''Play each player turn (compute death and bouncing of edges)'''
        for player in self.players:
            if not player.died and not player.won:
                move = Move(player.get_distance_to_goal())
                player.move()
                move.distance_to_win_final = player.get_distance_to_goal()
                # print(player.sprite)
                for obstacle in level.obstacles: # Die over obstacles
                    if player.sprite is not None and player.sprite.colliderect(obstacle):
                        # print('TOUCHER')
                        player.died = True
                        move.iskilling_move = True
                if player.x > screen_width - 5 or player.x < 0:
                    player.died = True
                    move.iskilling_move = True
                    # player.bounce(0)
                    # move.isbouncing_move = True
                if player.y > screen_height - 5 or player.y < 0:
                    player.died = True
                    move.iskilling_move = True
                    # player.bounce(1)
                    # move.isbouncing_move = True
                move.iswinning_move = player.check_win()
                player.score_move(move)

    def draw_players(self):
        '''Draw each player by calling their draw method'''
        for player in self.players:
            player.draw()

    def check_all_players_have_been_drawn(self):
        '''Check if all players have a sprite object'''
        for player in self.players:
            if player.sprite is None:
                return False
        return True

    def check_all_players_won_or_died(self):
        '''Check if at least one player is still playing (not dead or winning)'''
        for player in self.players:
            if player.died is False and player.won is False:
                return False
        return True

    def incr_nb_moves(self, step_nb_moves):
        for player in self.players:
            player.brain.add_moves(step_nb_moves)

    def _sort_players_by_fitness(self):
        '''sort players by their fitness score, in descending order'''
        self._score_players()
        self.players.sort(key=lambda player: player.fitness_score, reverse=True)

    def _score_players(self):
        '''Score each player'''
        for player in self.players:
            player.score()
        print()