# Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде
# повертати наступний символ рядку.


def string_iterator(text: str):
    for symbol in text:
        yield symbol


string = "Hello, World!"
str_iter = string_iterator(string)
for char in str_iter:
    print(char)
