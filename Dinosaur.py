class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age
    def roar(self):
        print(f"{self.name} let out a powerful roar!")
    def eat(self):
        if self.diet == food:
            print(f"{self.name} eats the {food}.")
        else:
            print(f"{self.name} doesn't eat that.")
    def dino_info(self):
        print(f"Dinosaur name: {self.name}  Species: {self.species}  Diet: {self.diet}  Age: {self.age}")

food = ("Meat")
dinosaur1 = Dinosaur("Rex", "T-Rex", "Meat", 25)
dinosaur1.dino_info()
dinosaur1.roar()
print(f"There is some {food} on the ground.")
dinosaur1.eat()

food = ("Fruit")
dinosaur2 = Dinosaur("Sara", "Triceratops", "Grass", 20)
dinosaur2.dino_info()
dinosaur2.roar()
print(f"There is some {food} on the ground.")
dinosaur2.eat()

food = ("Leaves")
dinosaur3 = Dinosaur("Paul", "Brachiosaurus", "Leaves", 30)
dinosaur3.dino_info()
dinosaur3.roar()
print(f"There is some {food} in a tree.")
dinosaur3.eat()