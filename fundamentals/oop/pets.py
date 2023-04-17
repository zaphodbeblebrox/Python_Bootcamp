class Pet:
    def __init__(self, name, type, tricks, health = 100, energy = 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
    
    def eat(self):
        self.energy += 5
        self.health += 10
    
    def play(self):
        self.health += 5
    
    def noise(self):
        print("Unknown...")

class Dog(Pet):
    def __init__(self, name, tricks, health = 100, energy = 100):
        super().__init__(name, "dog", tricks, health = 100, energy = 100)
    
    def noise(self):
        print("bark")

class Cat(Pet):
    def __init__(self, name, tricks, health = 100, energy = 100):
        super().__init__(name, "cat", tricks, health = 100, energy = 100)
    
    def noise(self):
        print("meow")

class Bird(Pet):
    def __init__(self, name, tricks, health = 100, energy = 100):
        super().__init__(name, "bird", tricks, health = 100, energy = 100)
    
    def noise(self):
        print("chirp")