"""
 Пятизначное число 16807 = 75 является также пятой степенью
натурального числа. Аналогично, девяти значное число 134217728 = 89
является девятой степенью.

 Сколько существует n-значных натуральных чисел,
являющихся также и n-ми степенями натуральных чисел?
"""

count = 0

for n in range(1, 100):
    for a in range(100000):
        if len(str(pow(a, n))) == n:
            count += 1

print(count)
