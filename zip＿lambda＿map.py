a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))  #需要加list来可视化这个功能
"""
[(1, 4), (2, 5), (3, 6)]
"""
for i,j in zip(a,b):
     print(i/2,j*2)
"""
0.5 8
1.0 10
1.5 12
"""
fun=lambda x,y:x+y
x=int(3)    #这里要定义int整数，否则会默认为字符串
y=int(4)
print(fun(x,y))
"""
x=6
y=6
12
"""

def fun1(x,y):
    return (x+y)
list(map(fun1,[1],[2]))
"""
[3]
"""
list(map(fun1,[1,2],[3,4]))
"""
[4,6]
"""



