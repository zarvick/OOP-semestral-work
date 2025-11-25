import pygame
import sys

# inicializace pygame
pygame.init()

screen = pygame.display.set_mode((1280,720)) # creates window for the game

running_program = True

# main loop to keep the program running
while running_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pokud klikneme na X zastaví chod programu
            running_program = False    


pygame.quit()
sys.exit()
