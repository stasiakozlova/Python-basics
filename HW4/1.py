class SpaceObject:

    def __init__(self, name):
        self.name = name

class Planet(SpaceObject):

    population = 0

    def __init__(self, name):
        super().__init__(name)

    def add_animal(self, animal):
        print(f'Welcome to {self.name}, {animal.name}!')
        self.population += 1

    def __str__(self):
        return f'I am planet {self.name} with population {self.population}.'

class Animal:

    amount = 0
    cubs = 0

    def __init__(self, name):
        self.name = name
        self.amount += 1

    def reproduce(self, number):
        self.cubs += number
        print(f'{self.name} has just given birth to {number} kids and has {self.cubs} kids in total.')
        while number:
            cub = Animal(f"{self.name}'s cub")
            earth.add_animal(cub)
            number -= 1

    def expand_habitat(self, territory):
        self.habitat.append(territory)
        for territory in self.habitat:
            print(f'{self.name} lives in {territory}.')

    def __str__(self):
        return f'I am animal {self.name}.'

class Carnivorous(Animal):

    flesh_eaten = 0
    habitat = []

    def __init__(self, name):
        super().__init__(name)

    def eat_flesh(self, amount):
        self.flesh_eaten += amount
        print(f'{self.name} has just eaten {amount} antelopes and has eaten {self.flesh_eaten} antelopes in total.')

class Herbivorous(Animal):

    grass_eaten = 0
    habitat = []

    def __init__(self, name):
        super().__init__(name)

    def eat_grass(self, amount):
        self.grass_eaten += amount
        print(f'{self.name} has just eaten {amount} plants and has eaten {self.grass_eaten} plants in total.')

class Omnivorous(Animal):

    seeds_eaten = 0
    habitat = []

    def __init__(self, name):
        super().__init__(name)

    def eat_seeds(self, amount):
        self.seeds_eaten += amount
        print(f'{self.name} has just eaten {amount} walnuts and has eaten {self.seeds_eaten} walnuts in total.')

earth = Planet('Earth')
print(f'{earth}\n')

eagle = Omnivorous('Eagle')
print(eagle)
earth.add_animal(eagle)
eagle.eat_seeds(10)
eagle.expand_habitat('North America')
eagle.reproduce(5)
eagle.expand_habitat('Australia')
eagle.reproduce(3)
print(f'{earth}\n')

ox = Herbivorous('Ox')
print(ox)
earth.add_animal(ox)
ox.eat_grass(17)
ox.expand_habitat('Eurasia')
ox.reproduce(2)
ox.eat_grass(15)
ox.expand_habitat('Southern America')
ox.reproduce(2)
print(f'{earth}\n')

lion = Carnivorous('Lion')
print(lion)
earth.add_animal(lion)
lion.eat_flesh(3)
lion.expand_habitat('Africa')
lion.reproduce(4)
lion.eat_flesh(7)
lion.reproduce(5)
print(f'{earth}\n')
