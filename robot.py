from weapon import Weapon

class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("sword", 30)

        
    def attack(self, dinosaur): 
        pass
