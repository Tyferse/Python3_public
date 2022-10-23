"""
 Можно убедиться в том, что квадратный корень из двух
можно выразить в виде бесконечно длинной дроби.

  √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

 Приблизив это выражение для первых четырех итераций, получим:

  1 + 1/2 = 3/2 = 1.5
  1 + 1/(2 + 1/2) = 7/5 = 1.4
  1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
  1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

 Следующие три приближения: 99/70, 239/169 и 577/408,
а восьмое приближение, 1393/985, является первым случаем,
в котором количество цифр в числителе
превышает количество цифр в знаменателе.

 У скольких дробей длина числителя больше длины знаменателя
в первой тысяче приближений выражения?
"""


def compute():
    LIMIT = 1000
    ans = 0
    numer = 0
    denom = 1
    for _ in range(LIMIT):
        numer, denom = denom, denom * 2 + numer
        # Сейчас числитель/знаменатель - это i-ная (основанная на 0)
        # аппроксимация непрерывной дроби sqrt (2) - 1
        # Now numer/denom is the i'th (0-based)
        # continued fraction approximation of sqrt(2) - 1
        if len(str(numer + denom)) > len(str(denom)):
            ans += 1
            
    return str(ans)


if __name__ == "__main__":
    print(compute())