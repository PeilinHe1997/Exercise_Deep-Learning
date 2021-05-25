
#Control Flow
'''
data = [0, [1], "two", 3., '4', -5]
index =0

#计算并输出每一个元素乘以2的结果
while index < len(data):#len(data)=6
    if isinstance(data[index],(int,float,list)):#[1]
        continue#continue返回while语句

    number = float(data[index])
    print(number * 2)
    index += 1

    if data[index] < 0: #data[index] == -5
        break
else:
    print("Success!")
'''
#给出序号

for i, e in enumerate([22,4,7,10]):
    print(i,e)

#三角递减

triang = [[x for x in range(10) if x > y] for y in range(10)]
for i in triang:
    print(i,sep = "\n")

#返回x/2如果x为奇数，键为x,值为x/2（整除）

half = {x:x//2 for x in range(10) if x % 2}
print(half)




















