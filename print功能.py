print('hello world')
'''
hello world
'''
print("hello world 2")
'''
hello world 2
'''

print('Hello world'+' Hello Hong Kong')
"""
Hello world Hello Hong Kong
"""
print(1+1)
"""
2
"""
print(3-1)
"""
2
"""
print(3*4)
"""
12
"""
print(12/4)
"""
3.0
"""
print('iphone'+4) #字符串不可以直接和数字相加
"""
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print('iphone'+4)
TypeError: Can't convert 'int' object to str implicitly
"""
print(int('2')+3) #int为定义整数型
"""
5
"""
print(int(1.9))  #当int一个浮点型数时，int会保留整数部分
"""
1
"""
print(float('1.2')+3) #float()是浮点型，可以把字符串转换成小数
""""
4.2
"""