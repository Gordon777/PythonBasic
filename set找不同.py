char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']

sentence = 'Welcome Back to This Tutorial'

print(set(char_list))
# {'b', 'd', 'a', 'c'}

print(set(sentence))
# {'l', 'm', 'a', 'c', 't', 'r', 's', ' ', 'o', 'W', 'T', 'B', 'i', 'e', 'u', 'h', 'k'}

print(set(char_list+ list(sentence)))
# {'l', 'm', 'a', 'c', 't', 'r', 's', ' ', 'd', 'o', 'W', 'T', 'B', 'i', 'e', 'k', 'h', 'u', 'b'}

unique_char = set(char_list)
unique_char.add('x')
# unique_char.add(['y', 'z']) this is wrong
print(unique_char)

# {'x', 'b', 'd', 'c', 'a'}

unique_char.remove('x')
print(unique_char)
# {'b', 'd', 'c', 'a'}

unique_char.discard('d') #沒有元素避免報錯
print(unique_char)
# {'b', 'c', 'a'}

unique_char.clear()
print(unique_char)
# set()

unique_char = set(char_list)
print(unique_char.difference({'a', 'e', 'i'}))
# {'b', 'd', 'c'}

print(unique_char.intersection({'a', 'e', 'i'}))
# {'a'}