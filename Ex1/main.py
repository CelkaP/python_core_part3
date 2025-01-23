from person import Person
from employee import Employee
from student import Student
from workingStudent import WorkingStudent

def main():
    person:Person = Person("Bob", 23)
    employee:Employee = Employee("John", 28, "Software Engineer")
    student:Student = Student("Anna", 19)
    working_student:WorkingStudent = WorkingStudent(name="Adam", age=20, work_position="Sales Trainer")
    
    person.say_hello()
    
    employee.say_hello()
    employee.introduce()
    
    student.say_hello()
    student.introduce()
    
    working_student()
    
if __name__ == '__main__':
    main()