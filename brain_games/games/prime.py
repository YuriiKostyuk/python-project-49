import random
from brain_games.game import play
from brain_games.consts import DESCRIPTION_PRIME


def is_prime(number):
    is_prime = (
        'yes' if number >= 2 and
        all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
        else 'no'
    )
    return is_prime


def game_prime():
    number = random.randint(1, 10)
    question = number
    correct_answer = is_prime(number)
    return question, str(correct_answer)


def run_game_prime():
    play(game_prime, DESCRIPTION_PRIME)
