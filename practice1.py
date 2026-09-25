def details():
    name = input("Name: ")
    roll = input("Roll: ")
    m1 = int(input("M1: "))
    m2 = int(input("M2: "))
    m3 = int(input("M3: "))

    avg = (m1+m2+m3)/3

    with open('students.txt','a') as f:
        f.write(f"{name},{roll},{m1},{m2},{m3},{avg}\n")

def search():
    s = input("Enter the roll number you wanna search: ")
    with open('students.txt','r') as f:
        for line in f:
            data = line.strip().split(",")
            if data[1]==s:
                print("record found")
                print(line.strip())
                return

    print("record not found")

details()
search()



