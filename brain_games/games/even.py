from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_EVEN
from brain_games.utils import get_rand_num


def check_evenness(number):
    return 'yes' if number % 2 == 0 else 'no'


def get_result_even_game():
    number = get_rand_num()
    question = f'{number}'
    correct_answer = check_evenness(number)
    return question, str(correct_answer)


def start_even_game():
    start_game(get_result_even_game, DESCRIPTION_EVEN)
