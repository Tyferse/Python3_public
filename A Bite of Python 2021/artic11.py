# Модули

"""
 Если бы это был не скомпилированный модуль, т.е. модуль,
написанный на Python, тогда интерпретатор Python
искал бы его в каталогах, перечисленных в переменной sys.path.
Если модуль найден, выполняются команды в теле модуля,
и он становится доступным.
"""

import sys


print('Аргументы командной строки:')

for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

'''
 В нашем примере, когда мы запускаем 
 
«python using_sys.py we are arguments», 

мы запускаем модуль using_sys.py командой python, а всё,
что следует далее – аргументы, передаваемые программе3. 
Python сохраняет аргументы командной строки в переменной sys.argv 
для дальнейшего использования.

 Помните, что имя запускаемого сценария
всегда является первым аргументом в списке sys.argv. 
Так что в приведённом примере 'using_sys.py' 
будет элементом sys.argv[0], 'we' – sys.argv[1], 
'are' – sys.argv[2], а 'arguments' – sys.argv[3].
'''

'''
 Импорт модуля – относительно дорогостоящее мероприятие, 
поэтому Python предпринимает некоторые трюки 
для ускорения этого процесса. Один из способов – 
создать байт-компилированные файлы (или байткод) с расширением .pyc,
которые являются некой промежуточной формой, 
в которую Python переводит программу. Такой файл .pyc полезен 
при импорте модуля в следующий раз в другую программу – 
это произойдёт намного быстрее, поскольку значительная часть обработки, 
требуемой при импорте модуля, будет уже проделана. 
Этот байткод также является платформо-независимым.
'''

from math import *


n = int(input("Введите диапазон:- "))
p = [2, 3]
count = 2
a = 5

while count < n:
    b = 0
    for i in range(2, a):
        if i <= sqrt(a):
            if a % i == 0:
                b = 1
            else:
                pass
            
    if b != 1:
        print(a, "простое")
        p = p + [a]
        
    count = count + 1
    a = a + 2

k = 0
for num in range(int((n/(n/20)))):
    if str(p[k: k+29]) == '[]':
        continue
        
    print(p[k: k+29])
    k += 30

# Имя модуля

'''
 каждого модуля есть имя, и команды в модуле могут узнать имя их модуля. 
Это полезно, когда нужно знать, запущен ли модуль 
как самостоятельная программа или импортирован. 
Как уже упоминалось выше, когда модуль импортируется впервые, 
содержащийся в нём код исполняется. Мы можем воспользоваться этим 
для того, чтобы заставить модуль вести себя по-разному 
в зависимости от того, используется ли он сам по себе или импортируется 
в другую программа. Этого можно достичь
с применением атрибута модуля под названием __name__.
'''

if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')

# Импорт своих модулей (по названию файла)

import artic11_modl

artic11_modl.sayhi()
print('Версия', artic11_modl.__version__)


from artic11_modl import sayhi, __version__

sayhi()
print('Версия', __version__)

# Функция dir

'''
 Встроенная функция dir() возвращает список имён, определяемых объектом. 
Например, для модуля в этот список входят функции, классы и переменные, 
определённые в этом модуле.

 Эта функция может принимать аргументы. 
Если в качестве аргумента указано имя модуля, 
она возвращает список имён, определённых в этом модуле. 
Если никакого аргумента не передавать, она вернёт список имён, 
определённых в текущем модуле.
'''

print(dir(sys))

# Пакеты

'''
 Пакеты – это просто каталоги с модулями 
и специальным файлом __init__.py, который показывает Python, 
что этот каталог особый, так как содержит модули Python.
'''

'''
| - <некоторый каталог из sys.path>/
|   |---- world/
|       |---- __init__.py
|       |---- asia/
|       |   |---- __init__.py
|       |   |---- india/
|       |       |---- __init__.py
|       |       |---- foo.py
|       |---- africa/
|           |---- __init__.py
|           |---- madagascar/
|               |---- __init__.py
|               |---- bar.py
'''
