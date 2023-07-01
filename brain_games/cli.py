import prompt


def welcome_user(return_name=False):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    if return_name is True:
        return name
