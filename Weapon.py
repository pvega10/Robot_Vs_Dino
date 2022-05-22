class Weapon:

    def __init__(self, name):
        self.name = name
        self.attack_power = 10

        pass

    def swing (self, dinosaur):
        dinosaur.health = self.attack_power