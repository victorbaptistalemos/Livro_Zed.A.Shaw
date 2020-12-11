class Parent:
    def altered(self):
        print('PARENT altered()')


class Child(Parent):
    def altered(self):
        print('CHILD, BEFORE PARENT altered()')
        super().altered()
        print('CHILD, AFTER PARENT altered()')


if __name__ == '__main__':
    dad = Parent()
    son = Child()

    dad.altered()
    son.altered()
