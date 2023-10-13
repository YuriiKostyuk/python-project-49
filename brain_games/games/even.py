import random
from brain_games.cli import welcome_user


def is_even(number):  # Эта функция проверяет число на четность
    if number % 2 == 0:
        return True
    else:
        return False


def generate_num():  # генерируем случайное число
    number = random.randint(1, 100)
    num = str(number)
    corect = "yes" if is_even(number) else "no"
    return num, corect


def even():
    print("Welcome to the Brain Game")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):  # 3 вопроса
        num, corect = generate_num()
        print("Question:", num)
        user = input("Your answer: ")
        if user != corect:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{corect}'")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
