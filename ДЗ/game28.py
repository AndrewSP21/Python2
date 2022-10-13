import random


def first_move(player1, player2):
    res = random.choice([player1, player2])
    return res


def next_move_clever(start):
    if not start % 2 and start >= 30:
        res = 1
    elif start % 2 and start >= 31:
        res = 2
    elif start <= 28:
        res = start
    else:
        res = 28
    return res
