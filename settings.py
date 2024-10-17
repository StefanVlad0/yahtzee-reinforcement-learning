# settings.py
from enum import Enum


class Messages(Enum):
    THREE_ROLLS_LEFT_PLAYER = "Your turn. You have 3 throws left."
    TWO_ROLLS_LEFT_PLAYER = "Click the dice you want to keep. You have 2 throws left."
    ONE_ROLLS_LEFT_PLAYER = "Click the dice you want to keep. You have 1 throws left."
    ZERO_ROLLS_LEFT_PLAYER = "Select your move by clicking a cell on the scorecard."
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
            "Full_House": -1,
            "Small_straight": -1,
            "Large_straight": -1,
            "Chance": -1,
            "YAHTZEE": -1,
            "TOTAL_SCORE": -1
        }

    def set_score(self, category, value):
        print(f"Score set Player for {category}: {value}")
        if category in self.scores:
            self.scores[category] = value
        else:
            print(f"Invalid category for Player: {category}")

    def get_score(self, category):
        return self.scores.get(category, None)

    def checkScore(self, category):
        if category in self.scores and self.scores[category] == -1:
            return True
        return False

    def showScore(self):
        score_list = [f"{category}: {score}" for category, score in self.scores.items()]
        return "\n".join(score_list)

    def check_sum(self):
        main_scores = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
        for category in main_scores:
            if self.scores[category] == -1:
                return

        main_scores = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
        total_sum = sum(self.scores[category] for category in main_scores if self.scores[category] != -1)
        self.scores["Sum"] = total_sum

        if total_sum >= 63:
            self.scores["Bonus"] = 35
        else:
            self.scores["Bonus"] = 0

    def check_total_score(self):
        for key in self.scores:
            if key != "TOTAL_SCORE" and self.scores[key] == -1:
                return

        total_sum = sum(value for key, value in self.scores.items() if (key != "TOTAL_SCORE" and key != "Sum") and value != -1)
        self.scores["TOTAL_SCORE"] = total_sum
        return

    def check_end(self):
        for key in self.scores:
            if self.scores[key] == -1:
                return False
        return True


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
