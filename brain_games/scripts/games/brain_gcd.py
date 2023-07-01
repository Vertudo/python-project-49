import brain_games.scripts.games.core.engine
import random
import math


def main():
    questions = []
    i = 0
    while i < 3:
        prepare_question(questions)

        i += 1

    welcome_text = 'Find the greatest common divisor of given numbers.'
    brain_games.scripts.games.core.engine.run(welcome_text, questions)


def prepare_question(questions: []):
    first_value = random.randint(1, 100)
    second_value = random.randint(1, 100)
    result = math.gcd(first_value, second_value)

    expression = f'{first_value} {second_value}'

    questions.append((expression, str(result)))


if __name__ == '__main__':
    main()
