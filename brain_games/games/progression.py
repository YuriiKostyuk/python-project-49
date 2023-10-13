import random
from brain_games.cli import welcome_user


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    lenght = random.randint(5, 10)
    progression = [start + step * i for i in range(lenght)]
    hidden_index = random.randint(0, lenght - 1)
    corec = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, corec


def progres():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What number is missing in the progression?")

    for _ in range(3):
        question, corec = generate_progression()
        print("Question:", question)
        user = input("Your answer: ")

        if user != corec:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{corec}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
