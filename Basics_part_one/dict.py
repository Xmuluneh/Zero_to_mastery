#!/usr/bin/python3
'''
Dictionary is unordered key value pair
root_dic = {
key:value
}
'''

my_dict = {'a': 1, 'b': 2}
'''print(my_dict['a'])
print(id(my_dict))
my_dict = {'a': 1, 'b': 2, 'c': 7}
print(id(my_dict))
user = dict(name='root')
print(user)
print(my_dict)
my_dict.clear()
print(my_dict)'''

print(my_dict)
print(my_dict.popitem())
my_dict.update({'a': 10})
print(my_dict)
'''
tuple immutable ds
'''
my_tuple = (1, 23, 3, 4, 5)
print(my_tuple)
