import random

from Dot import Dot
from Brain import Brain

class Population:

    PASSING_PERCENT = 5 # Percentage of players which will pass their "genes"

    def __init__(self, winning_area, nb_players=100, color=(255, 0, 0), screen=None, nb_turns=10): # RED
        self.nb_players = nb_players
        self.players = []
        self.passing_number = int(nb_players * self.PASSING_PERCENT / 100)
        self.players_color = color
        self.screen = screen
        self.winning_area = winning_area
        for i in range(0, self.nb_players):
            self.players.append(Dot(Brain(nb_moves=nb_turns), winning_area, color=self.players_color, screen=screen))

    def change_players_direction(self):
        for player in self.players:
            player.change_direction()

    def next_generation(self):
        passing_players = []
        self._sort_players_by_fitness()
        best_players = self.players[:self.passing_number]
        for i in range(0, self.nb_players):
            brain = best_players[random.randint(0, len(best_players) - 1)].brain.mutate()
            passing_players.append(Dot(brain=brain, winning_area=self.winning_area, color=self.players_color, screen=self.screen))
        self.players = passing_players

    def play_players_turn(self, screen_width, screen_height):
        for player in self.players:
            player.move()
            if player.x > screen_width - 5 or player.x < 0:
                player.bounce(0)
            if player.y > screen_height - 5 or player.y < 0:
                player.bounce(1)
            player.check_win()

    def draw_players(self):
        for player in self.players:
            player.draw()

    def _sort_players_by_fitness(self):
        self._score_players()
        self.players.sort(key=lambda player: player.fitness_score, reverse=True)

    def _score_players(self):
        for player in self.players:
            player.score()