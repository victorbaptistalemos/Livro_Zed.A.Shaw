from sys import exit
from random import randint
from textwrap import dedent


class Scene:
    def enter(self):
        print('This scene is not yet configured.')
        print('Subclass it and implement enter().')
        exit(1)


if __name__ == '__main__':
    x =  Scene()
    x.enter()
