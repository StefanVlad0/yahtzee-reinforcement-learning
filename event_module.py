import pygame
from dice_module import roll_dice
from draw_module import create_dice_rects, create_selected_dice_rects
from testModel import get_answer
import threading


def handle_events(dice_values, roll_button, clicked_button, selected_dices, rolls_left, button_disabled, needs_recalc, score_option_rects, score, player, endPlayerTurn, isAITurn, user_text, chat_log, response_text, input_box, input_active, cursor_pos):
    running = True
    mouse_pos = pygame.mouse.get_pos()
    button_disabled = True if rolls_left == 0 or isAITurn else False
    hover_button = roll_button.collidepoint(mouse_pos) if not button_disabled else False

    if hover_button and not isAITurn:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    if not isAITurn:
        for rect, category in score_option_rects:
            if rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    def process_ai_response(user_text):
        """Rulează `get_answer` într-un fir separat."""
        nonlocal response_text
        response = get_answer(user_text)
        response_text = response
        chat_log.pop()
        chat_log.append(f"Bot: {response}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    chat_log.append(f"User: {user_text}")
                    response_text = "Procesăm răspunsul..."
                    chat_log.append(f"Bot: {response_text}")  # Mesaj temporar
                    ai_thread = threading.Thread(target=process_ai_response, args=(user_text,))
                    ai_thread.start()  # Pornește firul pentru AI
                    user_text = ''
                    cursor_pos = 0
                elif event.key == pygame.K_BACKSPACE:
                    if cursor_pos > 0:
                        user_text = user_text[:cursor_pos-1] + user_text[cursor_pos:]
                        cursor_pos -= 1
                elif event.key == pygame.K_DELETE:
                    if cursor_pos < len(user_text):
                        user_text = user_text[:cursor_pos] + user_text[cursor_pos+1:]
                elif event.key == pygame.K_LEFT:
                    if cursor_pos > 0:
                        cursor_pos -= 1
                elif event.key == pygame.K_RIGHT:
                    if cursor_pos < len(user_text):
                        cursor_pos += 1
                elif event.key == pygame.K_SPACE:
                    user_text = user_text[:cursor_pos] + ' ' + user_text[cursor_pos:]
                    cursor_pos += 1
                elif event.key == pygame.K_v and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    clipboard_text = pygame.scrap.get(pygame.SCRAP_TEXT).decode('utf-8')
                    user_text = user_text[:cursor_pos] + clipboard_text + user_text[cursor_pos:]
                    cursor_pos += len(clipboard_text)
                else:
                    user_text = user_text[:cursor_pos] + event.unicode + user_text[cursor_pos:]
                    cursor_pos += 1
            else:
                if event.key == pygame.K_SPACE and not isAITurn:
                    if rolls_left:
                        dice_values = [roll_dice() for _ in range(5 - len(selected_dices))]
                        rolls_left = rolls_left - 1
                        needs_recalc = True
                elif event.key == pygame.K_ESCAPE:
                    running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False

            if roll_button.collidepoint(event.pos) and not isAITurn:
                clicked_button = True

            if not isAITurn:
                for i, dice_rect in enumerate(create_dice_rects(dice_values)):
                    if dice_rect.collidepoint(event.pos):
                        selected_dices.append(dice_values[i])
                        dice_values.pop(i)

                for i, selected_rect in enumerate(create_selected_dice_rects(selected_dices)):
                    if selected_rect.collidepoint(event.pos):
                        dice_values.append(selected_dices[i])
                        selected_dices.pop(i)

            if not isAITurn:
                for rect, category in score_option_rects:
                    if rect.collidepoint(event.pos):
                        if score:
                            value = score.get(category)
                            if value is not None and player.checkScore(category):
                                player.set_score(category, value)
                                isAITurn = True
                                endPlayerTurn = True

        elif event.type == pygame.MOUSEBUTTONUP:
            clicked_button = False
            if roll_button.collidepoint(event.pos) and not isAITurn:
                if rolls_left:
                    dice_values = [roll_dice() for _ in range(5 - len(selected_dices))]
                    rolls_left = rolls_left - 1
                    needs_recalc = True

    return running, dice_values, hover_button, clicked_button, selected_dices, dice_values, rolls_left, button_disabled, needs_recalc, endPlayerTurn, isAITurn, user_text, chat_log, input_active, cursor_pos
