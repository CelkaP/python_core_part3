class Person:
    
    def __new__(cls, *args, **kwargs):
        print("New person has been born.")
        return super().__new__(cls)
        
    
    def __init__(self, name:str, age:int):
        self.__name = name
        self.__age = age
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name:str) -> None:
        self.__name = name

    def get_age(self) -> int:
        return self.__age
    
    def set_age(self, age:int) -> None:
        self.__age = age
        
    def say_hello(self) -> str:
        print(f"Say Hello() -> Hello {self.__name}")
        
