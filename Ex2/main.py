from cat import Cat
from sofaIsDamagedException import SofaIsDamagedException
from catIsHungryException import CatIsHungryException
from fishIsUnderAttackException import FishIsUnderAttackException


def main():
    cat: Cat = Cat("Puszek")

    try:
        cat.sharpen_claws()
    except SofaIsDamagedException as error:
        print(error)
    finally:
        cat.sleep()

    try:
        cat.drink_water_from_aquarium()
    except FishIsUnderAttackException as error:
        print(error)
    finally:
        cat.sleep()

    try:
        cat.say_meow()
    except CatIsHungryException as error:
        print(error)
    finally:
        cat.sleep()


if __name__ == "__main__":
    main()
