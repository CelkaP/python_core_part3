from student import Student
from employee import Employee


class WorkingStudent(Employee, Student):

    def __init__(self, name, age, work_position="Student"):
        super().__init__(name, age, work_position)
        self._position = (
            f"Student + {work_position}" if work_position != "Student" else "Student"
        )

    def __call__(self):
        self.say_hello()
        self.introduce()
