class Other:
    def implicit(self):
        print('OTHER implicit()')

    def override(self):
        print('OTHER override()')

    def altered(self):
        print('OTHER altered()')


class Child:
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print('CHILD override()')

    def altered(self):
        print('CHILD, BEFORE OTHER altered()')
        self.other.altered()
        print('CHILD, AFTER OTHER altered()')


if __name__ == '__main__':
    son = Child()

    son.implicit()
    print()
    son.override()
    print()
    son.altered()
