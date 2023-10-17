import random


DESCRIPTION = 'What is the result of the expression?'


def generate_num():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    question = f"Question: {num1} {operator} {num2}"

    if operator == '+':
        right = num1 + num2
    elif operator == '-':
        right = num1 - num2
    else:
        right = num1 * num2

    return question, str(right)
