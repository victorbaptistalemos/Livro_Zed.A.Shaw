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


class LaserWeaponArmory:
    def enter(self):
        print(dedent('''
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might up be hiding. It's dead
            quiet, too quiet. You stand up and run the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need to code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
        '''))

        code = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        guesses = 0

        while True:
            guess = input('[keyboard]> ')
            guesses += 1 if guess != code else 0

            if guess == code:
                print(dedent('''
                    The container clicks and open the seal breaks, letting
                    gas out. You grab the neutron bomb and run as fast as fast
                    as you can to the bridge where you must place it in the
                    right spot.
                '''))
                return 'the_bridge'
            elif guesses >= 10:
                print(dedent('''
                    The lock buzzes one last time and then you hear a
                    sickening melton sound as the mechanism is fused
                    together. You decide to sit there, and finally the
                    Gothons blow up the ship from their ship and you die.
                '''))
                return 'death'
            elif len(guess) == 3:
                for i in range(0, 3):
                    print('' if guess[i] == code[i] else 'BZZ', end='')
                print()
            else:
                print('BZZZZEDDD!')


class TheBridge(Scene):
    def enter(self):
        print(dedent('''
            You burst onto the Bridge with the neutron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship. Each of them has an even uglier
            clown costume than the last. They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
        '''))

        print(dedent('''
            Actions:
            1. Slowly place the bomb
            2. Throw the bomb
        '''))

        action = input('> ')

        if action == '1':
            print(dedent('''
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb to the floor, pointing your
                blaster at it. You then jump back through the door,
                punch the close door and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
            '''))
            return 'escape_pod'

        elif action == '2':
            print(dedent('''
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as you drop it a
                Gothon shoots you right in the back killing you. As
                you die you see another Gothon fantically try to
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
            '''))
            return 'death'

        else:
            print(dedent('''
                While you're thinking about what to do a Gothon pulled his
                weapon desperately and shot the bomb. Well, everybody was
                killed in that action.
            '''))
            return 'death'


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
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
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
    x_map = Map('laser_weapon_armory')
    x_game = Engine(x_map)
    x_game.play()
