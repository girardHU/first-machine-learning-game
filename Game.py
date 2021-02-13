import time, random, argparse
from pprint import pprint

import pygame

from Player import Player
from Population import Population
from WinningArea import WinningArea
from Level import Level

class Game:

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, width=1000, height=1000, nb_players=50, nb_moves=5, nb_new_moves=5, gap_new_moves=5, player_radius=5, starting_level=0, tickrate=1000):
        self.width = width
        self.height = height
        self.nb_players = nb_players
        self.starting_nb_moves = nb_moves
        self.current_nb_moves = nb_moves
        self.nb_new_moves = nb_new_moves
        self.gap_new_moves = gap_new_moves
        self.player_radius = player_radius
        self.current_level = starting_level

        self.tickrate = tickrate
        self.size = None
        self.screen = None
        self.done = None
        self.clock = None

    def setup(self):
        '''All the setup code'''
        pygame.init()
        pygame.font.init()
        self.comicsansms_font = pygame.font.SysFont('Comic Sans MS', 30)
        # Set the width and height of the screen [width, height]
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption("My Game")
        # Loop until the user clicks the close button.
        self.done = False
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        self.MOVETICK = pygame.USEREVENT + 1

        pygame.time.set_timer(self.MOVETICK, self.tickrate) # fired once every second by default
        self.winning_area = WinningArea((400, 950, 200, 50), screen=self.screen)
        self.population = Population(winning_area=self.winning_area, nb_players=self.nb_players, nb_moves=self.starting_nb_moves, player_radius=self.player_radius, screen=self.screen)
        self.level = Level(level_nb=self.current_level, screen=self.screen)

    def draw_game(self, nbplayerssurface, levelsurface, gensurface, turnsurface):
        '''All the drawing code'''
        self.level.draw_obstacles()
        self.winning_area.draw()
        self.population.draw_players()
        self.screen.blit(nbplayerssurface, (1, 0))
        self.screen.blit(levelsurface, (1, 20))
        self.screen.blit(gensurface, (1, 40))
        self.screen.blit(turnsurface, (1, 60))

    def play(self):
        '''Main Function, with main event loop'''

        gen_counter = 1
        turn_counter = 1
        hasincreased = False

        # -------- Main Program Loop -----------
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == self.MOVETICK:
                    self.population.increment_players_current_move()
                    turn_counter += 1

            # --- Game logic should go here
            if turn_counter - 1 >= self.current_nb_moves or self.population.check_all_players_won_or_died():
                self.population.next_generation()
                turn_counter = 1
                gen_counter += 1
                hasincreased = False

            if gen_counter > 1 and not hasincreased and gen_counter % self.gap_new_moves == 0:
                self.population.incr_nb_moves(self.nb_new_moves)
                self.current_nb_moves += self.nb_new_moves
                hasincreased = True

            nbplayerssurface = self.comicsansms_font.render(f'NB Players {self.nb_players}', False, (0, 0, 0)) # surface used to display Generations
            levelsurface = self.comicsansms_font.render(f'Level {self.current_level}', False, (0, 0, 0)) # surface used to display Generations
            gensurface = self.comicsansms_font.render(f'Gen {gen_counter}', False, (0, 0, 0)) # surface used to display Generations
            turnsurface = self.comicsansms_font.render(f'Move {turn_counter}/{self.current_nb_moves}', False, (0, 0, 0)) # surface used to display Turns

            if self.population.check_all_players_have_been_drawn():
                self.population.play_players_turn(self.width, self.height, self.level)

            # --- Screen-clearing code goes here
            # Here, we clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
        
            # If you want a background image, replace this clear with blit'ing the
            # background image.
            self.screen.fill(self.WHITE)
        
            # --- Drawing code should go here
            self.draw_game(nbplayerssurface, levelsurface, gensurface, turnsurface)
        
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()

if __name__ == '__main__':
    #TODO: add more argument support
    parser = argparse.ArgumentParser(description='Run the Machine Learning IA on the game.')
    parser.add_argument('--level', type=int, nargs='?', default=0, help='The Level to start with.')
    parser.add_argument('--nb-players', type=int, nargs='?', default=50, help='The Number of players.')
    parser.add_argument('--player-radius', type=int, nargs='?', default=5, help='The Radius of Players.')
    parser.add_argument('--nb-moves', type=int, nargs='?', default=5, help='The Number of moves of the first generations.')
    parser.add_argument('--nb-new-moves', type=int, nargs='?', default=5, help='The Number by which you want to increase the size of the movepool.')
    parser.add_argument('--gap-new-moves', type=int, nargs='?', default=5, help='The Number of generation between two nb moves increases.')
    parser.add_argument('--tickrate', type=int, nargs='?', default=1000, help='The rate of the move tick (in milliseconds)')
    # parser.add_argument('--width', type=int, nargs='?', help='The Width of the Screen')
    # parser.add_argument('--height', type=int, nargs='?', help='The Height of the Screen')

    args = parser.parse_args()

    # WIDTH = args.width if args.width else 1000
    # HEIGHT = args.height if args.height else 1000
    LEVEL = args.level
    NB_PLAYERS = args.nb_players
    NB_TURNS = args.nb_moves
    NB_NEW_MOVES = args.nb_new_moves
    GAP_NEW_MOVES = args.gap_new_moves
    PLAYER_RADIUS = args.player_radius
    TICKRATE = args.tickrate

    game = Game(nb_players=NB_PLAYERS, nb_moves=NB_TURNS, nb_new_moves=NB_NEW_MOVES, gap_new_moves=GAP_NEW_MOVES, player_radius=PLAYER_RADIUS, starting_level=LEVEL, tickrate=TICKRATE)
    game.setup()
    game.play()