l = [2,3,4,5,"siddu",True]
print(l)
print(type(l))
print(len(l))
print(l[-3]) # negative indexing 
print(l[len(l)-3])  #subtract from length of the list to get the positive index of the same

print(l[:])  # prints the full list

print(l[1:2])  # list slicing list[start:end]
print(l[1:4:2])  # list slicing with jumps list[start:end:jump]

lst = [i*i for i in range(4) ]
lst1 = [i*i for i in range(4) if i%2==0]
print(lst)
print(lst1)

l.append(33)
print(l)

l.insert(1,899)

list1 = [20,10,40,30,0]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
print(l.index(1))
print(l.count(1))

m = l.copy()
m[0]=0
print(m)

l.extend(m)
print(l)