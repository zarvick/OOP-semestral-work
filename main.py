# import of the library
import pygame
import sys

# import of game.py
import game
from game import game_4letter, game_5letter, game_6letter # imports the child classes from game.py

# initialization of pygame
pygame.init()

screen = pygame.display.set_mode((1280,720)) # creates window for the game
pygame.display.set_caption("Wordle Game Menu") # created window will have a name Wordle Game Menu

# variable which is used for running the while loop till something changes its state to False, basicaly keeps the program running
running_program = True

class Button():
    def __init__(self, text, color, height, width, x, y):
        self.text = text
        self.color = color
        self.shape = pygame.Rect(x, y, height, width) # creates a rectangle shape
        self.font = pygame.font.SysFont(None, 30)  # basic font with height of 30 points

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.shape) # draws the rectangle onto the screen buffer (will be visible after display.flip())

        # writes the text onto the surface of the rectangles
        text_surf = self.font.render(self.text, True, (255, 255, 255))  # color of the text
        text_rect = text_surf.get_rect(center=self.shape.center) # centers the text on the rectangle

        screen.blit(text_surf, text_rect) # draws the text surface onto the screen buffer (still not visible until display.flip())
        
    def clicked_button(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.shape.collidepoint(event.pos) # collidepoint checks if the click of a mouse was inside of the shape or not, if not than returns False

# creation of buttons
btn4 = Button("4 LETTER GAME", (50, 100, 200), 180, 50, (1280-180)/2, 200)
btn5 = Button("5 LETTER GAME", (50, 100, 200), 180, 50, (1280-180)/2, 300)
btn6 = Button("6 LETTER GAME", (50, 100, 200), 180, 50, (1280-180)/2, 400)

# main loop to keep the program running
while running_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if i click the X in the right corner the program will shutdown
            running_program = False  # the reason why program will shutdown

        if btn4.clicked_button(event):

            # just a tests right now to check if the buttons still work correctly
            print("Start 4-letter game")

            # starts the game of Wordle with target word with 4 letters
            game4 = game_4letter()
            game4.evaluate_guess()

        if btn5.clicked_button(event):

            # just a tests right now to check if the buttons still work correctly
            print("Start 5-letter game")

            # starts the game of Wordle with target word with 5 letters
            game5 = game_5letter()
            game5.evaluate_guess()

        if btn6.clicked_button(event):

            # just a tests right now to check if the buttons still work correctly
            print("Start 6-letter game")

            # starts the game of Wordle with target word with 6 letters
            game6 = game_6letter()
            game6.evaluate_guess()


    screen.fill((30,30,30)) # fills the screen with a color
    btn4.draw(screen)
    btn5.draw(screen)
    btn6.draw(screen)
    pygame.display.flip() # finally displays everything drawn in this frame


pygame.quit()
sys.exit()
