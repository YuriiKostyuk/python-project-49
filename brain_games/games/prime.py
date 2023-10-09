import random
from brain_games.cli import welcome_user


def is_prime():
    n = random.randint(1, 10)
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k += 1
    if n < 2:
        correct_answer = 'no'
    elif k <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return n, correct_answer


def prime():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    for _ in range(3):
        n, correct_answer = is_prime()
        print(f"Question: {n}")
        user_answer = input("Your answer ")
        if user_answer != correct_answer:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")