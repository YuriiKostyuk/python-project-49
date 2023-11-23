import math
from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_GCD
from brain_games.utils import get_rand_num


def get_gcd(num1, num2):
    return math.gcd(num1, num2)


def get_a_pair_of_number_and_gcd():
    num1, num2 = get_rand_num(), get_rand_num()
    pair_of_numbers = f"{num1} {num2}"
    gcd = get_gcd(num1, num2)
    return pair_of_numbers, str(gcd)


def start_gcd_game():
    start_game(get_a_pair_of_number_and_gcd, DESCRIPTION_GCD)
