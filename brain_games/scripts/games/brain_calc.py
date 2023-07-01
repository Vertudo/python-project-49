import brain_games.scripts.games.core.engine
import random


def main():
    questions = []
    i = 0
    while i < 3:
        operators = ['+', '-', '*']
        operator = random.choice(operators)
        first_value = random.randint(1, 100)
        second_value = random.randint(1, 100)

        result = 0
        match operator:
            case '+':
                result = first_value + second_value

            case '-':
                result = first_value - second_value

            case '*':
                result = first_value * second_value

        expression = f'{first_value} {operator} {second_value}'

        questions.append((expression, str(result)))

        i += 1

    welcome_text = 'What is the result of the expression?'
    brain_games.scripts.games.core.engine.run(welcome_text, questions)


if __name__ == '__main__':
    main()
