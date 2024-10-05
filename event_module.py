import pygame
from dice_module import roll_dice
from draw_module import create_dice_rects, create_selected_dice_rects


def handle_events(dice_values, roll_button, clicked_button, selected_dices):
    running = True
    mouse_pos = pygame.mouse.get_pos()
    hover_button = roll_button.collidepoint(mouse_pos)

    if hover_button:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_values = [roll_dice() for _ in range(5 - len(selected_dices))]
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

        elif event.type == pygame.MOUSEBUTTONUP:
            clicked_button = False
            if roll_button.collidepoint(event.pos):
                dice_values = [roll_dice() for _ in range(5 - len(selected_dices))]
    return running, dice_values, hover_button, clicked_button, selected_dices, dice_values
