import pygame
import settings  

def draw_dice(screen, value, x, y):
    pygame.draw.rect(screen, settings.BLUE, pygame.Rect(x, y, settings.DICE_SIZE, settings.DICE_SIZE), border_radius=10)
    font = pygame.font.Font(None, 74)
    text = font.render(str(value), True, settings.BLACK)
    screen.blit(text, (x + settings.DICE_SIZE // 3, y + settings.DICE_SIZE // 4))

def draw_screen(screen, background_color, dice_positions, dice_values):
    screen.fill(background_color)  # Clear screen
    for i, pos in enumerate(dice_positions):
        draw_dice(screen, dice_values[i], pos[0], pos[1])
