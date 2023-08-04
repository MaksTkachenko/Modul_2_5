# Реалізуйте ітератор для перебору всіх ключів словника.

class DictKeysIterator:

    def __init__(self, diction):
        self.diction = diction
        self.index = 0
        self.keys = list(dictionary.keys())

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < len(self.diction.keys()):

            key_2 = self.keys[self.index]
            self.index += 1
            return key_2
        else:
            raise StopIteration


dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = DictKeysIterator(dictionary)

for key in dict_iter:
    print(key)
