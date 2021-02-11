import random

from Dot import Dot
from Brain import Brain

class Population:

    PASSING_PERCENT = 5 # Percentage of players which will pass their "genes"
    PLAYER_COLOR = (220, 20, 60) # Player Color
    BEST_PLAYER_COLOR = (139, 0, 0) # Player Color

    def __init__(self, screen, winning_area, nb_players=100, color=PLAYER_COLOR, nb_turns=10): # RED
        self.nb_players = nb_players
        self.players = []
        self.passing_number = int(nb_players * self.PASSING_PERCENT / 100)
        self.players_color = color
        self.screen = screen
        self.winning_area = winning_area
        self.gen_best_brain = None

        for i in range(0, self.nb_players):
            self.players.append(Dot(Brain(nb_moves=nb_turns), winning_area, color=self.players_color, screen=screen))

    def change_players_direction(self):
        for player in self.players:
            player.change_direction()

    def next_generation(self):
        passing_players = []
        self._sort_players_by_fitness() # sort players by best fitness score
        self.gen_best_brain = self.players[0].brain.copy()
        best_players = self.players[:self.passing_number]
        for i in range(0, self.nb_players - 1):
            brain = best_players[random.randint(0, len(best_players) - 1)].brain.mutate()
            passing_players.append(Dot(brain=brain, winning_area=self.winning_area, color=self.players_color, screen=self.screen))
        passing_players.append(Dot(brain=self.gen_best_brain, winning_area=self.winning_area, color=self.BEST_PLAYER_COLOR, screen=self.screen)) # Create last Gen best player
        self.players = passing_players

    def play_players_turn(self, screen_width, screen_height, level):
        for player in self.players:
            player.move()
            # print(player.sprite)
            for obstacle in level.obstacles: # Die over obstacles
                if player.sprite is not None and player.sprite.colliderect(obstacle):
                    # print('TOUCHER')
                    player.died = True
            if player.x > screen_width - 5 or player.x < 0:
                player.bounce(0)
            if player.y > screen_height - 5 or player.y < 0:
                player.bounce(1)
            player.check_win()

    def draw_players(self):
        for player in self.players:
            player.draw()

    def check_all_players_have_been_drawn(self):
        for player in self.players:
            if player.sprite is None:
                return False
        return True

    def check_all_players_won_or_died(self):
        for player in self.players:
            if player.died is False or player.won is False:
                return False
        return True

    def _sort_players_by_fitness(self):
        self._score_players()
        self.players.sort(key=lambda player: player.fitness_score, reverse=True)

    def _score_players(self):
        for player in self.players:
            player.score()