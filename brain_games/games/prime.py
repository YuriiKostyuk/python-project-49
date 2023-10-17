import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_num():
    question = random.randint(1, 10)
    k = 0
    for i in range(2, question // 2 + 1):
        if (question % i == 0):
            k += 1
    if question < 2:
        right = 'no'
    elif k <= 0:
        right = 'yes'
    else:
        right = 'no'
    return question, str(right)
