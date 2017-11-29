def score(game):
    return change_result(game)


def change_result(game, frame=1, in_first_half=True, result=0):
    STRIKE = "x"
    SPARE = "/"
    for i in range(len(game)):
        if game[i] == SPARE:
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10:
            if game[i] == SPARE:
                result += get_value(game[i + 1])
            elif game[i].lower() == STRIKE:
                result += get_value(game[i + 1])
                if game[i + 2] == SPARE:
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
            in_first_half = True
        if in_first_half:
            in_first_half = False
        if game[i].lower() == STRIKE:
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        return int(char)
    elif char.lower() in ("x", "/"):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


score("1/35XXX458/X3/23")
