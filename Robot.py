from Weapon import Weapon

weapon_one = Weapon ("Battle Axe", 25)

class Robot:


    def __init__(self, name):
        self.name = name
        self.active_weapon= weapon_one
        self.health = 100

        pass