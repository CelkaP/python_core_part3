from cat import Cat
from sofa_is_damaged_exception import SofaIsDamagedException
from cat_is_hungry_exception import CatIsHungryException
from fish_is_under_attack_exception import FishIsUnderAttackException


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
