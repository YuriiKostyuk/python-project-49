import prompt
from brain_games.consts import NUMBER_OF_ROUNDS


def start_game(game_result, game_instructions):
    user_name = prompt.string('Welcome to the Brain Games! \n'
                              'May I have your name? ')
    print(f"Hello, {user_name}!\n{game_instructions}")
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game_result()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is the wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
