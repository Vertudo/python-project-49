import brain_games.scripts.games.core.engine
import random


def main():
    questions = []
    i = 0
    while i < 3:
        prepare_question(questions)

        i += 1

    welcome_text = 'What number is missing in the progression?'
    brain_games.scripts.games.core.engine.run(welcome_text, questions)


def prepare_question(questions: []):
    start_value = random.randint(1, 20)
    inc_value = random.randint(1, 10)
    length = 10
    progression = list(range(start_value, inc_value * length + start_value + 1, inc_value))

    index = random.randint(1, 10)
    number = progression[index]
    progression[index] = '..'

    expression = ''
    for elem in progression:
        expression += str(elem) + ' '

    expression.strip()

    questions.append((expression, str(number)))


if __name__ == '__main__':
    main()
