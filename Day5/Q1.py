class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

# Hierarchichal Inheritance
class Student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno

#Multiple Inheritance
class Academic:
    def __init__(self,course,cgpa):
        self.course=course
        self.cgpa=cgpa

class Sports:
    def __init__(self,sports_name,level):
        self.sports_name=sports_name
        self.level=level


#Hybrid Inheritance

class Allrounderstudent(Student,Academic,Sports):
    def __init__(self,name,age,rollno,is_academic=False,is_sports=False,course=None,cgpa=None,sports_name=None,level=None):
        super().__init__(name,age,rollno)
        self.is_academic=is_academic
        self.is_sports=is_sports


        if self.is_academic:
            Academic.__init__(self,course,cgpa)

        if self.is_sports:
            Sports.__init__(self,sports_name,level)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Rollno: {self.rollno}")

        if self.is_academic:
            print(f"Course: {self.course}")
            print(f"CGPA: {self.cgpa}")
        
        if self.is_sports:
            print(f"Sports Name: {self.sports_name}")
            print(f"Sports Level: {self.level}")


s1=Allrounderstudent("Sunny",22,101,is_academic=True,is_sports=True,course="CSE-CS",sports_name="kho kho",level="National",cgpa=8.29)

s1.display()

