from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_PRIME
from brain_games.utils import ganerate_random_number


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if not (number % i):
            return False
    return True


def result_prime_game():
    number = ganerate_random_number()
    question = number
    correct_answer = is_prime(number) and 'yes' or 'no'
    return question, str(correct_answer)


def start_prime_game():
    start_game(result_prime_game, DESCRIPTION_PRIME)
