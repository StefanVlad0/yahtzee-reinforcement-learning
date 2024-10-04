import pygame
from dice_module import roll_dice


def handle_events(dice_values, roll_button):
    running = True
    mouse_pos = pygame.mouse.get_pos()

    if roll_button.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Setăm cursorul la "mână" dacă este peste buton
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_values = [roll_dice() for _ in range(5)]
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos):  # Verifică dacă click-ul a fost pe buton
                dice_values = [roll_dice() for _ in range(5)]
    return running, dice_values
