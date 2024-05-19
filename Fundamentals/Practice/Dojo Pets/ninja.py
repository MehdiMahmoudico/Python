import pet

class Ninja :
    def __init__(self ,first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet_food.eat()
        return self
    def bathe(self):
        self.treats.noise()
        return self

    
ninja = Ninja("Mehdi","mm",pet.Pet("beki","kitty","jump","meow"),pet.Pet("beki","kitty","jump","meow"),pet.Pet("beki","kitty","jump","meow"))

ninja.feed().walk().bathe()