class GameState:
    def __init__(self, player, ai, dice_values, selected_dices, rolls_left, ai_rolls_left, isAITurn):
        self.player = player
        self.ai = ai
        self.dice_values = dice_values
        self.selected_dices = selected_dices
        self.rolls_left = rolls_left
        self.ai_rolls_left = ai_rolls_left
        self.isAITurn = isAITurn

    def update_dice_values(self, dice_values):
        self.dice_values = dice_values

    def update_selected_dices(self, selected_dices):
        self.selected_dices = selected_dices

    def update_rolls_left(self, rolls_left):
        self.rolls_left = rolls_left

    def update_ai_rolls_left(self, ai_rolls_left):
        self.ai_rolls_left = ai_rolls_left

    def switch_turn(self):
        self.isAITurn = not self.isAITurn

    def get_current_player(self):
        return self.ai if self.isAITurn else self.player
