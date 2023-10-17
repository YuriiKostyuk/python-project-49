import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_num():
    number = random.randint(1, 100)
    question = f'{number}'
    right = number % 2 and 'no' or 'yes'
    return question, str(right)
