from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase(self)
        self.display_winner()

    def display_welcome():
        print('Welcome to Robots vs Dinosaurs!')

    def battle_phase(self):
        dinosaur = self.dinosaur
        robot = self.robot
        while robot.health != 0 or dinosaur.health != 0:
            robot.attack(dinosaur)
            dinosaur.attack(robot)
            if robot.health == 0:
                print(f'{robot.name} has been knocked out.')
                break
            else:
                self.dinosaur.health == 0
                print(f'{self.dinosaur.name} has been knocked out!')
                break
            
    
    def display_winner(self):
        if self.robot.health == 0:
            print(f'{self.dinosaur.name} won!')
        else:
            self.dinosaur.health == 0
            print(f'{self.robot.name} won!')

        
