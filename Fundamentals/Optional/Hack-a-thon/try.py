import random

class Character:
    def __init__(self, name, strength, speed, health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
        self.inventory = []

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nInventory: {[item.name for item in self.inventory]}\n")

    def attack(self, obj, battlefield):
        obj.health -= self.strength
        battlefield.drop_item()
        return self

    def is_alive(self):
        return self.health > 0

    def pick_up_item(self, item):
        self.inventory.append(item)

    def use_item(self):
        if self.inventory:
            item = self.inventory.pop(0)
            item.apply(self)
            print(f"{self.name} used a {item.name}!")
        else:
            print(f"{self.name} has no items to use.")

class Ninja(Character):
    def __init__(self, name, strength=10, speed=5, health=100):
        super().__init__(name, strength, speed, health)

class Pirate(Character):
    def __init__(self, name, strength=15, speed=3, health=100):
        super().__init__(name, strength, speed, health)



class Item:
    def __init__(self, name):
        self.name = name



class Potion(Item):
    def __init__(self, name, health_restore):
        super().__init__(name)
        self.health_restore = health_restore

    def apply(self, character):
        character.health += self.health_restore
        print(f"{character.name}'s health restored by {self.health_restore}!")

class Battlefield:
    def __init__(self):
        self.items_on_ground = []

    def drop_item(self):
        if random.random() < 0.2:
            potion = Potion("Health Potion", 20)
            self.items_on_ground.append(potion)
            print(f"A {potion.name} dropped on the battlefield!")

    def pick_up_items(self, character):
        if self.items_on_ground:
            item = self.items_on_ground.pop(0)
            character.pick_up_item(item)
            print(f"{character.name} picked up a {item.name}!")

class Battle:
    @staticmethod
    def start_battle(ninja, pirate):
        battlefield = Battlefield()
        round = 1
        while ninja.is_alive() and pirate.is_alive():
            print(f"Round: {round}")
            for _ in range(0, random.randint(0, ninja.speed)):
                ninja.attack(pirate, battlefield)
            if pirate.is_alive():
                for _ in range(0, random.randint(0, pirate.speed)):
                    pirate.attack(ninja, battlefield)

            
            battlefield.pick_up_items(ninja)
            battlefield.pick_up_items(pirate)

            
            if random.random() < 0.5:
                ninja.use_item()
            if random.random() < 0.5:
                pirate.use_item()

            ninja.show_stats()
            pirate.show_stats()
            round += 1
        Battle.declare_winner(ninja, pirate)

    @staticmethod
    def declare_winner(ninja, pirate):
        if ninja.is_alive():
            print(f"{ninja.name} is the winner")
        elif pirate.is_alive():
            print(f"{pirate.name} is the winner")
        else:
            print("Draw")

ninja = Ninja("Shadow")
pirate = Pirate("Blackbeard")
Battle.start_battle(ninja, pirate)
