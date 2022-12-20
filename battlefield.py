from dinosaur import Dinosaur
from robot import Robot

class Battlefield:

    def __init__(self):
        self.dinosaur = Dinosaur('Dinosaur The Killer', '30')
        self.robot = Robot('Robot The Judge', 'sword')
        


    def run_game(self):
        pass
    

    def display_welcome(self):
        print('\nWelcome to Dinosaurs vs Robots!\nOnly one can win!')

    def battle_phase(self):
        if self.dinosaur.is_alive and self.robot.is_alive():
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)


    def display_winner(self):
        if self.dinosaur.is_alive():
            print(f'{Dinosaur} is the winner!')
        else:
            print(f'{Robot} is the winner!')


# class Robot:
#     def __init__(self, name, health, active_weapon):
#         self.name = name
#         self.health = 100
#         self.active_weapon = Weapon("sword", 30)

        
#     def attack(self, dinosaur): 
#         pass

  # class Dinosaur:
    # def __init__(self, name, health, attack_power):
    #     self.name = name
    #     self.health = health
    #     self.attack_power = 30


    # def set_attack(self, robot): 
    #     pass


#     from alarm_clock import Alarm_Clock

# clock = Alarm_Clock('10:00', True, '4:00')


# clock.set_or_change_time('10:00')
# clock.set_alarm_time('4:00')
# clock.set_alarm_on_or_off()
