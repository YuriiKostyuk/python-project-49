import random
from brain_games.cli import welcome_user


def is_prime():
    n = random.randint(1, 10)
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k += 1
    if n < 2:
        corec = 'no'
    elif k <= 0:
        corec = 'yes'
    else:
        corec = 'no'
    return n, corec


def prime():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        n, corec = is_prime()
        print(f"Question: {n}")
        user = input("Your answer ")
        if user != corec:
            print(f'"{user}" is wrong answer ;(. Correct answer was "{corec}"')
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
