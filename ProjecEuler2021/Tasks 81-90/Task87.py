"""
 Наименьшее число, которое можно представить
в виде суммы квадрата простого числа, куба простого числа
и четвертой степени простого числа, равно 28. Между прочим,
существует ровно 4 таких числа меньше пятидесяти,
которые можно представить в виде суммы указанным способом:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

 Сколько чисел до пятидесяти миллионов можно представить
в виде суммы квадрата, куба и четвертой степени простых чисел?
"""

import eulerlib

LIMIT = 50000000
nums = range(1, LIMIT)
sums = set()

primes = eulerlib.primes(int(LIMIT**0.5) + 1)

for c in eulerlib.primes(LIMIT**0.25):
    for b in eulerlib.primes(LIMIT**(1/3)):
        for a in primes:
            sum1 = a**2 + b**3 + c**4
            if sum1 not in sums and sum1 in nums:
                sums.add(sum1)

print(len(sums))
