from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_GCD
from brain_games.utils import generate_random_numbers


def euclidean_algorithm(num1, num2):
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    return num1 + num2


def result_gcd_game():
    num1, num2 = generate_random_numbers()
    question = f"Question: {num1} {num2}"
    correct_answer = euclidean_algorithm(num1, num2)
    return question, str(correct_answer)


def start_gcd_game():
    start_game(result_gcd_game, DESCRIPTION_GCD)
