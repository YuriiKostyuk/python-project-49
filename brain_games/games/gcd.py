import random
from brain_games.game_engine import play
from brain_games.consts import DESCRIPTION_GCD


def game_gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"Question: {num1} {num2}"
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    right = num1 + num2
    return question, str(right)


def run_game_gcd():
    play(game_gcd, DESCRIPTION_GCD)
