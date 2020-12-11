class Parent:
    def implicit(self):
        print('PARENT implicit()')


class Child(Parent):
    pass


if __name__ == '__main__':
    dad = Parent()
    son = Child()

    dad.implicit()
    son.implicit()
