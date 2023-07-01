import brain_games.scripts.games.core.engine
import random


def main():
    questions = []
    i = 0
    while i < 3:
        prepare_question(questions)

        i += 1

    welcome_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_games.scripts.games.core.engine.run(welcome_text, questions)


def prepare_question(questions: []):
    number = random.randint(1, 100)
    result = is_prime_number(number)
    correct_answer = 'yes' if result is True else 'no'

    expression = f'{number}'

    questions.append((expression, correct_answer))


def is_prime_number(number):
    if number == 1:
        return False
    for i in range(2, number):
        if (number % i) == 0:
            return False

    return True


if __name__ == '__main__':
    main()
