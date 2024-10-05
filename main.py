import pygame
import sys
from draw_module import draw_screen
from event_module import handle_events
import settings
from settings import Messages
from calcs import calc_values

pygame.init()
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]  # initializare imagini

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("AI-Project")
dice_values = []
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]
clock = pygame.time.Clock()

roll_button = pygame.Rect(settings.WIDTH // 2 - 100, settings.HEIGHT - 300, 200, 50)
selected_dices = []
clicked_button = False
rolls_left = 3
button_disabled = False
message = Messages.EMPTY
needs_recalc = False

running = True
while running:
    running, dice_values, hover_button, clicked_button, selected_dices, dice_values, rolls_left, button_disabled, needs_recalc = handle_events(dice_values, roll_button, clicked_button, selected_dices, rolls_left, button_disabled, needs_recalc)

    if (needs_recalc):
        calc_values(selected_dices + dice_values)
        needs_recalc = False

    if (rolls_left == 3):
        message = Messages.THREE_ROLLS_LEFT
    elif (rolls_left == 2):
        message = Messages.TWO_ROLLS_LEFT
    elif (rolls_left == 1):
        message = Messages.ONE_ROLLS_LEFT
    elif (rolls_left == 0):
        message = Messages.ZERO_ROLLS_LEFT

    draw_screen(screen, dice_values, dice_images, roll_button, hover_button, clicked_button, selected_dices, button_disabled, message)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
