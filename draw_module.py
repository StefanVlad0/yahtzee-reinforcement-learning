import pygame
import settings


# Afiseaza sum
# def calculate_sum_and_bonus(screen, player, ai):
#     if player.check_sum():
#         if player.calculate_sum():
#             player.scores["Bonus"] = 35
#         else:
#             player.score["Bonus"] = 0

#     if ai.check_sum():
#         if ai.calculate_sum() >= 63:
#             ai.scores["Bonus"] = 35
#         else:
#             ai.scores["Bonus"] = 0


# def draw_total_score(screen, player, ai):
#     player.check_total_score()
#     ai.check_total_score()

def draw_chat(screen, chat_log, user_text, input_box, input_active, cursor_pos, scroll_offset=0):
    # Dimensiunile și poziția box-ului pentru chat
    font = pygame.font.Font(None, 36)
    chat_box_x = 10
    chat_box_y = settings.HEIGHT - 250  # Aproape de partea de jos a ecranului
    chat_box_width = 400
    chat_box_height = 200
    y = 10
    # Desenăm background-ul box-ului pentru chat
    pygame.draw.rect(screen, settings.WHITE, (chat_box_x, chat_box_y, chat_box_width, chat_box_height))
    pygame.draw.rect(screen, settings.BLACK, (chat_box_x, chat_box_y, chat_box_width, chat_box_height), 2)  # Border negru

    # Fontul pentru text
    font = pygame.font.Font(None, 24)
    line_height = 20
    padding = 10

    # Calculăm liniile generate din chat_log
    wrapped_lines = []
    for chat in chat_log:
        words = chat.split(" ")
        line = ""
        for word in words:
            if font.size(line + word)[0] > chat_box_width - 2 * padding:
                wrapped_lines.append(line)
                line = word + " "
            else:
                line += word + " "
        wrapped_lines.append(line.strip())

    # Aplicăm scroll-ul
    start_line = max(0, len(wrapped_lines) - (chat_box_height // line_height)) - scroll_offset
    visible_lines = wrapped_lines[start_line:start_line + (chat_box_height // line_height)]

    # Desenăm liniile vizibile
    y = chat_box_y + padding
    for line in visible_lines:
        chat_surface = font.render(line, True, settings.BLACK)
        screen.blit(chat_surface, (chat_box_x + padding, y))
        y += line_height

    # Desenăm input box-ul
    pygame.draw.rect(screen, settings.BLACK, input_box, 2)
    filtered_user_text = user_text.replace('\x00', '')  # Remove null characters
    text_surface = font.render(filtered_user_text, True, settings.BLACK)
    text_rect = text_surface.get_rect()
    if text_rect.width > input_box.width - 10:
        text_surface = pygame.transform.scale(text_surface, (input_box.width - 10, text_rect.height))
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Desenăm cursorul dacă input-ul este activ
    if input_active:
        cursor_x = input_box.x + 5 + font.size(filtered_user_text[:cursor_pos])[0]
        pygame.draw.line(screen, settings.BLACK, (cursor_x, input_box.y + 5), (cursor_x, input_box.y + 25))

    # Opțional: scroll bar
    # if len(wrapped_lines) > chat_box_height // line_height:
    #     scroll_bar_height = (chat_box_height / len(wrapped_lines)) * chat_box_height
    #     scroll_bar_y = chat_box_y + (scroll_offset / len(wrapped_lines)) * chat_box_height
    #     pygame.draw.rect(screen, settings.BLACK, (chat_box_x + chat_box_width - 10, scroll_bar_y, 5, scroll_bar_height))


def create_score_option_rects():
    table_width = 375
    cell_height = 30
    table_height = 510
    x_start = settings.WIDTH - table_width - 20
    y_start = settings.HEIGHT // 2 - table_height // 2

    categories = [
        "", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sum", "Bonus",
        "Three_of_a_kind", "Four_of_a_kind", "Full_House", "Small_straight",
        "Large_straight", "Chance", "YAHTZEE", "TOTAL_SCORE"
    ]

    score_option_rects = []
    for i, category in enumerate(categories):
        if category:  # Sărim peste prima categorie goală
            rect = pygame.Rect(x_start, y_start + i * cell_height, table_width // 3, cell_height)
            score_option_rects.append((rect, category))

    return score_option_rects


def draw_screen(screen, values, dice_images, roll_button, hover_button, clicked_button, selected_dices, button_disabled, message, score, player, ai, isAITurn, chat_log, user_text, input_box, input_active, cursor_pos):
    screen.fill(settings.GREEN)
    draw_dice(screen, values, dice_images)
    draw_button(screen, roll_button, hover_button, clicked_button, button_disabled)
    draw_selected_dices(screen, selected_dices, dice_images)
    draw_score_table(screen, score, player, isAITurn, ai)
    draw_info(screen, message)
    draw_chat(screen, chat_log, user_text, input_box, input_active, cursor_pos)
    player.check_sum()
    player.check_total_score()
    ai.check_sum()
    ai.check_total_score()
    # print(player.scores)
    # print('\n')
    # print(ai.scores)


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


def draw_score_table(screen, score, player, isAITurn, ai):
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

        category_modified = category.replace(" ", "_")

        if category_modified in score:
            score_value = score[category_modified]
        else:
            score_value = 0

        player_score = player.get_score(category_modified)
        ai_score = ai.get_score(category_modified)

        text = font.render(category, True, settings.BLACK)
        screen.blit(text, (x_start + 10, y_start + i * cell_height + 10))

        if player_score is not None:
            if player_score == -1:
                if (isAITurn is False):
                    if (score_value != 0):
                        score_text = font.render(str(score_value), True, settings.RED)
                        if (score_value > 9):
                            screen.blit(score_text, (x_start + 175, y_start + i * cell_height + 10))
                        else:
                            screen.blit(score_text, (x_start + 180, y_start + i * cell_height + 10))
            else:
                score_text = font.render(str(player_score), True, settings.BLACK)
                if (player_score > 9):
                    screen.blit(score_text, (x_start + 175, y_start + i * cell_height + 10))
                else:
                    screen.blit(score_text, (x_start + 180, y_start + i * cell_height + 10))

        if ai_score is not None:
            if ai_score == -1:
                if (isAITurn is True):
                    if (score_value != 0):
                        score_text = font.render(str(score_value), True, settings.RED)
                        if (score_value > 9):
                            screen.blit(score_text, (x_start + 305, y_start + i * cell_height + 10))
                        else:
                            screen.blit(score_text, (x_start + 310, y_start + i * cell_height + 10))
            else:
                score_text = font.render(str(ai_score), True, settings.BLACK)
                if (ai_score > 9):
                    screen.blit(score_text, (x_start + 305, y_start + i * cell_height + 10))
                else:
                    screen.blit(score_text, (x_start + 310, y_start + i * cell_height + 10))

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
