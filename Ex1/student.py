from person import Person


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._position = "Student"

    def introduce(self) -> None:
        self.say_hello()
        print(f"Introduce() -> Position: {self._position}")
