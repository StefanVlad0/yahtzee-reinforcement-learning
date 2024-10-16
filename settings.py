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
            "ONES": -1,
            "TWOS": -1,
            "THREES": -1,
            "FOURS": -1,
            "FIVES": -1,
            "SIXES": -1,
            "SUM": -1,
            "BONUS": -1,
            "THREE_OF_A_KIND": -1,
            "FOUR_OF_A_KIND": -1,
            "FULL_HOUSE": -1,
            "SMALL_STRAIGHT": -1,
            "LARGE_STRAIGHT": -1,
            "CHANCE": -1,
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


class AI(Enum):
    ONES = -1
    TWOS = -1
    THREES = -1
    FOURS = -1
    FIVES = -1
    SIXES = -1
    SUM = -1
    BONUS = -1
    THREE_OF_A_KIND = -1
    FOUR_OF_A_KIND = -1
    FULL_HOUSE = -1
    SMALL_STRAIGHT = -1
    LARGE_STRAIGHT = -1
    CHANCE = -1
    YAHTZEE = -1
    TOTAL_SCORE = -1


class Aux(Enum):
    ONES = -1
    TWOS = -1
    THREES = -1
    FOURS = -1
    FIVES = -1
    SIXES = -1
    SUM = -1
    BONUS = -1
    THREE_OF_A_KIND = -1
    FOUR_OF_A_KIND = -1
    FULL_HOUSE = -1
    SMALL_STRAIGHT = -1
    LARGE_STRAIGHT = -1
    CHANCE = -1
    YAHTZEE = -1
    TOTAL_SCORE = -1


# Screen dimensions
WIDTH, HEIGHT = None, None

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
