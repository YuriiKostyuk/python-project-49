import random
from brain_games.game_engine import play
from brain_games.consts import DESCRIPTION_CALC


def game_calc():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    question = f"Question: {num1} {operator} {num2}"

    if operator == '+':
        right = num1 + num2
    elif operator == '-':
        right = num1 - num2
    else:
        right = num1 * num2

    return question, str(right)


def run_game_calc():
    play(game_calc, DESCRIPTION_CALC)
