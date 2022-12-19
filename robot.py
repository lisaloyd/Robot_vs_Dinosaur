from weapon import Weapon

class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = ""
        self.health = int
        self.active_weapon = Weapon("sword", 30)

    def set_name(self, name):
        self.name = name
        
    def attack(self, dinosaur): 
        pass
