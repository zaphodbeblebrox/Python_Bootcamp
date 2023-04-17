import pets as pets

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

bob = Ninja("bob", 
            "builder", 
            pets.Cat("Zip", "Purrcore"), 
            ["fish", "chicken"], 
            "dry food")

noelle = Ninja("noelle", 
            "cordis", 
            pets.Dog("Zip", "sit"), 
            ["pork"], 
            "wet food")

bob.feed()
bob.walk()
bob.bathe()

noelle.feed()
noelle.walk()
noelle.bathe()

print(bob.pet.__dict__)
print(noelle.pet.__dict__)