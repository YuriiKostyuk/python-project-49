import random
from brain_games.game_engine import play
from brain_games.consts import DESCRIPTION_PRIME



def game_prime():
    question = random.randint(1, 10)
    k = 0
    for i in range(2, question // 2 + 1):
        if (question % i == 0):
            k += 1
    if question < 2:
        right = 'no'
    elif k <= 0:
        right = 'yes'
    else:
        right = 'no'
    return question, str(right)


def run_game_prime():
    play(game_prime, DESCRIPTION_PRIME)
