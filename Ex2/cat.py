from cat_is_hungry_exception import CatIsHungryException
from fish_is_under_attack_exception import FishIsUnderAttackException
from sofa_is_damaged_exception import SofaIsDamagedException


class Cat:
    def __init__(self, name):
        self.name = name

    def sharpen_claws(self):
        raise SofaIsDamagedException

    def drink_water_from_aquarium(self):
        raise FishIsUnderAttackException

    def say_meow(self):
        raise CatIsHungryException

    def sleep(self) -> None:
        print("Zzzz")
