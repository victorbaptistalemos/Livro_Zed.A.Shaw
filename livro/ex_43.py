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


class EscapePod(Scene):
    def enter(self):
        print(dedent('''
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference. You get to the chamber with the
            escape pods, and now you neeed to pick one to take. Some of
            them could be damaged but you don't have time to look.
            There's 5 pods, which one do you take?
        '''))

        good_pod = randint(1, 5)
        guesses = 0

        while True:
            guess = input('[pod]> ')
            guess = int(guess) if str.isdigit(guess) else 0

            if not 1 <= guess <= 5 and guesses < 5:
                guesses += 1
                print(f'{guess} is not a valid pod number. Try again!')

            if guesses >= 5:
                print(dedent('''
                    While you're playing around not choosing a valid pod number
                    a Gothon came and shot you right to the head killing you.
                '''))
                return 'death'
            elif guess == good_pod:
                print(dedent(f'''
                    You jump into pod #{guess} and hit the eject button.
                    The pod easily slides out into space heading to the
                    planet below. As it flies to the planet, you look
                    back and see your ship implode then explode like a
                    bright star, taking out the Gothon ship at the same
                    time. You won!
                '''))
                return 'finished'
            else:
                print(dedent(f'''
                    You jump into pod #{guess} and hit the eject button.
                    The pod escapes out into the void of space, then
                    implodes as the hull ruptures, crushing your body into
                    jam jelly.
                '''))
                return 'death'


class Finished(Scene):
    def enter(self):
        print('You won! Good job!')
        exit(0)


class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # Map.opening_scene() -- Composição de objetos
        current_scene = self.scene_map.opening_scene()
        # Map.next_scene() -- Composição de objetos
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Map:
    scenes = {
        'death': Death(),
        'escape_pod': EscapePod(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


if __name__ == '__main__':
    x_map = Map('escape_pod')
    x_game = Engine(x_map)
    x_game.play()
