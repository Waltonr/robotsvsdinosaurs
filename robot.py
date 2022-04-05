from weapon import Weapon
import random 

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon(0)
    
    def attack(self, dinosaur):
        weapon = self.active_weapon
        random_weapon = random.choice(weapon.name)
        if random_weapon == 'Gun':
            weapon.attack_power = 20
            dinosaur.health -= weapon.attack_power
            print(f'{self.name} attacks {dinosaur.name} with {random_weapon} for {weapon.attack_power} damage! {dinosaur.name} health is {dinosaur.health}%')
        elif random_weapon == 'Grenade':
            weapon.attack_power = 25
            dinosaur.health -= weapon.attack_power
            print(f'{self.name} attacks {dinosaur.name} with {random_weapon} for {weapon.attack_power} damage! {dinosaur.name} health is {dinosaur.health}%')
        elif random_weapon == 'Knife':
            weapon.attack_power = 10
            dinosaur.health -= weapon.attack_power
            print(f'{self.name} attacks {dinosaur.name} with {random_weapon} for {weapon.attack_power} damage! {dinosaur.name} health is {dinosaur.health}%')
        
        
        
 