from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Gun', 25)
    
    def attack(self, dinosaur):
        weapon = self.active_weapon
        dinosaur.health -= weapon.attack_power
        print(f'{self.name} attacks {dinosaur.name} with {weapon.name} for {weapon.attack_power} damage! {dinosaur.name} health is {dinosaur.health}%')
        
 