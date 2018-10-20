a_list = [12, 3, 67, 7 , 82]
a_tuple = (12, 3, 5, 15 , 6)




for index in range(len(a_list)):
    print("index = ", index, ", number in list = ", a_list[index])
"""
index =  0 , number in list =  12
index =  1 , number in list =  3
index =  2 , number in list =  67
index =  3 , number in list =  7
index =  4 , number in list =  82
"""

for index in range(len(a_tuple)):
    print("index = ", index, ", number in tuple = ", a_tuple[index])
"""
tuple不可以修改
index =  0 , number in tuple =  12
index =  1 , number in tuple =  3
index =  2 , number in tuple =  5
index =  3 , number in tuple =  15
index =  4 , number in tuple =  6
"""
