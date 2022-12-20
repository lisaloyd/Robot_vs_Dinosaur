from weapon import Weapon

class Robot:
    def __init__(self, name, active_weapon):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("sword", 20)

        
    def attack(self, dinosaur): 
        if self.is_alive():
            dinosaur.health -= self.active_weapon.attack_power
            

    def is_alive(self):
        return self.health > 0
