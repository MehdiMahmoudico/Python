class Pet :
    def __init__(self ,name , type , tricks, noises):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.noises = noises
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print("beki full")
        return self
    def play(self):
        self.health += 5
        print("beki happy")
        return self
    def noise(self):
        print(f"{self.noises}")
        return self

