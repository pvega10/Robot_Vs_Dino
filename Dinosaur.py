class Dinosaur:

    def __init__(self, name):
        self.name = name
        self.attack_power = 10
        self.health = 100

        pass

    def bite (self, robot):
        robot.health -= self.attack_power