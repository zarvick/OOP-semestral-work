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

# when the program is started and player did not choose target word length
# used for vizualization from window with buttons to window with grid
selected_max_attempts = None
selected_word_length = None

# empty string for writing players guess
guess = ""


# empty parametr which will be filled after player chooses (clicks on one of the 3 buttons) game with word length
game_object = None # instance of child classes game4_letter, game5_letter, game6_letter,


class Button():
    def __init__(self, text, color, height, width, x, y):
        self.text = text
        self.color = color
        self.shape = pygame.Rect(x, y, height, width) # creates a rectangle shape
        self.font = pygame.font.SysFont(None, 30)  # basic font with height of 30 points

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.shape) # draws the rectangle onto the screen buffer (will be visible after display.flip())

        # writes the text onto the surface of the rectangles
        text_surf = self.font.render(self.text, True, (255, 255, 255))  # color of the text, white text
        text_rect = text_surf.get_rect(center=self.shape.center) # centers the text on the rectangle

        screen.blit(text_surf, text_rect) # draws the text surface onto the screen buffer (still not visible until display.flip())
        
    def clicked_button(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.shape.collidepoint(event.pos) # collidepoint checks if the click of a mouse was inside of the shape or not, if not than returns False

class WordleGameUI():
    def __init__(self, screen):
        self.screen = screen
        self.current_row = 0
        self.grid_letters = [] # list for letter of guess word
        self.grid_colors  = [] # list of colors which are evaluated after the guess word is send into grid
        self.guess = "" 
        self.game_object = None # instance of game class (4,5,6 letter)

    def start_game_grid(self, word_length, max_attempts):

        # store grid configuration so other methods can use it
        self.word_length = word_length
        self.max_attempts = max_attempts

        # create grid only if it's empty or size mismatch in rows or columns
        if not self.grid_letters or len(self.grid_letters) != max_attempts or len(self.grid_letters[0]) != word_length:
            # 2D lists: rows = max_attempts, cols = word_length
            # creates a grid depending on which target word length (game) was choosen
            self.grid_letters = [[""] * word_length for _ in range(max_attempts)] 
            self.grid_colors = [[""] * word_length for _ in range(max_attempts)]

        # implementation how the grid should look, position and size
        rect_size = 60
        padding = 10 # spaces between rectangles
        start_x = (1280 - (rect_size + padding) * word_length) // 2
        start_y = 100
        
        for row in range(max_attempts):
            for col in range(word_length):

                color = (200, 200, 200)  # default color, grey
                # set color based on evaluation
                if self.grid_colors[row][col] == "green": # if the index of this list is "green" than makes the rectangle of the grid green
                    color = (0, 255, 0) # green                    # works the same way for yellow and grey letter representations
                elif self.grid_colors[row][col] == "yellow":
                    color = (255, 255, 0) # yellow
                elif self.grid_colors[row][col] == "grey":
                    color = (100, 100, 100) # grey

                rect = pygame.Rect(
                    start_x + col * (rect_size + padding),
                    start_y + row * (rect_size + padding),
                    rect_size,
                    rect_size
                ) # creates a 60x60 rectangle which is copied till word_length is reached which is collum and than this is done till max_attempts are reached which represents rows
                pygame.draw.rect(self.screen, (200,200,200), rect, 3) # border
                pygame.draw.rect(self.screen, color, rect) # fill


                # fills the grid only if the player types a letter which makes the index of the list not empty -> letter will show up in grid
                # the letter will get centered and font, same thing as it was with buttons
                letter = self.grid_letters[row][col]
                if letter != "":
                    font = pygame.font.SysFont(None, 50)
                    text_surf = font.render(letter, True, (0,0,0))
                    text_rect = text_surf.get_rect(center=rect.center)
                    self.screen.blit(text_surf, text_rect)

    def handle_guess(self):

        # waits till the player chooses a game otherwise it would create an AtributeError
        if self.game_object is None:
            return

        checked = self.game_object.try_word(self.guess) # checks the players word for correct length compared to target word
        if checked is None:
            # wrong length, than checked is None and wont send it to handle_guess(), the word wont show in the grid
            return # the reason why it wont update the grid

        # get result of evaluation
        status, colors = self.game_object.evaluate_guess(checked)
        letters = self.game_object.split_words(checked)

        # update grid
        self.grid_letters[self.current_row] = letters
        self.grid_colors[self.current_row] = colors

        # move to next row and reset input
        self.current_row += 1
        self.guess = ""  # reset the input

        # prints result message after evaluation depending on the conditions
        if status == "win":
            print(f"YOU WON! THE WORD WAS: {self.game_object.random_word}")
        else:
            # check lose condition here based on current_row
            if self.current_row + 1 >= self.max_attempts:  # last attepmt
                status = "lose"
                print(f"YOU LOST! THE WORD WAS: {self.game_object.random_word}")

# creation of buttons
btn4 = Button("4 LETTER GAME", (50, 100, 200), 180, 50, (1280-180)/2, 200)
btn5 = Button("5 LETTER GAME", (50, 100, 200), 180, 50, (1280-180)/2, 300)
btn6 = Button("6 LETTER GAME", (50, 100, 200), 180, 50, (1280-180)/2, 400)

# creation of grid instance
grid = WordleGameUI(screen)


# main loop to keep the program running
while running_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if i click the X in the right corner the program will shutdown
            running_program = False  # the reason why program will shutdown

        if btn4.clicked_button(event): # if player clicks button with text "4 LETTER GAME" 

            # just a tests right now to check if the buttons still work correctly
            print("Start 4-letter game")

            # player can type only words with 4 letter and has 5 tries to guess target word
            selected_word_length = 4
            selected_max_attempts = 5

            # using methods from game.py
            game_object = game_4letter() # instance of child class game_4letter()
            game_object.choose_word() # generates the target word
            grid.game_object = game_object # this lets the instance grid of class WordleGameUI use methods of instance game_object
            grid.start_game_grid(selected_word_length, selected_max_attempts) # tells grid how big it will be (rows, columns)
            guess = ""
            print("Chosen:", game_object.random_word)

            # starts the game of Wordle with target word with 4 letters
            # game4 = game_4letter()
            # game4.evaluate_guess()

        if btn5.clicked_button(event): # if player clicks button with text "5 LETTER GAME" 

            # just a tests right now to check if the buttons still work correctly
            print("Start 5-letter game")

            # player can type only words with 5 letter and has 6 tries to guess target word
            selected_word_length = 5
            selected_max_attempts = 6

            # using methods from game.py
            game_object = game_5letter()
            game_object.choose_word()
            grid.game_object = game_object
            grid.start_game_grid(selected_word_length, selected_max_attempts)
            guess = ""
            print("Chosen:", game_object.random_word)

            # starts the game of Wordle with target word with 5 letters
            # game5 = game_5letter()
            # game5.evaluate_guess()

        if btn6.clicked_button(event): # if player clicks button with text "6 LETTER GAME" 

            # just a tests right now to check if the buttons still work correctly
            print("Start 6-letter game")

            # player can type only words with 6 letter and has 7 tries to guess target word
            selected_word_length = 6
            selected_max_attempts = 7

            # using methods from game.py
            game_object = game_6letter()
            game_object.choose_word()
            grid.game_object = game_object
            grid.start_game_grid(selected_word_length, selected_max_attempts)
            guess = ""
            print("Chosen:", game_object.random_word)

            # starts the game of Wordle with target word with 6 letters
            # game6 = game_6letter()
            # game6.evaluate_guess()


        # keyboard inputs
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                if len(grid.guess) > 0:
                    grid.guess = grid.guess[:-1] # pressing backspace deletes last letter
                    grid.grid_letters[grid.current_row][len(grid.guess)] = ""   # clear the last letter from the grid when Backspace is pressed
                                                                                # 'len(grid.guess)' points to the column of the letter being removed

            elif event.key == pygame.K_RETURN:
                grid.handle_guess() # pressing enter evaluates players guess

            else:    
                # check that we have active game (grid.game_object is not None), that pressed keys are only A-Z
                # and the player hasnt reached word_length yet
                if grid.game_object and event.unicode.isalpha() and len(grid.guess) < grid.game_object.word_length():
                    char = event.unicode.upper() # conversion to uppercase
                    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": # lets user only use A-Z letters
                        grid.guess += char # adds letter to current players guess
                    grid.grid_letters[grid.current_row][len(grid.guess)-1] = char # updates grid so that the written word will can show up


    screen.fill((30,30,30)) # fills the screen with a color, background

    if selected_word_length is None: # first the player needs to set a length of target word to move onto guessing grid
        btn4.draw(screen)
        btn5.draw(screen)
        btn6.draw(screen)
    else:
        grid.start_game_grid(selected_word_length, selected_max_attempts) # draws the grid

    pygame.display.flip() # finally displays everything drawn in this frame, updates the screen


pygame.quit()
sys.exit()
