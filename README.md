# OOP-semestral-work
A Wordle inspired game built with Python and Pygame.

## Project Description
This project is a Wordle inspired word-guessing game implemented in Python, with a graphical interface built using library Pygame. Players can select to play with 4, 5, or 6-letter words. The game provides immediate visual feedback on each guess in a grid same as original Wordle:
- Green – the letter is correct and in the correct position
- Yellow – the letter exists in the word but in a different position
- Grey – the letter does not appear in the word
The game enforces a limited number of attempts depending on the word length (4-letter: 5 attempts, 5-letter: 6 attempts, 6-letter: 7 attempts).

## Navigation
The project is separated into many files to separete structure of the game mechanics from the user interface, making the code easier to maintain, extend, and test. Project containes those files:
- main.py – Launches the Pygame interface and manages game interactions
- game.py – Implements game logic and evaluation methods
- test_wordle.py – Unit tests for the game logic
- wordlists/ - folder with 3 .txt files with words (4,5,6 letters long)

## Installation
To run the program and play game made in this project you will need to download these:
- pip install pygame
- pip install pytest

## Running the program
1. Run main.py to start the game.
2. A window with three buttons will appear for selecting the target word length. Click the desired button (4, 5, or 6 letters).
3. The game grid will appear, along with a MENU button in the corner.
4. Type your guesses using the keyboard. Letters will appear in the grid.
5. Press Enter to submit a guess. The game ends when:
   - YOU WON! THE WORD WAS:
   - YOU LOST! THE WORD WAS:
6. Click the MENU button to return to the word-length selection screen and start a new game. You can play multiple games without restarting the program.
