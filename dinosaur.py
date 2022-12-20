class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = 30


    def set_attack(self, robot): 
        if self.is_alive():
            return self.attack_power


    def is_alive(self):
        return self.health