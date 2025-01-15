## 1. Implement classes one by one:
A class Person with private name and age fields. Implement __new__() method where there is a print statement with the phrase “New person has been born”. Implement getter and setter methods for name and age. Implement the method say_hello() with a print statement of the name of the Person.
A class  Employee inherited from Person. Add protected field position. In __init__ pass the value of position of Employer and save into the instance field. Implement method introduce() that uses say_hello() and prints the position after it.
A class Student  inherited from Person. Add protected field position. In __init__ set position = “Student”. Implement method introduce() that uses say_hello() method and prints the position after it.
A class WorkingStudent that is inherited from both  Employee and Student. Implement __call__() method for the WorkingStudent class which calls say_hello() and introduce() methods inside.
Create instances of each class and call say_hello() and introduce() methods. Try to call and instance of a WorkingStudent class.

## 2. Implement one by one:
Three Exceptions: SofaIsDamaged, FishIsUnderAttack and CatIsHungry. All inherited from Exception.
A class Cat with following methods: sharpen_claws() that raises SofaIsDamaged, drink_wate_from_aquarium() that raises FishIsUnderAttack and say_meow() that raises CatIsHungry.
A method sleep() that prints “zZz”.
A main function where you create an instance of a Cat and catch all possible exceptions.
In the finally block call sleep() method.

## 3. Rewrite to lambda syntax:
def multiply (x):
    return x + x

def double(x):
    return x*2
