
APPLE = 100 # 全局变量
a = None
def fun():
    global a    # 使用之前在全局里定义的 a
    a = 20      # 现在的 a 是全局变量了
    return a+100

print(APPLE)    # 100
print('a past:', a)  # None
print(fun())
print('a now:', a)   # 20