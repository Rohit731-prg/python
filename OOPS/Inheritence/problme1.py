class Person:
    def __init__(self):
        self.name = "Rohit Singha"
        self.age = 22

    def displayPersonInfo(self):
        print("Person Name: ", self.name);
        print("Person Age: ", self.age);

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.employeeID = 101

    def displayEmployeeInfo(self):
        print("Employe ID: ", self.employeeID);

class Professor(Employee):
    def __init__(self):
        super().__init__()
        self.subject = "English"

    def displayProfessorInfo(self):
        print("Professor Subject", self.subject);

class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollNumber = 12

    def displayStudentInfo(self):
        print("Student roll number: ", self.rollNumber);


professor = Professor()
professor.displayPersonInfo()
professor.displayEmployeeInfo()
professor.displayProfessorInfo()
print("\n\n")
student = Student()
student.displayPersonInfo()
student.displayStudentInfo();