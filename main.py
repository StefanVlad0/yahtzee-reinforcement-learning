import pygame
import sys
from draw_module import draw_screen
from event_module import handle_events
import settings

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

running = True
while running:
    running, dice_values, hover_button, clicked_button, selected_dices, dice_values = handle_events(dice_values, roll_button, clicked_button, selected_dices)

    draw_screen(screen, dice_values, dice_images, roll_button, hover_button, clicked_button, selected_dices)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
