class employee:

    increment = 1.5
    def __init__(self,name,pay,email):
        self.name=name
        self.pay=pay
        self.email=email

    def intro(self):
        return 'Hello I am {} my salary is {} and my email is {}'.format(self.name,self.pay,self.email)

    def pay_raise(self):
        return self.pay*self.increment  # dont use Employee.increment as it wont be inherited to child classes

class dev(employee):
    increment =2
    def __init__(self,name,pay,email,language):
        super().__init__(name,pay,email)
       # employee.__init__(self,name,pay,email)  same as the above one
        self.language = language 

class manager(employee):
    def __init__(self,name,pay,email,employees=None):
        super().__init__(name,pay,email)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
            if emp not in self.employees:
                self.employees.remove(emp)

    def display(self):
        for emp in self.employees:
            print('-->',emp.name())

emp1 = employee('Siddu',100,'ussid@email.com')
print(emp1.intro())
print(emp1.pay_raise())

dev1 = dev('sam',200,'test@email.com','C')
print(dev1.intro())
print(dev1.pay_raise())


print(dev1.__dict__)
# print(help(dev))

mgr1 = manager('Sue',500,'sue@email.com',[dev1])
#mgr1.display()

print(isinstance(mgr1, employee))
print(isinstance(mgr1, dev))
print(issubclass(manager,employee))