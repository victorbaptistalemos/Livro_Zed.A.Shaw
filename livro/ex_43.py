from sys import exit
from random import randint
from textwrap import dedent


class Scene:
    def enter(self):
        print('This scene is not yet configured.')
        print('Subclass it and implement enter().')
        exit(1)


class Death(Scene):
    quips = (
        'You died. You kinda suck at this.',
        'Your Mom would be proud...if she were smarter.',
        'Such a luser.',
        'I have a small puppy that\'s better at this.',
        'You\'re worse than your Dad\'s jokes.'
    )

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class Finished(Scene):
    def enter(self):
        print('You won! Good job!')
        exit(0)


if __name__ == '__main__':
    x = Finished()
    x.enter()
