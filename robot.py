from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Gun', 30)
    
    def attack(self, dinosaur):
        weapon = self.active_weapon
        print(f'{self.name} attacks {dinosaur.name} with {weapon.name}')
        dinosaur.health -= weapon.attack_power
        print(dinosaur.health)
 