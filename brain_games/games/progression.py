import random
from brain_games.cli import welcome_user


def generate_progression():
    start = random.randint(1, 10)  # Генерируем начало прогрессии
    step = random.randint(1, 10)  # Генерируем шаг прогрессии
    lenght = random.randint(5, 10)  # Генерируем длину прогрессии
    progression = [start + step * i for i in range(lenght)]  # Генерация прогрессии
    hidden_index = random.randint(0, lenght - 1)  # Выбор индекса числа, которое нужно скрыть
    correct_answer = str(progression[hidden_index])  # Верный ответ
    progression[hidden_index] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, correct_answer


def progres():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What number is missing in the progression?")

    for _ in range(3):
        question, correct_answer = generate_progression()
        print("Question:", question)
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
