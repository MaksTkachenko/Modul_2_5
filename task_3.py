# Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде
# повертати наступний символ рядку.


class StringIterator:
    def __init__(self, line):
        self.line = line
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        len_line = len(self.line)
        if self.index < len_line:
            symbol = self.line[self.index]
            self.index += 1
            return symbol
        else:
            raise StopIteration


string = "Hello, World!"
str_iter = StringIterator(string)
for char in str_iter:
    print(char)
