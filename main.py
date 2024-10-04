import pygame
import sys
from draw_module import draw_screen
from event_module import handle_events
from dice_module import roll_dice
import settings

pygame.init()
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]  # initializare imagini

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("AI-Project")
dice_values = [roll_dice() for _ in range(5)]
dice_images = [pygame.image.load(f"{i}.png") for i in range(1, 7)]
clock = pygame.time.Clock()

running = True
while running:
    running, dice_values = handle_events(dice_values)

    draw_screen(screen, dice_values, dice_images)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
