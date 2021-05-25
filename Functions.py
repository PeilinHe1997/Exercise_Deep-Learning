#Functions

def func1(data, opt = None):
    if opt is None:
        print("data is",data)
    else:
        return data
    
func1(27,True)
func1(opt = False,data = 27)
 # Generator Example
def sup(it1,it2):
    for v1 in it1:
        for v2 in it2:
            yield v1,v2
for t in sup("ab",range(2)):
    print(type(t),t)
