def display(name,usn):
    print(f"Name:{name}")
    print(f"USN: {usn}")

def calculate(*marks):
    total = sum(marks)
    average = total/len(marks)
    highest = max(marks)
    lowest = min(marks)
    return total,average,highest,lowest

while True:
    print("1.Process student data")
    print("2. exit")
    choice = input("Selct an option: ")

    if choice =='2':
        break
    elif choice =='1':


        name = input("Enter the name: ")
        usn = input("Enter usn id: ")

        n = int(input("Enter the number of subjects:"))
        marks_list =[]

        for i in range(n):
             mark = float(input(f"Enter marks of subject{i+1}: "))
             marks_list.append(mark)

        display(name,usn)
        print(calculate(*marks_list))
