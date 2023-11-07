import random
from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_CALC, MATH_OPERATORS
from brain_games.utils import get_rand_num


def get_math_result_by_sign(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise ValueError('Unsupported operator')


def get_data_for_calc_game():
    num1, num2 = get_rand_num(), get_rand_num()
    operator = random.choice(MATH_OPERATORS)

    question = f"Question: {num1} {operator} {num2}"
    correct_answer = get_math_result_by_sign(num1, num2, operator)

    return question, str(correct_answer)


def start_calc_game():
    start_game(get_data_for_calc_game, DESCRIPTION_CALC)
