import pygame
import settings


def draw_screen(screen, values, dice_images, roll_button):
    screen.fill(settings.WHITE)
    draw_dice(screen, values, dice_images)
    draw_button(screen, roll_button)


def draw_dice(screen, values, dice_images):
    x_start = (settings.WIDTH - (5 * settings.DICE_SIZE + 4 * settings.SPACING)) // 2
    y_start = settings.HEIGHT // 2 - settings.DICE_SIZE // 2

    for i, value in enumerate(values):
        # Calculăm poziția fiecărui zar
        dice_rect = pygame.Rect(x_start + i * (settings.DICE_SIZE + settings.SPACING), y_start, settings.DICE_SIZE, settings.DICE_SIZE)

        # Desenăm imaginea zarului corespunzător
        screen.blit(dice_images[value - 1], dice_rect.topleft)  # `value - 1` deoarece imaginile sunt indexate de la 0


def draw_button(screen, button_rect):
    pygame.draw.rect(screen, settings.BUTTON_COLOR, button_rect)
    font = pygame.font.Font(None, 36)  # Font pentru text
    text = font.render("Roll Dice", True, settings.BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
