
import random

class Character :
    def __init__(self,name,strenght,speed,health) :
        self.name = name
        self.strength = strenght
        self.speed = speed
        self.health = health
        self.inventory = []
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    def attack ( self , obj ):
        obj.health -= self.strength
        self.drop_item(obj)
        return self
    def is_alive(self):
        return self.health>0


    def drop_item(self, obj):
            # 20% chance to drop an item
            if random.random() < 0.2:
                potion = Potion("Health Potion", 20)
                obj.pick_up_item(potion)
                print(f"{self.name} dropped a {potion.name}!")

    def pick_up_item(self, item):
                self.inventory.append(item)

    def use_item(self):
        if self.inventory:
            item = self.inventory.pop(0)
            item.apply(self)
            print(f"{self.name} used a {item.name}!")
        else:
            print(f"{self.name} has no items to use.")



class Item:
    def __init__(self, name):
        self.name = name

    def apply(self, character):
        pass

class Potion(Item):
    def __init__(self, name, health_restore):
        super().__init__(name)
        self.health_restore = health_restore

    def apply(self, character):
        character.health += self.health_restore
        print(f"{character.name}'s health restored by {self.health_restore}!")





class Ninja (Character):

    def __init__(self, name, strenght=10, speed=5, health=100):
        super().__init__(name, strenght, speed, health)




class Pirate (Character):

    def __init__(self, name, strenght=15, speed=3, health=100):
        super().__init__(name, strenght, speed, health)





class Battle :
    @staticmethod
    def start_battle (ninja,pirate):
        round =1
        while ninja.is_alive() and pirate.is_alive():
            print(f"Round:{round}")
            for i in range(0,random.randint(0,ninja.speed)):
                ninja.attack(pirate)
            if pirate.is_alive():
                for i in range(0,random.randint(0,ninja.speed)):
                    pirate.attack(ninja)

            if random.random() < 0.5:
                ninja.use_item()
            if random.random() < 0.5:
                pirate.use_item()

            
            ninja.show_stats()
            pirate.show_stats()
            round+=1
        Battle.declare_winner(ninja,pirate)

    @staticmethod
    def declare_winner(ninja,pirate):
        if (ninja.is_alive()):
            print(f"{ninja.name} is the winner")
        elif (pirate.is_alive()):
            print(f"{pirate.name} is the winner")
        else : print(f"Draw")




michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

Battle.start_battle(michelangelo,jack_sparrow)