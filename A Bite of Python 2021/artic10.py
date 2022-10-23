# Функции

"""
 Имена, указанные в объявлении функции, называются параметрами,
тогда как значения, которые вы передаёте в функцию при её вызове, –
аргументами.
"""

# Глобальные переменные

x = 50


def func():
    global x

    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)


func()
print('Значение x составляет', x)

'''
 Зарезервированное слово global используется для того, чтобы объявить, 
что x – это глобальная переменная, а значит, 
когда мы присваиваем значение имени x внутри функции, 
это изменение отразится на значении переменной x 
в основном блоке программы.

 Используя одно зарезервированное слово global, можно объявить сразу
несколько переменных: global x, y, z.
'''

# Нелокальные переменные

'''
 Когда мы находимся внутри func_inner, переменная x, 
определённая в первой строке func_outer находится 
ни в локальной области видимости 
(определение переменной не входит в блок func_inner), 
ни в глобальной области видимости (она также 
и не в основном блоке программы). Мы объявляем, 
что хотим использовать именно эту переменную x, следующим образом:
nonlocal x.
'''


def func_outer():
    y = 2
    print('y равно', x)

    def func_inner():
        nonlocal y
        y = 5

    func_inner()
    print('Локальное y сменилось на', y)


func_outer()

# Значения аргументов по умолчанию

'''
 Функция под именем say используется для вывода на экран строки 
указанное число раз. Если мы не указываем значения, 
по умолчанию строка выводится один раз. 
Мы достигаем этого указанием значения аргумента по умолчанию,
равного 1 для параметра times.

 При первом вызове say мы указываем только строку, 
и функция выводит её один раз. 
При втором вызове say мы указываем также и аргумент 5, 
обозначая таким образом, что мы хотим сказать фразу 5 раз.
'''


def say(message, times=1):
    print(message * times)


say('Привет')
say('Мир ', 5)

# Ключевые аргументы

'''
 Если имеется некоторая функция с большим числом параметров, 
и при её вызове требуется указать только некоторые из них, 
значения этих параметров могут задаваться по их имени – 
это называется ключевые параметры. В этом случае 
для передачи аргументов функции используется имя (ключ) 
вместо позиции (как было до сих пор).

 Есть два преимущества такого подхода: во-первых, 
использование функции становится легче, 
поскольку нет необходимости отслеживать порядок аргументов; 
во-вторых, можно задавать значения только некоторым 
избранным аргументам, при условии,
что остальные параметры имеют значения аргумента по умолчанию.
'''


def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)

#

'''
 Когда мы объявляем параметр со звёздочкой (например, *param), 
все позиционные аргументы начиная с этой позиции 
и до конца будут собраны в кортеж под именем param.

 налогично, когда мы объявляем параметры с двумя звёздочками (**param),
все ключевые аргументы начиная с этой позиции и до конца будут собраны 
в словарь под именем param.
'''


def total(a=5, *numbers, **phonebook):
    print('a', a)
    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
        
    # проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

# Только ключевые параметры

'''
 Объявление параметров после параметра со звёздочкой 
даёт только ключевые аргументы. Если для таких аргументов не указано 
значение по умолчанию, и оно не передано при вызове, 
обращение к функции вызовет ошибку.

 Если вам нужны аргументы, передаваемые только по ключу, 
но не нужен параметр со звёздочкой, 
то можно просто указать одну звёздочку без указанияимени: 
def total(initial=5, *, extra_number).
'''


def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
        
    count += extra_number
    print(count)


total(10, 1, 2, 3, extra_number=50)

try:
    total(10, 1, 2, 3)
except TypeError:
    print('Вызовет ошибку, поскольку мы не указали '
          'значение аргумента по умолчанию для extra_number')

'''
 Строки документации

 Строка в первой логической строке функции является строкой документации
для этой функции. Обратите внимание на то, 
что строки документации применимы также к модулям и классам.

 Строки документации принято записывать в форме многострочной строки,
где первая строка начинается с заглавной буквы и заканчивается точкой. 
Вторая строка оставляется пустой, 
а подробное описание начинается с третьей. 
Вам настоятельно рекомендуется следовать такому формату 
для всех строк документации всех ваших нетривиальных функций.
'''