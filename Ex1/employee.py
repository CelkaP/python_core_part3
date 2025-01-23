from person import Person


class Employee(Person):

    def __init__(self, name, age, position):
        super().__init__(name, age)
        self._position = position

    def introduce(self) -> None:
        self.say_hello()
        print(f"Introduce() -> Position: {self._position}")
