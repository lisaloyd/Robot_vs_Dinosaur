from dinosaur import Dinosaur
from robot import Robot

class Battlefield:

    def __init__(self):
        self.dinosaur = Dinosaur('Dinosaur The Killer', 30)
        self.robot = Robot('Robot The Judge', 'sword')
        run_game = self.dinosaur.attack(self.robot) and self.robot.attack(self.dinosaur)


    def run_game(self):
        run_game = True
    

    def display_welcome(self):
        print('\nWelcome to Dinosaurs vs Robots!\nOnly one can win!')

    def battle_phase(self):
        while self.dinosaur.is_alive() and self.robot.is_alive():
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
            print(f'{Robot.name} attacked {Dinosaur.name} with a {Robot.active_weapon} for {Robot.attack_power} damage!')
            print(f'{Dinosaur.name} attacked {Robot.name} for {Dinosaur.attack_power} damage!')


    def display_winner(self):
        if self.dinosaur.is_alive():
            print(f'{Dinosaur} is the winner!')
        else: 
            self.robot.is_alive()
            print(f'{Robot} is the winner!')


 