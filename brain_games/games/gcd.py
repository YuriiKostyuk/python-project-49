import random
from brain_games.cli import welcome_user


def generate_num():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"Question: {num1} {num2}"
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    corec = num1 + num2
    return question, corec


def gcd():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for _ in range(3):
        question, corec = generate_num()
        print(question)
        user = int(input("Your answer: "))
        if user != corec:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{corec}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
