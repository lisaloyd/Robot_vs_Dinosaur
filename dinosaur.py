class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power


    def attack(self, robot): 
        if self.is_alive():
            robot.health = self.attack_power
            


    def is_alive(self):
        return self.health > 0

   
#    def attack(self, dinosaur): 
#         if self.is_alive():
#             dinosaur.health = self.active_weapon.attack_power