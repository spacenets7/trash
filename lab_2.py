def display():
    pass
print(display)
print(display())

def display1():
    print("Hello this is a function")

display1()

def hello_func():
    return 'Hello Function'

print(hello_func().upper)

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('Math','Art','Chem',name='Jhon',age=22, id=132)

courses = ['Math','Art','Chem'] #this is a list
info = {'name':'Jhon','age':22, 'id':132} # this is a dictionary

#  student_info(courses,info) they are not unpacked
#unpack them
student_info(*courses,**info)

