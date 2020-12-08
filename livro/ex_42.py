## Animal é-um objeto
# class Animal(object):
# Para simplificar
class Animal:
    pass


# A classe Dog é-um Animal
class Dog(Animal):
    def __init__(self, name):
        # O atributo name do objeto da classe Dog, nesse caso, o parâmetro self
        # recebe o paâmetro name
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name):
        self.name = name

        # Person tem-um pet de algum tipo
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        # Employee herda tudo de Person
        # No caso o atributo name
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish:
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

# rover é-um Dog
rover = Dog('Rover')

# satan é-um Cat
satan = Cat('Satan')

# mary é-um Pessoa
mary = Person('Mary')

# mary tem-um pet do tipo Cat
mary.pet = satan

# frank é-um Employee que é-um Person
frank = Employee('Frank', 120_000)

# frank tem-um pet do tipo Dog
frank.pet = rover

flipper = Fish()
crouse = Salmon()
harry = Halibut()
