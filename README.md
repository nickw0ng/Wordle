# Wordle by Nicholas Wong

This is a Wordle game implemented using Pygame. The objective of the game is to guess the correct 5-letter word within six attempts. After each guess, the color of the tiles will change to show how close your guess was to the word.

## Setup and Installation

### Prerequisites

- Python 3.x
- Pygame library

## Game Explanation

### Constants
- WIDTH, HEIGHT: Dimensions of the game window.
- SCREEN: The Pygame display surface.
- BACKGROUND: The background image of the game.
- ICON: The icon image for the game window.
  
### Colors
- GREEN: Indicates a correct letter in the correct position.
- YELLOW: Indicates a correct letter in the wrong position.
- GRAY: Indicates an incorrect letter.
- OUTLINE, GUESSED_OUTLINE: Colors for the box outlines.

### Fonts
- GUESSED_LETTER_FONT: Font for guessed letters.
- AVAILABLE_LETTER_FONT: Font for the letters on the keyboard indicators.
- 
### Game State Variables
- guesses_count: Tracks the number of guesses made.
- guesses: Stores the list of guesses.
- current_guess: Current guess being typed by the player.
- current_guess_string: String representation of the current guess.
- indicators: List of keyboard indicators.
- game_result: State of the game ("W" for win, "L" for lose, or empty for in-progress).

## Classes

### Letter: 
Represents a single letter in a guess.

Attributes:
- text: The letter.
- bg_color: Background color of the letter box.
- text_color: Color of the text.
- bg_position, bg_rect: Position and size of the letter box.
- text_position, text_surface, text_rect: Position and rendering of the text.

Methods:
- draw(): Draws the letter on the screen.
- delete(): Deletes the letter from the screen.
  
### Indicator
Represents a keyboard indicator for the on-screen keyboard.

Attributes:

- x, y: Position of the indicator.
- text: The letter displayed on the indicator.
- rect: Rectangle representing the indicator.
- bg_color: Background color of the indicator.

Methods:

- draw(): Draws the indicator on the screen.
  
## Functions
- check_guess(guess_to_check): Checks the current guess against the correct word and updates the colors accordingly.
- play_again(): Displays a message to play again and the correct word if the game is over.
- reset(): Resets the game state for a new game.
- create_new_letter(): Creates a new letter and adds it to the current guess.
- delete_letter(): Deletes the last letter from the current guess.
  
## Main Loop
The game runs in an infinite loop, checking for events such as quitting the game, pressing keys for guesses, backspace for deleting letters, and entering for submitting guesses or restarting the game.
