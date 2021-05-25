# String Formatting

'''
The format syntax:→
"name:{};age:{}".format("John", 42)
"name: {name}; age: {age}".format(age=42, name="John")
'''
t = "name:{};age:{}".format("John",42)
n = "name: {name}; age: {age}".format(age=42, name="John")
print(t,"\n",n)

data = {"name":"John","age":42}
print(f"name:{data['name']};age:{data['age']}")
x = 3.14159265
print(f"pi = {x: 3.4}")
