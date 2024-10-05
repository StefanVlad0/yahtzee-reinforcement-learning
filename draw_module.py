import pygame
import settings


def draw_screen(screen, values, dice_images, roll_button, hover_button, clicked_button, selected_dices):
    screen.fill(settings.GREEN)
    draw_dice(screen, values, dice_images)
    draw_button(screen, roll_button, hover_button, clicked_button)
    draw_selected_dices(screen, selected_dices, dice_images)


def draw_dice(screen, values, dice_images):
    x_start = (settings.WIDTH - (5 * settings.DICE_SIZE + 4 * settings.SPACING)) // 2
    y_start = settings.HEIGHT // 2 - settings.DICE_SIZE // 2

    for i, value in enumerate(values):
        # Calculăm poziția fiecărui zar
        dice_rect = pygame.Rect(x_start + i * (settings.DICE_SIZE + settings.SPACING), y_start, settings.DICE_SIZE, settings.DICE_SIZE)

        # Desenăm imaginea zarului corespunzător
        screen.blit(dice_images[value - 1], dice_rect.topleft)  # `value - 1` deoarece imaginile sunt indexate de la 0


def draw_selected_dices(screen, selected_dices, dice_images):
    x_start = (settings.WIDTH - (5 * settings.DICE_SIZE + 4 * settings.SPACING)) // 2  # - (2.5 * settings.DICE_SIZE + 2 * settings.SPACING)
    y_start = settings.HEIGHT // 2 - settings.DICE_SIZE // 2 + 350
    for i, value in enumerate(selected_dices):
        dice_rect = pygame.Rect(x_start + i * (settings.DICE_SIZE + settings.SPACING), y_start, settings.DICE_SIZE, settings.DICE_SIZE)
        screen.blit(dice_images[value - 1], dice_rect.topleft)


def draw_button(screen, button_rect, hover_button, clicked_button):
    if clicked_button:
        button_color = settings.BUTTON_CLICKED_COLOR  # Culoare gri închis pentru click
    elif hover_button:
        button_color = settings.BUTTON_HOVER_COLOR  # Culoare pentru hover
    else:
        button_color = settings.BUTTON_COLOR

    pygame.draw.rect(screen, button_color, button_rect)

    font = pygame.font.SysFont('arial', 30)
    text = font.render("Roll Dice", True, settings.BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
