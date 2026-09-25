'''f = open('text.txt','r+') 
print(f.name)
print(f.mode)
f.close()'''

# with is best practice as it closes the file automatically
# this is called context manager

with open('text.txt','r+') as f:
    #f_contents = f.read()
    #f_lines = f.readlines()
    #print(f_lines)
    #print(f_contents,end=' ')

    #for line in f:
    #   print(line,end=' ')

    f_contents = f.read(100)
    print(f_contents)

with open('test.txt','w') as f:
    f.write('Test')


