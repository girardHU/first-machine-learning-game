import time, random, argparse
from pprint import pprint

import pygame

from Dot import Dot
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

    def __init__(self, width=1000, height=1000, nb_players=50, nb_turns=5, starting_level=0):
        self.width = width
        self.height = height
        self.nb_players = nb_players
        self.nb_turns = nb_turns
        self.current_level = starting_level

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
        self.turn_counter = 1
        self.gen_counter = 1

        pygame.time.set_timer(self.MOVETICK, 1000) # fired once every second
        self.winning_area = WinningArea((400, 950, 200, 50), screen=self.screen)
        self.population = Population(winning_area=self.winning_area, nb_players=self.nb_players, screen=self.screen)
        self.level = Level(level_nb=self.current_level, screen=self.screen)

    def draw_game(self, turnsurface, gensurface, levelsurface):
        '''All the drawing code'''
        self.level.draw_obstacles()
        self.winning_area.draw()
        self.population.draw_players()
        self.screen.blit(gensurface, (1, 0))
        self.screen.blit(turnsurface, (1, 20))
        self.screen.blit(levelsurface, (1, 40))

    def play(self):
        '''Main Function, with main event loop'''
        # -------- Main Program Loop -----------
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == self.MOVETICK:
                    self.population.change_players_direction()
                    self.turn_counter += 1
        
            # --- Game logic should go here
            if self.turn_counter >= self.nb_turns + 1 or self.population.check_all_players_won_or_died():
                self.population.next_generation()
                self.turn_counter = 1
                self.gen_counter += 1

            turnsurface = self.comicsansms_font.render(f'Turn {self.turn_counter}/{self.nb_turns}', False, (0, 0, 0)) # surface used to display Turns
            gensurface = self.comicsansms_font.render(f'Gen {self.gen_counter}', False, (0, 0, 0)) # surface used to display Generations
            levelsurface = self.comicsansms_font.render(f'Level {self.current_level}', False, (0, 0, 0)) # surface used to display Generations

            if self.population.check_all_players_have_been_drawn():
                self.population.play_players_turn(self.width, self.height, self.level)

            # --- Screen-clearing code goes here
            # Here, we clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
        
            # If you want a background image, replace this clear with blit'ing the
            # background image.
            self.screen.fill(self.WHITE)
        
            # --- Drawing code should go here
            self.draw_game(turnsurface, gensurface, levelsurface)
        
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()

if __name__ == '__main__':
    #TODO: add more argument support
    parser = argparse.ArgumentParser(description='Run the Machine Learning IA on the game.')
    parser.add_argument('--level', type=int, nargs='?', help='The Level to start with.')
    # parser.add_argument('--width', type=int, nargs='?', help='The Width of the Screen')
    # parser.add_argument('--height', type=int, nargs='?', help='The Height of the Screen')

    args = parser.parse_args()

    # WIDTH = args.width if args.width else 1000
    # HEIGHT = args.height if args.height else 1000
    LEVEL = args.level if args.level else 0

    game = Game(starting_level=LEVEL)
    game.setup()
    game.play()