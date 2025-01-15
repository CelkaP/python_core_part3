from catIsHungryException import *
from fishIsUnderAttackException import *
from sofaIsDamagedException import *

class Cat:
    def __init__(self, name:str):
        self.name = name
    
    def sharpen_claws(self):
        raise SofaIsDamagedException
    
    def drink_water_from_aquarium(self):
        raise FishIsUnderAttackException

    def say_meow(self):
        raise CatIsHungryException
    
    def sleep(self) -> None:
        print("Zzzz")
        
        