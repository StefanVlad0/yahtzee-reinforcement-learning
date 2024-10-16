import pygame
import settings


def draw_screen(screen, values, dice_images, roll_button, hover_button, clicked_button, selected_dices, button_disabled, message, score):
    screen.fill(settings.GREEN)
    draw_dice(screen, values, dice_images)
    draw_button(screen, roll_button, hover_button, clicked_button, button_disabled)
    draw_selected_dices(screen, selected_dices, dice_images)
    draw_score_table(screen, score)
    draw_info(screen, message)


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
    y_start = settings.HEIGHT // 2 - settings.DICE_SIZE // 2 + 250
    for i, value in enumerate(selected_dices):
        dice_rect = pygame.Rect(x_start + i * (settings.DICE_SIZE + settings.SPACING), y_start, settings.DICE_SIZE, settings.DICE_SIZE)
        screen.blit(dice_images[value - 1], dice_rect.topleft)


def draw_button(screen, button_rect, hover_button, clicked_button, button_disabled):
    if button_disabled:
        button_color = settings.BUTTON_DISABLED_COLOR
    elif clicked_button:
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


def create_dice_rects(dice_values):
    dice_rects = []
    x_start = (settings.WIDTH - (5 * settings.DICE_SIZE + 4 * settings.SPACING)) // 2
    y_start = settings.HEIGHT // 2 - settings.DICE_SIZE // 2

    for i, _ in enumerate(dice_values):
        dice_rect = pygame.Rect(x_start + i * (settings.DICE_SIZE + settings.SPACING), y_start, settings.DICE_SIZE, settings.DICE_SIZE)
        dice_rects.append(dice_rect)

    return dice_rects


def create_selected_dice_rects(selected_dices):
    selected_dice_rects = []
    x_start = (settings.WIDTH - (5 * settings.DICE_SIZE + 4 * settings.SPACING)) // 2
    y_start = settings.HEIGHT // 2 - settings.DICE_SIZE // 2 + 250

    for i, _ in enumerate(selected_dices):
        dice_rect = pygame.Rect(x_start + i * (settings.DICE_SIZE + settings.SPACING), y_start, settings.DICE_SIZE, settings.DICE_SIZE)
        selected_dice_rects.append(dice_rect)

    return selected_dice_rects


def draw_score_table(screen, score):
    table_width = 375
    table_height = 510
    cell_height = 30
    x_start = settings.WIDTH - table_width - 20
    y_start = settings.HEIGHT // 2 - table_height // 2

    pygame.draw.rect(screen, settings.WHITE, (x_start - 10, y_start - 10, table_width + 20, table_height + 20))  # White background

    font = pygame.font.SysFont('arial', 16)

    categories = [
        "", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sum", "Bonus",
        "Three of a kind", "Four of a kind", "Full House", "Small straight",
        "Large straight", "Chance", "YAHTZEE", "TOTAL SCORE"
    ]

    for i, category in enumerate(categories):
        # break line
        pygame.draw.line(screen, settings.BLACK, (x_start, y_start + (i + 1) * cell_height), (x_start + table_width, y_start + (i + 1) * cell_height), 2)

        if category in score:
            score_value = score[category]
        else:
            score_value = 0
        score_text = font.render(str(score_value), True, settings.RED)

        text = font.render(category, True, settings.BLACK)
        screen.blit(text, (x_start + 10, y_start + i * cell_height + 10))
        if (score_value != 0):
            if(score_value > 9):
                screen.blit(score_text, (x_start + 175, y_start + i * cell_height + 10))
            else:
                screen.blit(score_text, (x_start + 180, y_start + i * cell_height + 10))

    column_labels = ["You", "AI"]
    for j, label in enumerate(column_labels):
        pygame.draw.line(screen, settings.BLACK, (x_start + (j + 1) * (table_width // 3), y_start), (x_start + (j + 1) * (table_width // 3), y_start + table_height), 2)

        # Text pentru coloanele "You" și "AI"
        column_text = font.render(label, True, settings.BLACK)
        screen.blit(column_text, (x_start + 10 + (j + 1) * (table_width // 3), y_start + 10))

    # delimiter lines
    pygame.draw.line(screen, settings.BLACK, (x_start, y_start + 7 * cell_height), (x_start + table_width, y_start + 7 * cell_height), 5)
    pygame.draw.line(screen, settings.BLACK, (x_start, y_start + 9 * cell_height), (x_start + table_width, y_start + 9 * cell_height), 5)
    pygame.draw.line(screen, settings.BLACK, (x_start, y_start + 16 * cell_height), (x_start + table_width, y_start + 16 * cell_height), 5)

    # outlines
    pygame.draw.line(screen, settings.BLACK, (x_start, y_start + 0 * cell_height), (x_start + table_width, y_start + 0 * cell_height), 2)
    pygame.draw.line(screen, settings.BLACK, (x_start + 0 * (table_width // 3), y_start), (x_start + 0 * (table_width // 3), y_start + table_height), 2)
    pygame.draw.line(screen, settings.BLACK, (x_start + 3 * (table_width // 3), y_start), (x_start + 3 * (table_width // 3), y_start + table_height), 2)


def draw_info(screen, message):
    x_start = settings.WIDTH // 2 - settings.INFO_WIDTH // 2
    y_start = settings.HEIGHT // 2 - settings.INFO_HEIGHT // 2 - 125

    pygame.draw.rect(screen, settings.YELLOW, (x_start, y_start, settings.INFO_WIDTH, settings.INFO_HEIGHT))

    font = pygame.font.SysFont('arial', 16)
    message_text = font.render(message.value, True, settings.BLACK)

    screen.blit(message_text, (x_start + 10, y_start + 10))
