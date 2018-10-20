class Calculator:
    name='good calculator'
    price=18
    def __init__(self,name,price,height,width,weight):   # 注意，这里的下划线是双下划线
        self.name=name
        self.price=price
        self.h=height
        self.wi=width
        self.we=weight


# """"
# >>> cal=Calculator()  #注意这里运行class的时候要加"()",否则调用下面函数的时候会出现错误,导致无法调用.
# >>> cal.name
# 'Good Calculator'
# >>> cal.price
# 18
# >>> cal.add(10,20)
# Good Calculator
# 30
# >>> cal.minus(10,20)
# -10
# >>> cal.times(10,20)
# 200
# >>> cal.divide(10,20)
# 0.5
# >>>