# Реалізуйте ітератор для перебору всіх ключів словника.

def dict_keys_iterator(diction):
    for i in diction.keys():
        yield i


dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = dict_keys_iterator(dictionary)

for key in dict_iter:
    print(key)
