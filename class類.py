class Calculator:       #首字母要大写，冒号不能缺
    name='Good Calculator'  #该行为class的属性
    price=18
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
        
# """"
# >>> c=Calculator('bad calculator',18,17,16,15)
# >>> c.name
# 'bad calculator'
# >>> c.price
# 18
# >>> c.h
# 17
# >>> c.wi
# 16
# >>> c.we
# 15
# >>>
# """"