from dice_module import roll_dice
import random


class AI:
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
        category = category
        if category in self.scores:
            self.scores[category] = value
            print(f"Score set AI for {category}: {value}")
        else:
            print(f"Invalid category for AI: {category}")

    def get_score(self, category):
        return self.scores.get(category, None)

    def checkScore(self, category):
        if category in self.scores and self.scores[category] == -1:
            return True
        return False

    def showScore(self):
        score_list = [f"{category}: {score}" for category, score in self.scores.items()]
        return "\n".join(score_list)

    def rollDice(self, diceValue, selected_dices):
        num_rolls = 5 - len(selected_dices)
        rolled_dice = [roll_dice() for _ in range(num_rolls)]
        return rolled_dice, selected_dices

    def chooseOption(self, score):
        keys = [key for key in score if self.checkScore(key)]
        if not keys:
            print("Nu mai există opțiuni cu valoarea -1 disponibile.")
            return
        random_key = random.choice(keys)
        random_value = score[random_key]
        self.set_score(random_key, random_value)
