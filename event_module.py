import pygame
from dice_module import roll_dice
from draw_module import create_dice_rects, create_selected_dice_rects


def handle_events(dice_values, roll_button, clicked_button, selected_dices, rolls_left, button_disabled, needs_recalc, score_option_rects, score, player, endPlayerTurn, isAITurn):
    running = True
    mouse_pos = pygame.mouse.get_pos()
    button_disabled = True if rolls_left == 0 or isAITurn else False
    hover_button = roll_button.collidepoint(mouse_pos) if not button_disabled else False

    if hover_button:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    for rect, category in score_option_rects:
        if rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if rolls_left:
                    dice_values = [roll_dice() for _ in range(5 - len(selected_dices))]
                    rolls_left = rolls_left - 1
                    needs_recalc = True
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos):
                clicked_button = True

            for i, dice_rect in enumerate(create_dice_rects(dice_values)):
                if dice_rect.collidepoint(event.pos):
                    selected_dices.append(dice_values[i])
                    dice_values.pop(i)

            for i, selected_rect in enumerate(create_selected_dice_rects(selected_dices)):
                if selected_rect.collidepoint(event.pos):
                    dice_values.append(selected_dices[i])
                    selected_dices.pop(i)

            for rect, category in score_option_rects:
                if rect.collidepoint(event.pos):
                    if score:
                        value = score.get(category)
                        if value is not None:
                            player.set_score(category, value)
                            isAITurn = True
                            endPlayerTurn = True

        elif event.type == pygame.MOUSEBUTTONUP:
            clicked_button = False
            if roll_button.collidepoint(event.pos):
                if rolls_left:
                    dice_values = [roll_dice() for _ in range(5 - len(selected_dices))]
                    rolls_left = rolls_left - 1
                    needs_recalc = True

    return running, dice_values, hover_button, clicked_button, selected_dices, dice_values, rolls_left, button_disabled, needs_recalc, endPlayerTurn, isAITurn
