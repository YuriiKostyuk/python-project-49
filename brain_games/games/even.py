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
    correct_answer = "yes" if is_even(number) else "no"
    return num, correct_answer


def even():
    print("Welcome to the Brain Game")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):  # 3 вопроса
        num, correct_answer = generate_num()
        print("Question:", num)
        user_answer = input("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
