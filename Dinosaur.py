class Dinosaur:

    def __init__(self, name):
        self.name = name
        self.attack_power = 50
        self.health = 100

        pass

    def attack (self, robot):
        robot.health -= self.attack_power