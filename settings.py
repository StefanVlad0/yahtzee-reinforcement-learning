# settings.py
from enum import Enum


class Messages(Enum):
    THREE_ROLLS_LEFT = "Your turn. You have 3 throws left."
    TWO_ROLLS_LEFT = "Click the dice you want to keep. You have 2 throws left."
    ONE_ROLLS_LEFT = "Click the dice you want to keep. You have 1 throws left."
    ZERO_ROLLS_LEFT = "Select your move by clicking a cell on the scorecard."
    AI_TURN = "Now is AI turn."
    EMPTY = ""

class Player:
    def __init__(self):
        self.scores = {
            "Ones": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "Sum": -1,
            "Bonus": -1,
            "Three_of_a_kind": -1,
            "Four_of_a_kind": -1,
            "Full_house": -1,
            "Small_straight": -1,
            "Large_straight": -1,
            "Chance": -1,
            "YAHTZEE": -1,
            "TOTAL_SCORE": -1
        }

    def set_score(self, category, value):
        if category in self.scores:
            self.scores[category] = value
        else:
            print(f"Invalid category: {category}")

    def get_score(self, category):
        return self.scores.get(category, None)

    def showScore(self):
        score_list = [f"{category}: {score}" for category, score in self.scores.items()]
        return "\n".join(score_list)


# Screen dimensions
WIDTH, HEIGHT = None, None

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
GREEN = (0, 160, 0)
YELLOW = (237, 243, 90)
RED = (255, 0, 0)

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
