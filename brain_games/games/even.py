from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_EVEN
from brain_games.utils import get_rand_num


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def get_data_for_even_game():
    number = get_rand_num()
    question = f'{number}'
    correct_answer = is_even(number)
    return question, str(correct_answer)


def start_even_game():
    start_game(get_data_for_even_game, DESCRIPTION_EVEN)
