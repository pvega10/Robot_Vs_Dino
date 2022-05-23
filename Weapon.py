class Weapon:

    def __init__(self, name):
        self.name = name
        self.attack_power = 30

        pass

    def attack (self, dinosaur):
        dinosaur.health -= self.attack_power