import random
from brain_games.engine import start_game
from brain_games.consts import DESCRIPTION_PROGRESSION


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [start + step * i for i in range(length)]
    return progression, start, step


def hide_progression_value(progression, index):
    hidden_value = progression[index]
    progression[index] = '..'
    return progression, str(hidden_value)


def get_answer_and_result_progression_game():
    progression, start, step = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    progression_with_hidden_value, correct_answer = hide_progression_value(progression, hidden_index)
    question = ' '.join(str(i) for i in progression_with_hidden_value)
    return question, str(correct_answer)


def start_progression_game():
    start_game(get_answer_and_result_progression_game, DESCRIPTION_PROGRESSION)
