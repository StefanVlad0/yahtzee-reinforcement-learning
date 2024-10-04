import pygame
import sys
from draw_module import draw_screen
from event_module import handle_events
from dice_module import roll_dice
import settings  

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("AI-Project")

dice_values = roll_dice()  

clock = pygame.time.Clock()

running = True
while running:
    running, dice_values = handle_events(dice_values)

    draw_screen(screen, settings.WHITE, settings.DICE_POSITIONS, dice_values)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
