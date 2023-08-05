# Напишіть генератор, який видає послідовність простих чисел.


def fun_prime_number(num: int):
    if num < 2:
        return False

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def prime_generator():
    num = 2
    while True:
        if fun_prime_number(num):
            yield num
        num += 1


prime_gen = prime_generator()
for i in range(10):
    print(next(prime_gen))
