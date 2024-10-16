from dice_module import roll_dice

class AI:
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
    
    def rollDice(self, diceValue,selected_dices):
        num_rolls = 5 - len(selected_dices)
        rolled_dice = [roll_dice() for _ in range(num_rolls)]
        
        return rolled_dice + selected_dices  
