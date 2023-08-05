# Створіть ітератор, який перебирає всі парні числа з заданого діапазону.


class EvenRangeIterator:

    def __init__(self, start, end):
        self.numbers = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.numbers <= self.end:

            if self.numbers % 2 == 0:
                result = self.numbers
                self.numbers += 2
                return result

            self.numbers += 1

        raise StopIteration


even_nums = EvenRangeIterator(1, 10)
for num in even_nums:
    print(num)
