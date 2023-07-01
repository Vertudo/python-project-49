#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main(return_name=False):
    print('Welcome to the Brain Games!')
    return welcome_user(return_name)


if __name__ == '__main__':
    main()
