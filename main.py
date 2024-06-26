import pygame
import sys
import random
from words import WORDS
pygame.init()

# Constants for the board
WIDTH, HEIGHT = 316, 450
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("wordle-game/assets/StartingTiles.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH // 1.6, HEIGHT // 1.6))
BACKGROUND_RECT = BACKGROUND.get_rect(center=(158, 155))
ICON = pygame.image.load("wordle-game/assets/LetterIcon.png") 

pygame.display.set_caption("Wordle by Nicholas Wong")
pygame.display.set_icon(ICON)

# Creating the colors to be used for the leters
GREEN = "#00FF00"
YELLOW = "#FFFF00"
GRAY = "#B2BEB5"
OUTLINE = "#d3d6da"
GUESSED_OUTLINE = "#878a8c"

# example correct word
CORRECT_WORD = "flame"

# all the letters on a keyboard to be used for inputing guesses
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

# creating the font and sizes of the letters on the screen
GUESSED_LETTER_FONT = pygame.font.Font("wordle-game/assets/TextFont.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("wordle-game/assets/TextFont.otf", 15)

# setting the play scrren and the background
SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

LETTER_SIZE = 75 
LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12


guesses_count = 0
guesses = [[]] * 6
current_guess, current_guess_string, current_letter_bg_x = [], "", 62
indicators, game_result = [], ""

 # the state of the game could be a win, lose, or in progress
game_result = ""

# Class that represent the letters thats going to be displayed on the screen
class Letter:
    # initializing variables
    def __init__(self, text, bg_position):
        # Initializes all the variables, 
        # text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x+36, self.bg_position[1]+34)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)
    
     # creating a method to draw the playing screen and make changes
    def draw(self):
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        # checks that if the space is unguessed there is an outline for the box
        if self.bg_color == "white" :
            pygame.draw.rect(SCREEN, GUESSED_OUTLINE, 3)
   
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update
    
    # creating a method to delete a letter that was typed
    def delete(self):
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
        pygame.display.update()
        
        
class Indicator:
    
    def __init__(self, x, y, letter):
        self.x, self.y = x, y
        self.text = letter
        self.rect = (self.x, self.y, 27, 50)
        self.bg_color = OUTLINE

    # This method draws the indicator on the screen
    def draw(self):
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+15, self.y+30))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

# initial indicator postition
indicator_x, indicator_y = 25, 300

for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 27
    indicator_y += 50
    if i == 0:
        indicator_x = 38
    elif i == 1:
        indicator_x = 65

def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in CORRECT_WORD:
            if lowercase_letter == CORRECT_WORD[i]:
                guess_to_check[i].bg_color = GREEN
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = "grey"
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = "grey"
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()
    
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110
    
    if guesses_count == 6 and game_result == "":
        game_result = "L"
        
def play_again():
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("wordle-game/assets/TextFont.otf", 50)
    play_again_text = play_again_font.render("Press ENTER to play again!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
    word_was_text = play_again_font.render(f"The word was {CORRECT_WORD}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 650))    
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()
    
def reset():
    # Resets all global variables to their default states.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    CORRECT_WORD = random.choice(WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()

def create_new_letter():
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()
            
def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING


# running the game
while True:
    if game_result != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                        check_guess(current_guess)
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()


