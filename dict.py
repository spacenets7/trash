dict = {
    "siddu":"student",
    "age": 19
}

print(dict)
print(dict["age"])
print(dict.get('names'))  # does not throw any error
print(dict.keys())  # prints all the keys

for key in dict.keys():   # iterate through the keys
    if("age"==key):
        print(f"The value corresponding to {key} is {dict[key]}")
    else:
         print(f"The value corresponding to {key} is {dict[key]}")

print(dict.items())