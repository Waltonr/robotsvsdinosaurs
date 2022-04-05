from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('Optimus')
        self.dinosaur = Dinosaur('Reptor', 20)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the game of: Robots vs Dinosaurs!')

    def battle_phase(self):
        robot = self.robot
        dinosaur = self.dinosaur
        while robot.health > 0 and dinosaur.health > 0:
            robot.attack(dinosaur)
            if dinosaur.health <= 0:
                print(f'{dinosaur.name} has been knocked out.')
                break   
            elif dinosaur.attack(robot):
                if robot.health <= 0:
                    print(f'{robot.name} has been knocked out!')
                    break
            
    
    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} won!')
        else:
            self.dinosaur.health <= 0
            print(f'{self.robot.name} won!')

        
