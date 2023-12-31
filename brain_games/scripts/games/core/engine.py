import brain_games.scripts.brain_games
import prompt


def run(welcome_text: str, questions: []):
    name = brain_games.scripts.brain_games.main(True)
    print(welcome_text)
    i = 0
    for elem in questions:
        question, correct_answer = elem
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            text = f'\'{answer}\' is wrong answer ;(. ' \
                   f'Correct answer was \'{correct_answer}\'.'
            print(text)
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')

        i += 1

    total_correct_answers = 3
    if i == total_correct_answers:
        print(f'Congratulations, {name}!')
