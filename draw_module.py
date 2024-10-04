import pygame
import settings


def draw_screen(screen, values, dice_images):
    screen.fill(settings.WHITE)
    draw_dice(screen, values, dice_images)


def draw_dice(screen, values, dice_images):
    x_start = (settings.WIDTH - (5 * settings.DICE_SIZE + 4 * settings.SPACING)) // 2
    y_start = settings.HEIGHT // 2 - settings.DICE_SIZE // 2

    for i, value in enumerate(values):
        # Calculăm poziția fiecărui zar
        dice_rect = pygame.Rect(x_start + i * (settings.DICE_SIZE + settings.SPACING), y_start, settings.DICE_SIZE, settings.DICE_SIZE)

        # Desenăm imaginea zarului corespunzător
        screen.blit(dice_images[value - 1], dice_rect.topleft)  # `value - 1` deoarece imaginile sunt indexate de la 0
