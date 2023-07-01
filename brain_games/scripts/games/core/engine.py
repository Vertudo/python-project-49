import brain_games.scripts.brain_games
import prompt


def run(welcome_text: str, questions: []):
    name = brain_games.scripts.brain_games.main()
    print(welcome_text)
    i = 0
    for elem in questions:
        question, correct_answer = elem
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            break
        else:
            print('Correct!')

        i += 1

    total_correct_answers = 3
    if i == total_correct_answers:
        print(f'Congratulations, {name}!')
