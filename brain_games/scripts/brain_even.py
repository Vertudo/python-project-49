import brain_games.scripts.brain_games
import random
import prompt


def main():
    name = brain_games.scripts.brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    total_correct_answers = 3
    while i < total_correct_answers:
        number = random.randint(1, 100)
        even = number % 2
        correct_answer = 'yes' if even == 0 else 'no'

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            break
        else:
            print('Correct!')

        i += 1

    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
