from abc import abstractmethod


class Animal:
    skin = None
    phrase = None
    def __init__(self, species, name) -> None:
        self.name = name
        self.species = species
    
    @abstractmethod
    def speak(self):
        return self.phrase

class Mammal(Animal):

    def __init__(self, name:str, species:str, carnivore:bool) -> None:
        super().__init__(name, species)
        self.skin = 'Hair'
        self.carnivore = carnivore
        # edit this phrase so that mamals speak a specific phrase
        self.phrase = 'Mammal noices'


class Reptile(Animal):

    def __init__(self, name:str, species:str, venomous:bool, carnivore:bool) -> None:
        super().__init__(name, species)
        self.skin = 'Scales'
        self.venomous = venomous
        self.carnivore = carnivore
        # edit this phrase so that reptiles speak a specific phrase
        self.phrase = 'Reptile noices'

class Bird(Animal):
    carnivore = False

    def __init__(self, name:str, species:str, can_fly:bool) -> None:
        super().__init__(name, species)
        self.skin = 'Feathers'
        self.can_fly = can_fly
        # edit this phrase so that birds speak a specific phrase
        self.phrase = 'Bird noices'

class Enclosure:

    def __init__(self, name_or_id:str) -> None:
        self.name_or_id = name_or_id
        self.contained_animals = []
        self.carnivore_containment = None
    
    def animal_to_enclosure(self, animal):
        if self.carnivore_containment is None:
            self.carnivore_containment = animal.carnivore
        
        if animal.carnivore == self.carnivore_containment:
            self.contained_animals.append(animal)
        else:
            if self.carnivore_containment == animal.carnivore:
                print(f'This {animal.name} will be eaten by the other animals in this containment, try again')
            else:
                print(f'This {animal.name} will eat the other animals in this containment, try again')

    def add_animal(self, animals):
        if type(animals) is list:
            for i in animals:
                self.animal_to_enclosure(i)
        else:
            self.animal_to_enclosure(animals)

    def number_of_animals(self):
        return len(self.contained_animals)
    
    def types_of_animals(self):
        result = [animal.species + ', ' + animal.name for animal in self.contained_animals]
        return result

class zoo:
    name = 'Place holder'
    enclosures = []
    def add_enclosure(self, enclosure):
        if type(enclosure) is Enclosure:
            self.enclosures.append(enclosure)
        else:
            print(f'{type(enclosure)} is not an enclosure')

    def print_facts(self):
        total_animals = 0
        enclosure_facts = []
        for enclosure in self.enclosures:
            total_animals += enclosure.number_of_animals()
            enclosure_facts.append((enclosure.name_or_id, enclosure.types_of_animals()))
    
        print(f'The total number of animals in the zoo is: {total_animals}')
        for i in enclosure_facts:
            print(f'In enclosure {i[0]} there are {len(i[1])} animals, theese are: {i[1]}')
        
        for enclosure in self.enclosures:
            for animal in enclosure.contained_animals:
                if type(animal) is Mammal or type(animal) is Reptile:
                    if animal.carnivore is True:
                        diet = 'Carnivorus'
                    else:
                        diet = 'Herbivorus'

                if type(animal) is Reptile:
                    if animal.venomous is True:
                        poison = ''
                    else:
                        poison = 'not'

                if type(animal) is Bird:
                    if animal.can_fly is True:
                        can_fly = ''
                    else:
                        can_fly = 'not'


                if type(animal) is Mammal:
                    print(f'We have a {animal.name}, species: {animal.species}, diet: {diet}')
                elif type(animal) is Reptile:
                    print(f'We have a {animal.name}, species: {animal.species}, diet: {diet} animal, they are {poison} poisonus')
                elif type(animal) is Bird:
                    print(f'We have a {animal.name}, species: {animal.species}, they can {can_fly} fly')
zoo = zoo()              

# create animals
mammal1 = Mammal('Ferela', 'lion', True)
mammal2 = Mammal('Leatboon', 'lemur', False)
mammal3 = Mammal('Doonok', 'donkey', False)
mammal4 = Mammal('Lurtacar', 'lemur', False)
reptile1 = Reptile('Fereetteoci', 'frog', False, False)
reptile2 = Reptile('Snakossum', 'snake', True, True)
reptile3 = Reptile('Citigator', 'crocodile', False, True)
bird1 = Bird('Flautingo', 'flamingo', True)
bird2 = Bird('Malliceo', 'parrot', True)
bird3 = Bird('Tucoda', 'penguin', False)
# create enclosures and add animals
enclosure1 = Enclosure('1')
enclosure1.add_animal(mammal2)
enclosure1.add_animal(mammal3)
enclosure1.add_animal(mammal4)
enclosure2 = Enclosure('2')
enclosure2.add_animal(bird3)
enclosure2.add_animal(mammal1)
enclosure2.add_animal(reptile3)
enclosure3 = Enclosure('3')
enclosure3.add_animal(reptile1)
enclosure3.add_animal(reptile2)
enclosure4 = Enclosure('4')
enclosure4.add_animal(bird1)
enclosure4.add_animal(bird2)

# add enclosures to zoo
zoo.add_enclosure(enclosure1)
zoo.add_enclosure(enclosure2)
zoo.add_enclosure(enclosure3)
zoo.add_enclosure(enclosure4)
# these should produce error message in console, they are not enclosures!
zoo.add_enclosure(bird1)
zoo.add_enclosure(zoo)
# print animal facts n’ stuff
print(mammal3.speak())
print(reptile2.speak())
print(bird1.speak())
zoo.print_facts()
