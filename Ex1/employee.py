from person import Person

class Employee(Person):
    
    def __init__(self, name:str, age:int, position:str):
        super().__init__(name, age)
        self._position = position
        
        
    def introduce(self) -> None:
        self.say_hello()
        print(f"Introduce() -> Position: {self._position}")
        
        