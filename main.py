import pygame
import sys
import random
from draw_module import draw_screen, create_score_option_rects
from event_module import handle_events
import settings
from settings import Messages
from calcs import calc_values
from AI import AI
from game_state import GameState
import pickle


def load_q_table(filename):
    with open(filename, 'rb') as file:
        Q_table = pickle.load(file)
    return Q_table


# Încărcarea Q_table din fișierul 'q_table.pkl'
Q_table = load_q_table('q_table.pkl')

pygame.init()
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]  # initializare imagini

screen_info = pygame.display.Info()
settings.WIDTH, settings.HEIGHT = screen_info.current_w, screen_info.current_h

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("AI-Project")
dice_values = []
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]
clock = pygame.time.Clock()

player = settings.Player()
ai = AI()

roll_button = pygame.Rect(settings.WIDTH // 2 - 100, settings.HEIGHT - 300, 200, 50)
selected_dices = []
clicked_button = False
rolls_left = 3
ai_rolls_left = 3
button_disabled = False
message = Messages.EMPTY
needs_recalc = False
score_option_rects = create_score_option_rects()
score = []
endPlayerTurn = False
startPlayerTurn = True
isAITurn = False
last_roll_time = pygame.time.get_ticks()
roll_interval = 3000
selection_start_time = None
selectAfterRoll = False
can_choose = False
max_index = None


def encode_state(scor_table, dice, rerolls_left):
    scor_table_tuple = tuple(scor_table)
    dice_tuple = tuple(sorted(dice))  # Sorted dices
    return scor_table_tuple, dice_tuple, rerolls_left


# Initialize GameState
game_state = GameState(player, ai, dice_values, selected_dices, rolls_left, ai_rolls_left, isAITurn)

game_over = False
running = True
while running:
    running, dice_values, hover_button, clicked_button, selected_dices, dice_values, rolls_left, button_disabled, needs_recalc, endPlayerTurn, isAITurn = handle_events(dice_values, roll_button, clicked_button, selected_dices, rolls_left, button_disabled, needs_recalc, score_option_rects, score, player, endPlayerTurn, isAITurn)

    # Update GameState
    game_state.update_dice_values(dice_values)
    game_state.update_selected_dices(selected_dices)
    game_state.update_rolls_left(rolls_left)
    game_state.update_ai_rolls_left(ai_rolls_left)
    game_state.isAITurn = isAITurn

    # CONDITIA OPRIRE
    if player.check_end() and ai.check_end():
        if player.scores["TOTAL_SCORE"] > ai.scores["TOTAL_SCORE"]:
            message = Messages.PLAYER_WINS
        elif ai.scores["TOTAL_SCORE"] > player.scores["TOTAL_SCORE"]:
            message = Messages.AI_WINS
        else:
            message = Messages.DRAW
        game_over = True
        # exit()
    # CONDITIA OPRIRE

    if (rolls_left == 3 and isAITurn is False and game_over is False):
        message = Messages.THREE_ROLLS_LEFT_PLAYER
    elif (rolls_left == 2 and isAITurn is False and game_over is False):
        message = Messages.TWO_ROLLS_LEFT_PLAYER
    elif (rolls_left == 1 and isAITurn is False and game_over is False):
        message = Messages.ONE_ROLLS_LEFT_PLAYER
    elif (rolls_left == 0 and isAITurn is False and game_over is False):
        message = Messages.ZERO_ROLLS_LEFT_PLAYER

    if isAITurn and game_over is False:
        message = Messages.AI_TURN
        current_time = pygame.time.get_ticks()

        if current_time - last_roll_time > roll_interval:
            if can_choose and not endPlayerTurn:
                score = calc_values(selected_dices + dice_values)  # Calculate the score
                ai.chooseOption(score, max_index)  # Pass the score to AI
                startPlayerTurn = True
                can_choose = False
                max_index = None

    if startPlayerTurn and game_over is False:
        startPlayerTurn = False
        rolls_left = 3
        selected_dices = []
        dice_values = []
        score = []
        isAITurn = False

    if endPlayerTurn and game_over is False:
        ai_rolls_left = 3
        selected_dices = []
        dice_values = []
        score = []

    if isAITurn and game_over is False:
        endPlayerTurn = False
        current_time = pygame.time.get_ticks()

        if current_time - last_roll_time > roll_interval:
            dice_values, selected_dices = ai.rollDice(dice_values, selected_dices)
            ai_rolls_left = ai_rolls_left - 1
            state = encode_state(ai.get_score_state(), sorted(dice_values + selected_dices), ai_rolls_left)
            print(state)
            q_values = Q_table[state]
            max_value = max(q_values)
            max_index = q_values.index(max_value)
            print("Actiune", max_index)
            if max_index < 13:  # selectam din tabel
                can_choose = True

            needs_recalc = True
            last_roll_time = current_time
            selectAfterRoll = True

        if selectAfterRoll and ai_rolls_left >= 1:
            if not selection_start_time:
                selection_start_time = pygame.time.get_ticks()

            if current_time - selection_start_time >= 1000:
                selectAfterRoll = False
                selection_start_time = None

                numberOfSelectedDice = random.randint(0, len(dice_values))
                for _ in range(numberOfSelectedDice):
                    randomSelected = random.randint(0, len(dice_values) - 1)
                    selected_dices.append(dice_values[randomSelected])
                    dice_values.pop(randomSelected)

    if (needs_recalc):
        score = calc_values(selected_dices + dice_values)
        needs_recalc = False

    draw_screen(screen, dice_values, dice_images, roll_button, hover_button, clicked_button, selected_dices, button_disabled, message, score, player, ai, isAITurn)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
