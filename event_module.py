import pygame
from dice_module import roll_dice


def handle_events(dice_values):
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_values = [roll_dice() for _ in range(5)]
            if event.key == pygame.K_ESCAPE:
                running = False
    return running, dice_values
