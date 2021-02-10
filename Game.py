"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""

from pprint import pprint
import time

import pygame

from Dot import Dot
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH = 1000
HEIGHT = 1000

NB_TURNS = 100
NB_PLAYERS = 5
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

MOVETICK = pygame.USEREVENT + 1

pygame.time.set_timer(MOVETICK, 1000) # fired once every second

dots_list = []
winning_zone = None

for i in range(0, NB_PLAYERS):
    dots_list.append(Dot(color=RED, screen=screen))
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == MOVETICK:
            for i in range(0, NB_PLAYERS):
                dots_list[i].change_direction(winning_zone)
            print()
 
    # --- Game logic should go here
    for i in range(0, NB_PLAYERS):
        dots_list[i].move()
        if winning_zone is not None:
            dots_list[i].is_winning(winning_zone)

    # Bounce the ball if needed
    for i in range(0, NB_PLAYERS):
        if dots_list[i].x > WIDTH - 5 or dots_list[i].x < 0:
            dots_list[i].bounce(0)
        if dots_list[i].y > HEIGHT - 5 or dots_list[i].y < 0:
            dots_list[i].bounce(1)

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    winning_zone = pygame.draw.rect(screen, GREEN, (400, 950, 200, 50))
    for i in range(0, NB_PLAYERS):
        dots_list[i].draw()
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()