# Створіть ітератор, який перебирає всі паліндроми (слова, які читаються однаково
# зліва направо та зправа наліво) з заданого списку слів.

class PalindromeIterator:

    def __init__(self, words: list):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.index < len(self.words):

            result = self.words[self.index]
            self.index += 1
            if result == result[::-1]:
                return result

        raise StopIteration


words_list = ['level', 'racecar', 'python', 'madam']
palindrome_iter = PalindromeIterator(words_list)
for word in palindrome_iter:
    print(word)
