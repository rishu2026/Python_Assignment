class Ten():
    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone

    def display(self):
        print("Student details:" ,self.name,self.address,self.phone)

class Tweleve(Ten):
    def __init__(self,name,address,phone,stream,section):
        super().__init__(name,address,phone)
        self.stream=stream
        self.section=section

    def details(self):
        super().display()
        print(self.stream,self.section)

class bachelors(Tweleve):
    def __init__(self,name,address,phone,stream,section,dept,passyr):
        super().__init__(name,address,phone,stream,section)
        self.dept=dept
        self.passyr=passyr

    def academicdetails(self):
        super().details()
        print(self.dept,self.passyr)

o2=bachelors("Rishu","Bhagalpur",7361914042,"PCM","A","CSEDS",2026)
o2.academicdetails()
