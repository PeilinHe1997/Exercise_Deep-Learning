'''In Python, almost everything is an object'''

#Class and objects
class AddN(object):
    def __init__(self,n = 1):
        super(AddN, self).__init__()
        self.n = n

    def __call__(self,x):
        return x + self.n

    def squared(self,x):
        return x ** 2 + self.n

    def sequence(self,x):
        for n in range(self.n):
            yield x + n


add1 = AddN(n=1)
print(add1.squared(5))
print(add1(5))

add1.n = 4
add1.unused = None
print(add1.squared(5))
#immutable Objects
def modify(x):
    x += 1
y = 10
modify(y)
print(y)

#mutable objects
def append1(x):
    x.append(1)

y = [10]
append1(y)
print(y)
# Function objects
def sqr(x):
    return x ** 2
def apply(f,data):
    return f(data)

print(apply(sqr,5))#25
print(apply(add1,5))#29  计算5+4(add1.n)















