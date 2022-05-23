#import something to use later
from Robot import Robot
from Dinosaur import Dinosaur
from Weapon import Weapon

#declare battlefield class

robot_one = Robot ("T-1000")
dino_one = Dinosaur ("T-Rex")
weapon_one = Weapon ("Battle Axe")

class Battlefield:

    def __init__(self):
        self.Robot = robot_one
        self.Dinosaur = dino_one

        pass

    def game_intro_scene  (self):

   
        print ("The game is almost under way!")
        print (f"The {self.Dinosaur.name} has entered the ring, with {self.Dinosaur.health} HP and an attack that does {self.Dinosaur.attack_power} damage!")
        print ("***All the dinos ROAR!***")
        print (f"The {self.Robot.name} has entered the ring, with {self.Robot.health} HP and appears to be carrying a {self.Robot.weapon.name} that also does {self.Robot.weapon.attack_power} damage!")
        print ("***Every robot goes beserk!!***")
  
        
        pass

    def run_game (self):
        print ("The game has begun!")
        print (f"The {robot_one.name} takes a swing at the {dino_one.name} and takes a big chunk out!")
        weapon_one.swing(dino_one)
        print (f"The {dino_one.name} is now at {dino_one.health} HP!")
        dino_one.bite(robot_one)
        print (f"And the {dino_one.name} bites back! The {robot_one.name} is down to {robot_one.health}")
        print (f"The {robot_one.name} is now at {robot_one.health} HP!")
        
       

    
            
        
    

            #robo and dino need to fight here

            #while dino.hp and robo.hp is greater than 0
                #robo attack_dino
                #subtract health on attack
             #dino attack_robo
                 #subtract health on attack
        pass
