import pygame
import random
import sys

# from replit import audio
from pygame.locals import *



# Initialize Pygame
pygame.init()

# Load your MP3 file
# def play_audio():
# try:
# audio.play_file("background_music1.mp3")
# except Exception as e:
# print(f"Error while playing audio: {e}")

# Intializing the global variables
best_guess = 0
username = 0
password = 0
coin_count = 0
change_database = False
coin_added = False
game_ended = False

# Set up the display
width, height = 633, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("5 Words - login")
ICON = pygame.image.load("5words_icon.png")
pygame.display.set_icon(ICON)
# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load a decoration image
image_path = "5words.png"
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (600, 175))


# Font settings
font = pygame.font.Font(None, 36)


def update_window_caption(coin_count):
    pygame.display.set_caption(f"5 Words    Coins: {coin_count}")
    pygame.display.update()


# Load words from a text file
def read_words_from_file(file_name):
    with open(file_name, "r") as file:
        words = file.readlines()
    return [word.strip() for word in words]


word_list = read_words_from_file("wordlist.txt")

# Function to validate credentials from a text file
def validate_credentials(username, password):
    global best_guess, username1, password1, coin_count
    with open("database.txt", "r") as file:
        users = file.readlines()
    user_pass = [user.strip().split(",") for user in users]
    for user in user_pass:
        if user[0] == username and user[1] == password:
            best_guess = int(user[2])
            coin_count = int(user[3])
            username1 = username
            password1 = password
            return True
    return False


def wordle_game(username, password):
    print(f"Welcome, {username}!")


def create_new_account_screen():
    new_username = ""
    new_password = ""
    creating_account = True
    active = "new_username"
    # Initialize active here

    while creating_account:
        screen.fill(white)

        # Display the UI elements for creating a new account
        create_account_text = font.render("Create New Account", True, black)
        create_account_rect = create_account_text.get_rect(center=(width // 2, 50))
        screen.blit(create_account_text, create_account_rect)

        text_surface_new_username = font.render("New Username:", True, black)
        text_surface_new_password = font.render("New Password:", True, black)
        screen.blit(text_surface_new_username, (100, 200))
        screen.blit(text_surface_new_password, (100, 300))

        # Display input fields for new username and password
        # These are rectangles where the user can type their new username and password
        new_username_rect = pygame.Rect(250, 225, 300, 40)
        new_password_rect = pygame.Rect(250, 325, 300, 40)
        pygame.draw.rect(screen, black, new_username_rect, 2)
        pygame.draw.rect(screen, black, new_password_rect, 2)

        text_surface_new_username = font.render(new_username, True, black)
        text_surface_new_password = font.render("*" * len(new_password), True, black)
        screen.blit(
            text_surface_new_username,
            (new_username_rect.x + 5, new_username_rect.y + 5),
        )
        screen.blit(
            text_surface_new_password,
            (new_password_rect.x + 5, new_password_rect.y + 5),
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Save the new account information (username and password) to your database
                    # For simplicity, let's assume appending to a text file (database.txt)
                    with open("database.txt", "a") as file:
                        file.write(f"{new_username},{new_password},0,0,\n")

                    # Transition back to the login screen
                    creating_account = False

                elif event.key == pygame.K_BACKSPACE:
                    if active == "new_username":
                        new_username = new_username[:-1]
                    elif active == "new_password":
                        new_password = new_password[:-1]
                else:
                    if active == "new_username":
                        new_username += event.unicode
                    elif active == "new_password":
                        new_password += event.unicode

        # Add this part to switch the active field between username and password
        if new_username_rect.collidepoint(pygame.mouse.get_pos()):
            active = "new_username"
        elif new_password_rect.collidepoint(pygame.mouse.get_pos()):
            active = "new_password"
        else:
            active = None

        pygame.display.update()


# Update the login_screen() function to open the create_new_account_screen()
def login_screen():
    username = ""
    password = ""
    username_rect = pygame.Rect(250, 395, 300, 40)
    password_rect = pygame.Rect(250, 495, 300, 40)
    active = None
    create_account_font = pygame.font.Font(None, 36)
    create_account_text = create_account_font.render("Create New Account", True, black)
    create_account_rect = create_account_text.get_rect()
    create_account_rect.center = (width // 2, 600)

    while True:
        screen.fill(white)
        # Display the decorative image
        screen.blit(image, (0, 0))
        screen.blit(create_account_text, create_account_rect)

        text_surface_username = font.render("Username:", True, black)
        text_surface_password = font.render("Password:", True, black)
        screen.blit(text_surface_username, (100, 400))
        screen.blit(text_surface_password, (100, 500))

        pygame.draw.rect(screen, black, username_rect, 2)
        pygame.draw.rect(screen, black, password_rect, 2)

        text_surface_username = font.render(username, True, black)
        text_surface_password = font.render("*" * len(password), True, black)
        screen.blit(text_surface_username, (username_rect.x + 5, username_rect.y + 5))
        screen.blit(text_surface_password, (password_rect.x + 5, password_rect.y + 5))
        screen.blit(create_account_text, create_account_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_account_rect.collidepoint(event.pos):
                    create_new_account_screen()
                elif username_rect.collidepoint(event.pos):
                    active = "username"
                elif password_rect.collidepoint(event.pos):
                    active = "password"
                else:
                    active = None

            if event.type == pygame.KEYDOWN:
                if active == "username":
                    if event.key == pygame.K_RETURN:
                        active = "password"
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active == "password":
                    if event.key == pygame.K_RETURN:
                        if validate_credentials(username, password):
                            return username, password
                            # User authenticated, return username and password
                        else:
                            password = ""
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        pygame.display.update()


# Game logic


# Main
def main():
    global best_guess
    logged_in = False
    while not logged_in:
        username, password = login_screen()
        if username:
            logged_in = True
            # play_audio()
            wordle_game(username, password)


if __name__ == "__main__":
    main()

pygame.init()

# Constants

WIDTH, HEIGHT = 633, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("Starting Tiles.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))
ICON = pygame.image.load("5words_icon.png")
print(str(coin_count))
pygame.display.set_caption("5 Words    Coin:", str(coin_count))
pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

lines = open("wordlist.txt").readlines()
line = lines[0]
CORRECT_WORD = random.choice(lines)
# print(CORRECT_WORD)

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 25)

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
update_window_caption(coin_count)
pygame.display.update()

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75

# Global variables

guesses_count = 0

# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = []

game_result = ""


class Letter:
    def __init__(self, text, bg_position):
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x + 36, self.bg_position[1] + 34)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
        pygame.display.update()


class Indicator:
    def __init__(self, x, y, letter):
        # Initializes variables such as color, size, position, and letter.
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_color = OUTLINE

    def draw(self):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x + 27, self.y + 30))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()


# Drawing the indicators on the screen.

indicator_x, indicator_y = 20, 600

for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 60
    indicator_y += 100
    if i == 0:
        indicator_x = 50
    elif i == 1:
        indicator_x = 105


def check_guess(guess_to_check):
    # Goes through each letter and checks if it should be green, yellow, or grey.
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
            guess_to_check[i].bg_color = GREY
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GREY
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
    if change_database == True:
        best_guess = guesses_count

    if guesses_count == 6 and game_result == "":
        game_result = "L"
        guesses_count = 7
    update_window_caption(coin_count)


def play_again():
    global best_guess, change_database, current_guess, guesses_count, coin_count, coin_added
    coin_added = False
    if guesses_count == 6 and not coin_added:
        coin_count += 13
        coin_added = True
    if guesses_count == 5 and not coin_added:
        coin_count += 20
        coin_added = True
    if guesses_count == 4 and not coin_added:
        coin_count += 35
        coin_added = True
    if guesses_count == 3 and not coin_added:
        coin_count += 60
        coin_added = True
    if guesses_count == 2 and not coin_added:
        coin_count += 250
        coin_added = True
    if guesses_count == 1 and not coin_added:
        coin_count += 1000
        coin_added = True
    update_window_caption(coin_count)
    # Puts the play again text on the screen.
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("FreeSansBold.otf", 40)
    play_again_text = play_again_font.render(
        "Press ENTER to play again!", True, "black"
    )
    play_again_rect = play_again_text.get_rect(center=(WIDTH / 2, 800))
    word_was_text = play_again_font.render(
        f"The word was {CORRECT_WORD}!", True, "black"
    )
    word_was_rect = word_was_text.get_rect(center=(WIDTH / 2, 650))
    if guesses_count < best_guess and best_guess != 0:
        play_again_font = pygame.font.Font("FreeSansBold.otf", 30)
        high_score_text = play_again_font.render(
            f"NEW HIGH SCORE! Your previous best score is {best_guess}.", True, "black"
        )
        change_database = True
        high_score_rect = high_score_text.get_rect(center=(WIDTH / 2, 725))
    elif best_guess != 0:
        high_score_text = play_again_font.render(
            f"Your best score is {best_guess}.", True, "black"
        )
        high_score_rect = high_score_text.get_rect(center=(WIDTH / 2, 725))
    elif best_guess == 0:
        high_score_text = play_again_font.render("That was a good start", True, "black")
        high_score_rect = high_score_text.get_rect(center=(WIDTH / 2, 725))
        change_database = True

    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(high_score_text, high_score_rect)
    SCREEN.blit(play_again_text, play_again_rect)

    # Write the updated high score to the file
    with open("database.txt", "r") as file:
        lines = file.readlines()

    with open("database.txt", "w") as file:
        for line in lines:
            # Update the line with the new high score for the specific user
            if f"{username1},{password1}," in line and change_database == True:
                line = f"{username1},{password1},{guesses_count},{coin_count}\n"
            elif f"{username1},{password1}," in line and change_database == False:
                line = f"{username1},{password1},{best_guess},{coin_count}\n"
            file.write(line)
    pygame.display.update()


def reset():
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result, coin_added
    if change_database == True:
        best_guess = guesses_count
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    lines = open("wordlist.txt").readlines()
    line = lines[0]
    CORRECT_WORD = random.choice(lines)
    # print(CORRECT_WORD)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    coin_added = False  # Reset the coin_added flag to False here

    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()


def create_new_letter():
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(
        key_pressed, (current_letter_bg_x, guesses_count * 100 + LETTER_Y_SPACING)
    )
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()


def delete_letter():
    # Deletes the last letter from the guess.e
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING


while True:
    if game_result != "" and not game_ended:
        play_again()
        game_ended = True
    if change_database:
        update_window_caption(coin_count)
        change_database = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                    game_ended = False  # Reset the game-ended flag
                else:
                    file = open("wordlist.txt")
                    if len(current_guess_string) == 5 and (
                        current_guess_string.lower() in file.read()
                    ):
                        check_guess(current_guess)
                        # play_audio()
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()
    pygame.display.update()