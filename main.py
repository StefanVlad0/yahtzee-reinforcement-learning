import pygame
import sys
from draw_module import draw_screen
from event_module import handle_events
import settings
from settings import Messages
from calcs import calc_values

pygame.init()
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]  # initializare imagini

screen_info = pygame.display.Info()
settings.WIDTH, settings.HEIGHT = screen_info.current_w, screen_info.current_h

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("AI-Project")
dice_values = []
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]
clock = pygame.time.Clock()


def create_score_option_rects():
    table_width = 400
    cell_height = 40
    x_start = settings.WIDTH - table_width - 20
    y_start = settings.HEIGHT // 2 - 680 // 2

    categories = [
        "", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sum", "Bonus",
        "Three of a kind", "Four of a kind", "Full House", "Small straight",
        "Large straight", "Chance", "YAHTZEE", "TOTAL SCORE"
    ]

    score_option_rects = []
    for i, category in enumerate(categories):
        if category:  # Sărim peste prima categorie goală
            rect = pygame.Rect(x_start, y_start + i * cell_height, table_width // 3, cell_height)
            score_option_rects.append((rect, category))

    return score_option_rects


roll_button = pygame.Rect(settings.WIDTH // 2 - 100, settings.HEIGHT - 300, 200, 50)
selected_dices = []
clicked_button = False
rolls_left = 3
button_disabled = False
message = Messages.EMPTY
needs_recalc = False
score_selected = False
score_option_rects = create_score_option_rects()
score = []
endPlayerTurn = False

running = True
while running:
    running, dice_values, hover_button, clicked_button, selected_dices, dice_values, rolls_left, button_disabled, needs_recalc, endPlayerTurn = handle_events(dice_values, roll_button, clicked_button, selected_dices, rolls_left, button_disabled, needs_recalc, score_option_rects, score)

    if (needs_recalc):
        score = calc_values(selected_dices + dice_values)
        needs_recalc = False

    if (rolls_left == 3):
        message = Messages.THREE_ROLLS_LEFT
    elif (rolls_left == 2):
        message = Messages.TWO_ROLLS_LEFT
    elif (rolls_left == 1):
        message = Messages.ONE_ROLLS_LEFT
    elif (rolls_left == 0):
        message = Messages.ZERO_ROLLS_LEFT

    if rolls_left == 0 and not score_selected:
        message = Messages.ZERO_ROLLS_LEFT

    if score_selected:
        message = Messages.AI_TURN

    if endPlayerTurn:
        rolls_left = 3

    draw_screen(screen, dice_values, dice_images, roll_button, hover_button, clicked_button, selected_dices, button_disabled, message)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
