import unittest


class AnimalShelter():

    def __init__ (self, animal_list=None, animal_type=None):

        if len(animal_list) != len(animal_type):
            print("messed up initialization")

        self.dog_queue = []
        self.cat_queue = []

        self.id = 0

        for i, animal in enumerate(animal_list):
            if animal_type[i] == 'Dog':
                animal = Dog(animal_list[i], self.id)
                self.dog_queue.append(animal)
                self.id += 1
            else:
                animal = Cat(animal_list[i], self.id)
                self.cat_queue.append(animal)
                self.id += 1

    def dequeueAnimal(self):

        if len(self.dog_queue) and len(self.cat_queue):
            dog = self.dog_queue[0]
            cat = self.cat_queue[0]

            if dog.animalID < cat.animalID:
                if len(self.dog_queue) < 1:
                    return None
                animal = self.dog_queue[0]
                self.dog_queue = self.dog_queue[1:]
            else:
                if len(self.cat_queue) < 1:
                    return None
                animal = self.cat_queue[0]
                self.cat_queue = self.cat_queue[1:]

            return animal
        else:
            if len(self.dog_queue) < 1:
                animal = self.cat_queue[0]
                self.cat_queue = self.cat_queue[1:]
            else:
                animal = self.dog_queue[0]
                self.dog_queue = self.dog_queue[1:]
            return animal

    def dequeueDog(self):
        if len(self.dog_queue) < 1:
            return None

        animal = self.dog_queue[0]
        self.dog_queue = self.dog_queue[1:]

        return animal

    def dequeueCat(self):
        if len(self.cat_queue) < 1:
            return None

        animal = self.cat_queue[0]
        self.dog_queue = self.cat_queue[1:]

        return animal

    def enqueueAnimal(self, animal_name, animalType):
        if animalType == 'Dog':
            animal = Dog(animal_name, self.id)
            self.animal_queue.append(animal)
            self.id += 1
        else:
            animal = Cat(animal_name, self.id)
            self.cat_queue.append(animal_name)
            self.d += 1


class Animal():
    def __init__(self, name, animalID):
        print('Animal named ' + name + ' has just been received')
        self.name = name
        self.animalID = animalID

    def __str__(self):
        return self.name


class Dog(Animal):
    def __init(self, name, animalID):
        super.__init__(name, animalID)


class Cat(Animal):
    def __init(self, name, animalID):
        super.__init__(name, animalID)


def printQueueInfo(shelter):

    print('----------------------------------\n')

    print('Dog Queue:\n')
    for dog in shelter.dog_queue:
        print(str(dog))
        print('\n\n')

    print('Cat Queue:\n')
    for cat in shelter.cat_queue:
        print(str(cat))
        print('\n\n')

    print('----------------------------------\n')


class Test(unittest.TestCase):
    def test_animal_shelter(self):
        animal_list = ["Hanzack", "Pluto", "Garfield", "Tony"]
        animal_type = ['Cat', 'Dog', 'Cat', 'Dog']

        shelter = AnimalShelter(animal_list, animal_type)

        self.assertEqual(str(shelter.dequeueAnimal()), "Hanzack")
        self.assertEqual(str(shelter.dequeueAnimal()), "Pluto")
        self.assertEqual(str(shelter.dequeueDog()), "Tony")
        self.assertEqual(str(shelter.dequeueCat()), "Garfield")


if __name__ == '__main__':
    unittest.main()