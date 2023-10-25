import random
from brain_games.engine import play
from brain_games.consts import DESCRIPTION_GCD


def perform_operation(num1, num2):
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    return num1 + num2


def play_gcd_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"Question: {num1} {num2}"
    correct_answer = perform_operation(num1, num2)
    return question, str(correct_answer)


def start_gcd_game():
    play(play_gcd_game, DESCRIPTION_GCD)
