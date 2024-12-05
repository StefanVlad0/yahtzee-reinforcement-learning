import sys
import itertools
import random
import csv
from calcs import get_reward
import pickle

# --- Q-TABLE, initialized with 0s --- #

Q_table = {}


def save_q_table(Q_table, filename):
    with open(filename, 'wb') as file:
        pickle.dump(Q_table, file)


# Generate all possible combinations of the score table
def generate_scor_table_combinations():
    return list(itertools.product([0, 1], repeat=13))


# Generate all possible combinations of the dices
def generate_dice_combinations():
    return list(itertools.product([1, 2, 3, 4, 5, 6], repeat=5))


def generate_rerolls_combinations():
    return [0, 1, 2]


def encode_state(scor_table, dice, rerolls_left):
    scor_table_tuple = tuple(scor_table)
    dice_tuple = tuple(sorted(dice))  # Sorted dices
    return scor_table_tuple, dice_tuple, rerolls_left


def save_q_table_to_csv(Q_table, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Scrie header-ul (opțional)
        writer.writerow(['State', 'Actions'])
        # Scrie fiecare stare și acțiunile corespunzătoare
        for state, actions in Q_table.items():
            writer.writerow([state, actions])


def initialize_q_table():
    Q_table = {}

    scor_table_combinations = generate_scor_table_combinations()
    dice_combinations = generate_dice_combinations()
    rerolls_combinations = generate_rerolls_combinations()

    total_combinations = len(scor_table_combinations) * len(dice_combinations) * len(rerolls_combinations)
    generated_combinations = 0
    next_percentage_threshold = 10

    # Generate all possible states
    for scor_table in scor_table_combinations:
        for dice in dice_combinations:
            for rerolls_left in rerolls_combinations:
                state = encode_state(scor_table, dice, rerolls_left)
                Q_table[state] = [0] * 45  # 44 actions, 13 categories + (2^5 - 1) rerolls configurations
                generated_combinations += 1
                percentage = (generated_combinations / total_combinations) * 100
                if percentage >= next_percentage_threshold:
                    print(f"Generated {generated_combinations}/{total_combinations} ({percentage:.2f}%) combinations")
                    next_percentage_threshold += 10

    # Salvează tabela Q într-un fișier CSV
    # save_q_table_to_csv(Q_table, 'q_table.csv')

    return Q_table


def calculate_memory_usage(Q_table):
    return sys.getsizeof(Q_table)


Q_table = initialize_q_table()


# --- Train Q-Learning --- #

def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]


# reprezents 1 epoch - a complete game
def play_game():
    scor_table = [0] * 13  # initialize score table with 0 because the game has started
    dice = roll_dice()
    rerolls_left = 2

    zero_indexes = [i for i, val in enumerate(scor_table) if val == 0]  # get the indexes of the categories that are not filled yet
    print("Dices: ", dice)
    print("Scor table: ", scor_table)
    while (zero_indexes):
        state = encode_state(scor_table, dice, rerolls_left)

        # One in three chance to reroll the dices, only if we have rerolls left
        if rerolls_left > 0 and random.randint(0, 2) == 0:
            number_of_dices_to_reroll = random.randint(1, 5)  # if we are here, we have to reroll at least one dice
            indexes_to_reroll = random.sample(range(5), number_of_dices_to_reroll)
            indexes_to_reroll.sort()
            for i in indexes_to_reroll:
                dice[i] = random.randint(1, 6)
            rerolls_left -= 1
            # Here it should be the action and Q(S, a) should be updated
            reward = 0
            new_state = encode_state(scor_table, dice, rerolls_left)
            print("ACTION: Reroll the dices with indexes: ", indexes_to_reroll)
            print("Dices after reroll: ", dice)
            if new_state in Q_table:
                index = 13 + int(''.join(map(str, [1 if i in indexes_to_reroll else 0 for i in range(5)])), 2)
                print("New State is in Q_table", new_state)
                Q_observed = reward + 0.9 * max(Q_table[new_state])
                TD_error = Q_observed - Q_table[state][index]
                Q_table[state][index] += 0.1 * TD_error
            else:
                print("New state not in Q_table")

        else:  # Choose random index from scor_table, only if it's 0 (available)
            index = random.choice(zero_indexes)
            # Here it should be the action and Q(S, a) should be updated
            print("ACTION: Choose the category: ", index)
            reward = get_reward(index, sorted(dice))
            print("Reward: ", reward)
            dice = roll_dice()
            scor_table[index] = 1
            rerolls_left = 2
            print("Dices: ", dice)
            print("Scor table: ", scor_table)
            new_state = encode_state(scor_table, dice, rerolls_left)
            if new_state in Q_table:
                print("New State is in Q_table", new_state)
                Q_observed = reward + 0.9 * max(Q_table[new_state])
                TD_error = Q_observed - Q_table[state][index]
                Q_table[state][index] += 0.1 * TD_error
            else:
                print("New state not in Q_table")
        zero_indexes = [i for i, val in enumerate(scor_table) if val == 0]

    print("No more zeros in the scor_table. Game over!")


number_of_epochs = 1000

for i in range(number_of_epochs):
    play_game()

# Salvarea Q_table în fișierul 'q_table.pkl'
save_q_table(Q_table, 'q_table.pkl')
