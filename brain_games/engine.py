import prompt
from brain_games.consts import ROUND_COUNT


def play(game, description):
    print('Welcome to thee Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"""\
Hello, {name}!
{description}""")
    for _ in range(ROUND_COUNT):
        question, correct_answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    else:
        print(f"Congratulations, {name}!")
