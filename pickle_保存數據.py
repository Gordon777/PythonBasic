import pickle

a_dict = {'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}

# pickle a variable to a file
file = open('pickle_example.pickle.txt', 'wb')
pickle.dump(a_dict, file)
file.close()

# reload a file to a variable
with open('pickle_example.pickle.txt', 'rb') as file:
    a_dict1 =pickle.load(file)
    file.close()
print(a_dict1)