import random
from brain_games.engine import play
from brain_games.consts import DESCRIPTION_CALC


def perform_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def play_calc_game():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    question = f"Question: {num1} {operator} {num2}"
    correct_answer = perform_operation(num1, num2, operator)

    return question, str(correct_answer)


def start_calc_game():
    play(play_calc_game, DESCRIPTION_CALC)
