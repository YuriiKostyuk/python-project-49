from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_EVEN
from brain_games.utils import ganerate_random_number


def check_evenness(number):
    return 'yes' if number % 2 == 0 else 'no'


def result_even_game():
    number = ganerate_random_number()
    question = f'{number}'
    correct_answer = check_evenness(number)
    return question, str(correct_answer)


def start_even_game():
    start_game(result_even_game, DESCRIPTION_EVEN)
