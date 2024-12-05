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
            "Full_House": -1,
            "Small_straight": -1,
            "Large_straight": -1,
            "Chance": -1,
            "YAHTZEE": -1,
            "TOTAL_SCORE": -1
        }

    def get_score_state(self):
        state = []
        for key in self.scores:
            if key == "TOTAL_SCORE" or key == "Sum" or key == "Bonus":
                continue
            if self.scores[key] == -1:
                state.append(0)
            else:
                state.append(1)
        return state

    def set_score(self, index, value):

        value_to_insert = value[index]

        score_array = {
            "Ones": 0,
            "Twos": 1,
            "Threes": 2,
            "Fours": 3,
            "Fives": 4,
            "Sixes": 5,
            "Three_of_a_kind": 6,
            "Four_of_a_kind": 7,
            "Full_House": 8,
            "Small_straight": 9,
            "Large_straight": 10,
            "Chance": 11,
            "YAHTZEE": 12
        }

        for key, value in score_array.items():
            if value == index:
                self.scores[key] = value_to_insert
                print(f"Score set AI for {key}: {value_to_insert}")

    def get_score(self, category):
        return self.scores.get(category, None)

    def checkScore(self, index):
        options = self.get_score_state()
        if options[index] == 1:
            return True
        return False

    def showScore(self):
        score_list = [f"{category}: {score}" for category, score in self.scores.items()]
        return "\n".join(score_list)

    def rollDice(self, diceValue, selected_dices):
        num_rolls = 5 - len(selected_dices)
        rolled_dice = [roll_dice() for _ in range(num_rolls)]
        return rolled_dice, selected_dices

    def chooseOption(self, score, index):
        invalid = self.checkScore(index)
        if invalid:
            print("Nu mai există opțiuni cu valoarea -1 disponibile.")
            return
        points = []
        for key in score:
            points.append(score[key])
        self.set_score(index, points)

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

    def check_end(self):
        for key in self.scores:
            if self.scores[key] == -1:
                return False
        return True
