import random
from brain_games.game import play
from brain_games.consts import DESCRIPTION_EVEN


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def game_even():
    number = random.randint(1, 100)
    question = f'{number}'
    correct_answer = is_even(number)
    return question, str(correct_answer)


def run_game_even():
    play(game_even, DESCRIPTION_EVEN)
