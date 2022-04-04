from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('Optimus Prime')
        self.dinosaur = Dinosaur('Godzilla', 25)
    
    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

    def battle_phase(self):
        robot = self.robot 
        dinosaur = self.dinosaur
        while robot.health != 0 or dinosaur.health != 0:
            robot.attack()
            dinosaur.attack
            if robot.health == 0:
                print(f'{robot.name} has been knocked out.')
                break
            else:
                dinosaur.health == 0
                print(f'{dinosaur.name} has been knocked out!')
                break
            
    
    def display_winner(self):
        robot = self.robot
        dinosaur = self.dinosaur
        if robot.health == 0:
            print(f'{dinosaur.name} won!')
