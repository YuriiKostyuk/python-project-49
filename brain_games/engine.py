import prompt
from brain_games.consts import ROUND_COUNT


def play(launch, description):
    print('Welcome to thee Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!\n{description}")
    for _ in range(ROUND_COUNT):
        question, correct_answer = launch()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is the wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
