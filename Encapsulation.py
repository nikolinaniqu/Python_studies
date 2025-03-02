class Person:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print("Person: ",self.firstname, self.lastname)

class Student(Person):
    def __init__(self, firstname,lastname,indexnumber):
        self.indexnumber = indexnumber

        super().__init__(firstname,lastname)
        
    def show(self):
        print("Student: ",self.firstname, self.lastname,self.indexnumber)

class Professor(Person):
    def __init__(self, firstname,lastname,subject):
        self.subject = subject

        super().__init__(firstname,lastname)
        
    def show(self):
        print("Professor: ",self.firstname, self.lastname,self.subject)

person = Person("John","Davidson")
student = Student("Will", "Smith", "10/02/009")
professor = Professor("Edward", "Owen", "Pyton programming")

person.show()
student.show()
professor.show()
