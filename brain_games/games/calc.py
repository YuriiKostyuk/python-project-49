import random
from brain_games.cli import welcome_user


def generate_num():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    operator = random.choice(['+', '-', '*'])

    question = f"Question: {num1} {operator} {num2}"

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return question, correct_answer


def calc():
    print("Welcome to the Brain Game")
    name = welcome_user()
    print("What is the result of the expression?")
    for _ in range(3):
        question, corect = generate_num()
        print(question)
        user = int(input("Your answer: "))
        if user != corect:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{corect}'")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
