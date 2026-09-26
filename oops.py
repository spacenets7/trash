class Employee:

    nums_of_emp =0  # class variable
    raise_amount = 1.5

    def __init__(self, first, last, pay, email):
        self.first = first
        self.last = last     # instance variable 
        self.pay = pay     
        self.email = email
        Employee.nums_of_emp+=1 #init runs every time a employee is created hence this will aslo increase

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay*Employee.raise_amount)  # the raise amount should be called through employee

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay,email = emp_str.split('-')
        return cls(first,last,pay,email)

emp_1 = Employee('Siddu', 'U S',5000,'smtg@email.com')
emp_2 = Employee('test','user',6000,'test@email.com')

Employee.set_raise_amt(2)

print(emp_1.first)
print(emp_2.email)
print('{} {}'.format(emp_1.first,emp_1.last))
print(emp_2.fullname())
print(Employee.fullname(emp_1))

emp_1.applyRaise()
print(emp_1.pay)

# emp_1.first = 'John'
# emp_1.last = 'Doe'
# emp_1.email = 'smthg@gmail.com'
# emp_1.pay = 50000

# emp_2.first = 'test'
# emp_2.last = 'test '
# emp_2.email = 'test@gmail.com'
# emp_2.pay = 60000

print(emp_1.__dict__)
#print(Employee.__dict__)

print(Employee.nums_of_emp)

emp_str_1 = 'Siddddu-US-80000-ussi@email.com'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.pay)
print(new_emp_1.first)