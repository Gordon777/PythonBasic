a_input=input('please input a number:')
print('this number is:',a_input)

''''
please input a number:12 #12 是我在硬盘中输入的数字
this number is: 12
'''




a_input=int(input('please input a number:'))#注意这里要定义一个整数型
if a_input==1:
    print('This is a good one')
elif a_input==2:
    print('See you next time')
else:
    print('Good luck')

""""
please input a number:1   #input 1
This is a good one

please input a number:2   #input 2
See you next time

please input a number:3   #input 3 or other number
Good luck
"""