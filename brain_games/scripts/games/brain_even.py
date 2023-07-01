import brain_games.scripts.games.core.engine
import random


def main():
    questions = []
    i = 0
    while i < 3:
        number = random.randint(1, 100)
        even = number % 2
        correct_answer = 'yes' if even == 0 else 'no'

        questions.append((number, correct_answer))

        i += 1

    welcome_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    brain_games.scripts.games.core.engine.run(welcome_text, questions)


if __name__ == '__main__':
    main()
