import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_num():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    lenght = random.randint(5, 10)
    progression = [start + step * i for i in range(lenght)]
    hidden_index = random.randint(0, lenght - 1)
    right = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, str(right)
