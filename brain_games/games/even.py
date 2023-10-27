import random
from brain_games.engine import play
from brain_games.consts import DESCRIPTION_EVEN


def check_evenness(number):
    return 'yes' if number % 2 == 0 else 'no'


def result_even_game():
    number = random.randint(1, 100)
    question = f'{number}'
    correct_answer = check_evenness(number)
    return question, str(correct_answer)


def start_even_game():
    play(result_even_game, DESCRIPTION_EVEN)
