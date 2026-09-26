tuple1 = (1,5,6,'siddu',True)  #tuples are immutable
tup = (1,2,4,5,6,7)
print(type(tup),tup)
print('the length of the tuple is ',len(tup))
print(tup[0])
print(tup[1])
print(tup[2])

if 'siddu' in tup:
    print('yes')
else:
    print('No')

tup2 = tup[1:5:2]
print(tup2)

# manipulation of tuple
countries = ("spain","italy","india","england","germany")
print(countries)
temp = list(countries)     # convert to list
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

res = countries.count("spain")
print("spain occurs times: ",res)
res1 = countries.index("spain",0,3)
print("index of spain is ",res1)