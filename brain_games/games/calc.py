import random
from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_CALC, MATH_OPERATORS
from brain_games.utils import get_rand_num


def get_math_result_by_sign(num1, num2, sign):
    match sign:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise ValueError('Unsupported operator')


def get_math_expression_and_result():
    num1, num2 = get_rand_num(), get_rand_num()
    sign = random.choice(MATH_OPERATORS)

    math_expression = f"{num1} {sign} {num2}"
    result = get_math_result_by_sign(num1, num2, sign)

    return math_expression, str(result)


def start_calc_game():
    start_game(get_math_expression_and_result, DESCRIPTION_CALC)
