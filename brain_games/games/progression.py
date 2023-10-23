import random
from brain_games.game import play
from brain_games.consts import DESCRIPTION_PROGRESSION


def game_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    lenght = random.randint(5, 10)
    progression = [start + step * i for i in range(lenght)]
    hidden_index = random.randint(0, lenght - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, str(correct_answer)


def run_game_progression():
    play(game_progression, DESCRIPTION_PROGRESSION)
