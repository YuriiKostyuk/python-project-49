import random
from brain_games.game import play
from brain_games.consts import DESCRIPTION_CALC


def is_calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def game_calc():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    question = f"Question: {num1} {operator} {num2}"
    correct_answer = is_calc(num1, num2, operator)

    return question, str(correct_answer)


def run_game_calc():
    play(game_calc, DESCRIPTION_CALC)
