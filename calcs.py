def get_reward(index, dices):
    if index == 0:
        return calc_values(dices)["Ones"]
    elif index == 1:
        return calc_values(dices)["Twos"]
    elif index == 2:
        return calc_values(dices)["Threes"]
    elif index == 3:
        return calc_values(dices)["Fours"]
    elif index == 4:
        return calc_values(dices)["Fives"]
    elif index == 5:
        return calc_values(dices)["Sixes"]
    elif index == 6:
        return calc_values(dices)["Three_of_a_kind"]
    elif index == 7:
        return calc_values(dices)["Four_of_a_kind"]
    elif index == 8:
        return calc_values(dices)["Full_House"]
    elif index == 9:
        return calc_values(dices)["Small_straight"]
    elif index == 10:
        return calc_values(dices)["Large_straight"]
    elif index == 11:
        return calc_values(dices)["Chance"]
    elif index == 12:
        return calc_values(dices)["YAHTZEE"]

# Suma numerelor de pe zar
def calc_sum_dices(dices):
    sum = 0
    for dice in dices:
        sum += dice
    return sum


# Verifica daca exista doua zaruri de acelasi tip
def exists_two_of_a_kind(dices):
    for i in range(7):
        if dices.count(i) == 2:
            return True

    return False


# Verifica daca exista trei zaruri de acelasi tip
def exists_three_of_a_kind(dices):
    for i in range(7):
        if dices.count(i) == 3:
            return True

    return False


# Verifica daca exista 4 zaruri de acelasi tip
def exists_four_of_a_kind(dices):
    for i in range(7):
        if dices.count(i) == 4:
            return True

    return False


# Verifica daca toate elementele din lista a sunt in lista b
def is_sublist(a, b):
    return all(element in b for element in a)


# Verifica daca exista small straight in combinatia de zaruri
def exists_small_straight(dices):
    list_1_4 = [1, 2, 3, 4]
    list_2_5 = [2, 3, 4, 5]
    list_3_6 = [3, 4, 5, 6]

    if (
        is_sublist(list_1_4, dices) or
        is_sublist(list_2_5, dices) or
        is_sublist(list_3_6, dices)
    ):
        return True

    return False


# Verifica daca exista large straight in combinatia de zaruri
def exists_large_straight(dices):
    list_1_5 = [1, 2, 3, 4, 5]
    list_2_6 = [2, 3, 4, 5, 6]

    if is_sublist(list_1_5, dices) or is_sublist(list_2_6, dices):
        return True

    return False


# Calculeaza maximul de scor din combinatiile posibile
def calc_max_score(score):
    max = 0

    for value in score.values():
        if value > max:
            max = value
    return max


# Punctajul fiecarei linii din tabela de scor
def calc_score(counter_dices_numbers, dices):
    score = {}

    # One of a kind
    score["Ones"] = counter_dices_numbers[1]
    score["Twos"] = counter_dices_numbers[2] * 2
    score["Threes"] = counter_dices_numbers[3] * 3
    score["Fours"] = counter_dices_numbers[4] * 4
    score["Fives"] = counter_dices_numbers[5] * 5
    score["Sixes"] = counter_dices_numbers[6] * 6
    score["Three_of_a_kind"] = 0
    score["Four_of_a_kind"] = 0
    score["Full_House"] = 0
    score["Small_straight"] = 0
    score["Large_straight"] = 0
    score["Chance"] = 0
    score["YAHTZEE"] = 0

    # Three of a kind
    if exists_three_of_a_kind(dices) or exists_four_of_a_kind(dices):
        score["Three_of_a_kind"] = calc_sum_dices(dices)

    # Four of a kind
    if exists_four_of_a_kind(dices):
        score["Four_of_a_kind"] = calc_sum_dices(dices)

    # Full House
    if exists_three_of_a_kind(dices) and exists_two_of_a_kind(dices):
        score["Full_House"] = 25

    # Small Straight
    if exists_small_straight(dices):
        score["Small_straight"] = 30

    # Large Straight
    if exists_large_straight(dices):
        score["Large_straight"] = 40

    # YAHTZEE
    for i in range(7):
        if dices.count(i) == 5:
            score["YAHTZEE"] = 50
            break

    # Chance
    score["Chance"] = calc_sum_dices(dices)

    # print(dices, score)
    return score


def calc_values(dices):
    counter_dices_numbers = {}
    for i in range(7):
        counter_dices_numbers[i] = dices.count(i)

    score = calc_score(counter_dices_numbers, dices)
    return score
