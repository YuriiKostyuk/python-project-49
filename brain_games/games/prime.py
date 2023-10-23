import random
from brain_games.game import play
from brain_games.consts import DESCRIPTION_PRIME


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if not (number % i):
            return False
    return True


def game_prime():
    number = random.randint(1, 10)
    question = number
    correct_answer = is_prime(number) and 'yes' or 'no'
    return question, str(correct_answer)


def run_game_prime():
    play(game_prime, DESCRIPTION_PRIME)
