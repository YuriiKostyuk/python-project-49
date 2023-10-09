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
    correct_answer = num1 + num2
    return question, correct_answer



def gcd():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for _ in range(3):
        question, correct_answer = generate_num()
        print(question)
        user_answer = int(input("Your answer: "))
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correc!")
        print(f"Congratulations {name}!")