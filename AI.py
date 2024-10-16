from dice_module import roll_dice

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
    
    def rollDice(self, diceValue,selected_dices):
        num_rolls = 5 - len(selected_dices)
        rolled_dice = [roll_dice() for _ in range(num_rolls)]
        
        return rolled_dice + selected_dices  
