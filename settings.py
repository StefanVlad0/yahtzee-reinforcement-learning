# settings.py
from enum import Enum


class Messages(Enum):
    THREE_ROLLS_LEFT = "Your turn. You have 3 throws left."
    TWO_ROLLS_LEFT = "Click the dice you want to keep. You have 2 throws left."
    ONE_ROLLS_LEFT = "Click the dice you want to keep. You have 1 throws left."
    ZERO_ROLLS_LEFT = "Select your move by clicking a cell on the scorecard."
    EMPTY = ""


# Screen dimensions
WIDTH, HEIGHT = 1600, 1000

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
GREEN = (0, 160, 0)
YELLOW = (237, 243, 90)

# Dice settings
DICE_SIZE = 100
SPACING = 20

# Button
BUTTON_COLOR = (235, 235, 235)
BUTTON_HOVER_COLOR = (255, 255, 255)
BUTTON_CLICKED_COLOR = (200, 200, 200)
BUTTON_DISABLED_COLOR = (180, 180, 180)

# Info box
INFO_HEIGHT = 75
INFO_WIDTH = 500
