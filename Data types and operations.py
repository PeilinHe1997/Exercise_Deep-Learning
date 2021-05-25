#Data type

print("type(4//2) is ",type(4//2))#整除，3/2等于1

print("type(4/2) is ",type(4/2))#除法，结果为浮点型float

k = 5
k **= 2
print(k)

s1 = """Multiline
string with
exact interpretation"""
print(s1)

x = [3]
y = [21,3,4,5,2,34,5]
print(x+y)

d = {"a":12,"b":13,"c":560}
print(d["a"])

# List Manipulation

data = [0,"onw",2.,'three',[4]]
data.append("5")
data.extend([6,7.])
print(data)

data.insert(0,-1)
print(data)
data[0:0] = ["-3",-2.]
print(data)


data.remove("three")
data.pop(1)
print(data)

data.pop(-2)
print(data)

del data[3]
print(data)





