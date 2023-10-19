import random
from brain_games.game_engine import play
from brain_games.consts import DESCRIPTION_EVEN


def game_even():
    number = random.randint(1, 100)
    question = f'{number}'
    right = number % 2 and 'no' or 'yes'
    return question, str(right)


def run_game_even():
    play(game_even, DESCRIPTION_EVEN)
