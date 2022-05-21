#import something to use later
from Robot import Robot
from Dinosaur import Dinosaur
from Weapon import Weapon

#declare battlefield class

robot_one = Robot ("T-1000")
dino_one = Dinosaur ("T-Rex", 100)

class Battlefield:

    def __init__(self):
        self.Robot = robot_one
        self.Dinosaur = dino_one



        pass

    def run_game (self):

        #while dino.hp and robo.hp is greater than 0
            #robo attack_dino
                #subtract health on attack
        #dino attack_robo
            #subtract health on attack
   
        print ("The game has begun!")
        print (self.Dinosaur.attack_power)
        print (self.Robot.name)
        print (self.Robot.active_weapon.name)
        
        pass
