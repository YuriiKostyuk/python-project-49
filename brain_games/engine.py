import prompt
from brain_games.consts import ROUND_COUNTS


def start_game(get_answer, description):
    print('Welcome to thee Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!\n{description}")
    for _ in range(ROUND_COUNTS):
        question, correct_answer = get_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is the wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
