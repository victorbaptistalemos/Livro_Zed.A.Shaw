class Parent:
    def override(self):
        print('PARENT override()')


class Child(Parent):
    def override(self):
        print('CHILD override()')


if __name__ == '__main__':
    dad = Parent()
    son = Child()

    dad.override()
    son.override()
