import prompt
from brain_games.constants import ROUND_COUNT


def play(game):
    print('Welcome to thee Brain Games!')
    name = prompt.string('May i have your name?')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for _ in range(ROUND_COUNT):
        question, right = game.generate_num()
        print(f'Question: {question}')
        user = prompt.string('Your answer: ')
        if user != right:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f"Congratulations, {name}!")
