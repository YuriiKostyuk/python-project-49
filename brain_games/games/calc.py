import random
from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_CALC
from brain_games.utils import generate_random_numbers


def perform_math_operation(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise ValueError('Unsupported operator')


def answer_calc_game():
    num1, num2 = generate_random_numbers()
    operator = random.choice(['+', '-', '*'])

    question = f"Question: {num1} {operator} {num2}"
    correct_answer = perform_math_operation(num1, num2, operator)

    return question, str(correct_answer)


def start_calc_game():
    start_game(answer_calc_game, DESCRIPTION_CALC)
