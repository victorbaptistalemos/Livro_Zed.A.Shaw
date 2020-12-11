class Parent:
    def implicit(self):
        print('PARENT implicit()')

    def override(self):
        print('PARENT override()')

    def altered(self):
        print('PARENT altered()')


class Child(Parent):
    def override(self):
        print('CHILD override()')

    def altered(self):
        print('CHILD, BEFORE PARENT altered()')
        super().altered()
        print('CHILD, AFTER PARENT altered()')


if __name__ == '__main__':
    dad = Parent()
    son = Child()
    print()
    dad.implicit()
    son.implicit()
    print()
    dad.override()
    son.override()
    print()
    dad.altered()
    son.altered()
