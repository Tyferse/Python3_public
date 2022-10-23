"""
 Первое из известных простых чисел,
длина которого превышает миллион цифр, было открыто в 1999 году.
Это - простое число Мерсенна, имеющее вид 2^6972593 − 1;
оно состоит ровно из 2 098 960 цифр.
Позже были найдены другие простые числа Мерсенна,
имеющие вид 2p−1, длина которых еще больше.

 Однако, в 2004 году было найдено огромное простое число,
не являющееся числом Мессена, которое состоит из 2 357 207 цифр:
28433 × 2^7830457 + 1.

 Найдите последние десять цифр этого простого числа.
"""

# MOD - число с десятью нулями
MOD = 10**10
# От данного числа берётся остаток от деления на MOD,
# т. е. последние десять цифр
ans = (28433 * pow(2, 7830457, MOD) + 1) % MOD

print(ans)