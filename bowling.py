STRIKE = "x"
SPARE = "/"
MISS = '-'


def score(game):
    '''Calculating the game's score based on the given input'''
    result = 0
    frame = 1
    in_first_half = True
    last = 0
    game = game.lower()

    for i in range(len(game)):
        result += add_base_points(game[i], last)
        if is_bonus_points_avaiable(frame, game[i]):
            result += add_bonus_points(game, i)

        last = get_value(game[i])
        in_first_half, frame = turn_process(in_first_half, game[i], frame)
    return result


def turn_process(in_first_half, current_turn, frame):
    ''' Counting the rounds to be able to add bonus points if neccessary.'''
    if not in_first_half or current_turn == STRIKE:
        in_first_half = True
        return in_first_half, frame + 1
    else:
        in_first_half = False
        return in_first_half, frame


def add_base_points(current_turn, last):
    '''Increase results with current hit.'''
    if current_turn == SPARE:
        return 10 - last
    else:
        return get_value(current_turn)


def is_bonus_points_avaiable(frame, current_turn):
    '''Returns True if the given condition is true so there will be bonus points'''
    return frame < 10 and current_turn in (STRIKE, SPARE)


def add_bonus_points(game, i):
    '''If with the current hit we achieve Spare the next hit will be added twice,
       If we achieve Strike the next 2 hit will be added twice to results as bonus points.'''
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
