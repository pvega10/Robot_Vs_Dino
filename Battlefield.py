#import something to use later
from Robot import Robot
from Dinosaur import Dinosaur


#declare battlefield class


class Battlefield:

    def __init__(self):
        self.robot = Robot("T-1000")
        self.dinosaur = Dinosaur("T-Rex")

        pass

    def game_intro_scene  (self):

   
        print ("The game is almost under way!")
        print (f"The {self.dinosaur.name} has entered the ring, with {self.dinosaur.health} HP and an attack that does {self.dinosaur.attack_power} damage!")
        print ("***All the dinos ROAR!***")
        print (f"The {self.robot.name} has entered the ring, with {self.robot.health} HP and appears to be carrying a {self.robot.weapon.name} that also does {self.robot.weapon.attack_power} damage!")
        print ("***Every robot goes beserk!!***")
  
        
        pass

    def run_game (self):
        print ("The game has begun!")
        while self.robot.health > 0 and self.dinosaur.health >0:
            print (f"The {self.robot.name} takes a swing at the {self.dinosaur.name} and lands a blow with the {self.robot.weapon.name}!")
            self.robot.weapon.attack(self.dinosaur)
            print (f"The {self.dinosaur.name} is now at {self.dinosaur.health} HP!")
            # use an if to see if both are still alive to see if 2nd attack should happen, check to see if dino still alive
            if self.dinosaur.health > 0: 
                print (f"And the {self.dinosaur.name} bites back!")
                self.dinosaur.attack(self.robot)
                print (f"The {self.robot.name} is now at {self.robot.health} HP!")
            elif self.dinosaur.health < 0:
                pass
            # elif the dino is dead pass


    def end_game (self):

        print ("It doesnt...it doesnt look like theyre gonna get up...")

        if self.robot.health > 0:
            print (f"{self.robot.name} wins!")
        elif self.dinosaur.health > 0:
            print (f"{self.dinosaur.name} wins!")

        pass
        
        
    
       
