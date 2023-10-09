import random


def welcome_user():
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


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


def main():
    print("Welcome to the Brain Game")
    name = welcome_user()
    print("What is the result of the expression?")
    for _ in range(3):
        question, correct_answer = generate_num()
        print(question)
        user_answer = int(input("Your answer: "))
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
