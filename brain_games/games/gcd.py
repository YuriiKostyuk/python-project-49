from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_GCD
from brain_games.utils import get_rand_num


def get_math_result_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    return num1 + num2


def get_answer_and_result_for_gcd_game():
    num1, num2 = get_rand_num(), get_rand_num()
    question = f"{num1} {num2}"
    correct_answer = get_math_result_gcd(num1, num2)
    return question, str(correct_answer)


def start_gcd_game():
    start_game(get_answer_and_result_for_gcd_game, DESCRIPTION_GCD)
