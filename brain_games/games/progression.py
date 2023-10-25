import random
from brain_games.engine import play
from brain_games.consts import DESCRIPTION_PROGRESSION


def play_progression_game():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    lenght = random.randint(5, 10)
    progression = [start + step * i for i in range(lenght)]
    hidden_index = random.randint(0, lenght - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, str(correct_answer)


def start_progression_game():
    play(play_progression_game, DESCRIPTION_PROGRESSION)
