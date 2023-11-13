from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_EVEN
from brain_games.utils import get_rand_num


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def get_the_required_even_game_number_and_answer():
    number = get_rand_num()
    correct_answer = is_even(number)
    return number, str(correct_answer)


def start_even_game():
    start_game(get_the_required_even_game_number_and_answer, DESCRIPTION_EVEN)
