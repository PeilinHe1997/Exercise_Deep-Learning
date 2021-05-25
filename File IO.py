#1. the open function
'''
signature:open(name,mode,..)
filenames:"C:/path/to/file.txt"
opening modes:
'r'ead
'w'rite
'a'ppend
't'ext
str
'b'inary:bytes
'''
#2. the with statement
'''
with open(...) as file:
'''

#write file
with open("test.txt","wt") as file:
    for x in range(1,11):
        file.write(f"{x},{x**2}\n")
#read file
with open("test.txt","rt") as file:
    for line in file:
        x,y = line.rstrip().split(",")
        print(x,y)
