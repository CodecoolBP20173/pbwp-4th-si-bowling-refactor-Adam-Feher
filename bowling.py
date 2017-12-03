STRIKE = "x"
SPARE = "/"
MISS = '-'

def score(game):
    result = 0
    frame = 1
    in_first_half = True
    last = 0
    return change_score(game, frame, in_first_half, result, last)

def change_score(game, frame, in_first_half, result, last):
    game = game.lower()
    for i in range(len(game)):
        result += add_base_points(game[i], last)
        if is_add_bonus_points_available(frame, game[i]):
            result += add_bonus_points(game, i)
        last = get_value(game[i])

        if not in_first_half or game[i] == STRIKE:
            in_first_half = True
            frame += 1
        else:
            in_first_half = False
    return result

def add_base_points(current_turn, last):
    if current_turn == SPARE:
        return 10 - last
    else:
        return get_value(current_turn)

def is_add_bonus_points_available(frame, current_turn):
    return frame < 10 and current_turn in (STRIKE, SPARE)


def add_bonus_points(game, i):
    if game[i] == SPARE:
        return get_value(game[i + 1])
    elif game[i] == STRIKE:
        if game[i + 2] == SPARE:
            return get_value(game[i + 1]) + 10 - get_value(game[i + 1])
        else:
            return get_value(game[i + 1]) + get_value(game[i + 2])


def get_value(char):
    try:
        char = int(char)
        if 1 <= char and char <= 9:
            return char

    except ValueError:
        if char in (STRIKE, SPARE):
            return 10
        elif char == MISS:
            return 0
        else:
            raise ValueError()