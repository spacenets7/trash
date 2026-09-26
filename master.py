class person:
    uni = "MIT Manipal"
    count=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        person.count+=1

    def display(self):
        print(f"My name is {self.name} and my age is {self.age}")



class student(person):
    def __init__(self,name,age,cgpa):
        super().__init__(name,age)
        self.__cgpa=cgpa

    def get_cgpa(self):
        return self.__cgpa

    def set_cgpa(self,cgpa):
        if 0<=cgpa<=10:
            self.__cgpa=cgpa

    def display(self):
        print(f"My name is {self.name} and my age is {self.age} my cgpa is {self.get_cgpa()}")

    def avg_marks(self,*args):
        print(f"the average marks of the student is {sum(args)/len(args)}")

    def add_details(self,**kwargs):
        print(f"more about students is {kwargs}")

    def role(self):
        return "Student"


class researcher:
    def role(self):
        return "Researcher"

class researchStudent(student, researcher):
    def __init__(self,name,age,cgpa,r_area):
        super().__init__(name,age,cgpa)
        self.r_area=r_area

    def display(self):
        print(f"My name is {self.name} and my age is {self.age} my cgpa is {self.get_cgpa()} my research area is {self.r_area}")

    

p1 = person("Siddu",19)
p1.display()

s1 = student("sam",19,9)
s1.display()
s1.avg_marks(12,13,14,15)
s1.add_details(city="bang",hostel="b10")
students = [s1]
sorted(students,key=lambda x : x.get_cgpa())

r1 = researchStudent("mat",19,8.5,"ml")
r1.display()

people = [p1,s1,r1]
for x in people:
    x.display()

print(person.count)

print(r1.role())