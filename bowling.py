STRIKE = "x"
SPARE = "/"
MISS = '-'

def score(game):
    result = 0
    frame = 1
    in_first_half = True
    return change_score(game, frame, in_first_half, result)

def change_score(game, frame, in_first_half, result):
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])

        if not in_first_half or game[i].lower() == STRIKE:
            in_first_half = True
            frame += 1
        else:
            in_first_half = False
    return result


def get_value(char):
    try:
        char = int(char)
        if 1 <= char and char <= 9:
            return char

    except ValueError:
        if char.lower() in (STRIKE, SPARE):
            return 10
        elif char.lower() == MISS:
            return 0
        else:
            raise ValueError()