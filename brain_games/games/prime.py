from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_PRIME
from brain_games.utils import get_rand_num


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    return True


def get_answer_and_result_for_prime_game():
    number = get_rand_num()
    question = number
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, str(correct_answer)


def start_prime_game():
    start_game(get_answer_and_result_for_prime_game, DESCRIPTION_PRIME)
