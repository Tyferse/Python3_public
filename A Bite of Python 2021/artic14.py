# Объектно-ориентированное программирование

"""
 До сих пор наши программы состояли из функций, т.е. блоков выражений,
которые манипулируют данными. Это называется
процедурно-ориентированным стилем программирования.
Существует и другой способ организации программ:
объединять данные и функционал внутри некоего объекта.
Это называется объектно-ориентированной парадигмой программирования.
В большинстве случаев можно ограничиться процедурным программированием,
а при написании большой программы или если решение конкретной задачи
того требует, можно переходить к техникам
объектно-ориентированного программирования.

 Два основных аспекта объектно-ориентированного программирования –
классы и объекты. Класс создаёт новый тип,
а объекты являются экземплярами класса. Аналогично,
когда мы говорим о «переменных типа int», это означает, что переменные,
которые хранят целочисленные значения,
являются экземплярами (объектами) класса int.

 бъекты могут хранить данные в обычных переменных,
которые принадлежат объекту. Переменные,
принадлежащие объекту или классу, называют полями.
Объекты могут также обладать функционалом, т.е. иметь функции,
принадлежащие классу. Такие функции принято называть методами класса.
Эта терминология важна, так как она помогает нам отличать
независимые функции и переменные от тех,
что принадлежат классу или объекту.
Всё вместе (поля и методы) принято называть атрибутами класса.
Поля бывают двух типов: они могут принадлежать
каждому отдельному экземпляру объекта класса или всему классу.
Они называются переменными экземпляра
и переменными класса соответственно.
"""

# self

'''
 Методы класса имеют одно отличие от обычных функций: 
они должны иметь дополнительно имя,  
добавляемое к началу списка параметров. Однако, 
при вызове метода никакого значения этому параметру 
присваивать не нужно – его укажет Python. 
Эта переменная указывает на сам объект экземпляра класса, 
и по традиции она называется self.

 Вы, должно быть, удивляетесь, как Python присваивает значение self 
и почему вам не нужно указывать это значение самостоятельно. 
Поясним это на примере. Предположим, у нас есть класс с именем MyClass 
и экземпляр этого класса с именем myobject. 
При вызове метода этого объекта, например, 
«myobject.method(arg1, arg2)», Python автоматически превращает это в 
«MyClass.method(myobject, arg1, arg2)» – в этом и состоит смысл self.
'''

# Класс

'''
 Объект-экземпляр класса, записывая имя класса со скобками. 
Для проверки мы выясняем тип переменной, просто выводя её на экран. 
Так мы видим, что у нас есть экземпляр класса Person в модуле __main__.

 Обратите внимание, что выводится также и адрес в памяти компьютера, 
где хранится ваш объект. На вашем компьютере адрес будет другим, 
так как Python хранит объекты там, где имеется свободное место.
'''

# Метод __init__

'''
 Здесь мы определяем метод __init__ так, чтобы он принимал параметр name
(наряду с обычным self). Далее мы создаём новое поле с именем name. 
Обратите внимание, что это две разные переменные, даже несмотря на то, 
что они обе названы name. Это не проблема, 
так как точка в выражении self.name обозначает,
что существует нечто с именем «name», являющееся частью объекта «self», 
и другое name – локальная переменная. 
Поскольку мы в явном виде указываем, к которому имени мы обращаемся, 
путаницы не возникнет. Для создания нового экземпляра p класса Person 
мы указываем имя класса, после которого – аргументы в скобках:
p = Person('Swaroop').

 Метод __init__ мы при этом не вызываем явным образом.
В этом и заключается специальная роль данного метода.
'''


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Привет! Меня зовут', self.name)


p = Person('Swaroop')
p.say_hi()
# Предыдущие 2 строки можно
# Person('Swaroop').say_hi()

# Переменные коасса и объекта

'''
 Данные, т.е. поля, являются не чем иным, как обычными переменными, 
заключёнными в пространствах имён классов и объектов. Это означает,
что их имена действительны только в контексте этих классов или объектов.
Отсюда и название «пространство имён».

 Существует два типа полей: переменные класса и переменные объекта, 
которые различаются в зависимости от того, 
принадлежит ли переменная классу или объекту соответственно.

 Переменные класса разделяемы – доступ к ним могут получать 
все экземпляры этого класса. Переменная класса существует только одна, 
поэтому когда любой из объектов изменяет переменную класса, 
это изменение отразится и во всех остальных экземплярах того же класса.

 Переменные объекта принадлежат каждому отдельному экземпляру класса. 
В этом случае у каждого объекта есть своя собственная копия поля, 
т.е. не разделяемая и никоим образом не связанная 
с другими такими же полями в других экземплярах.
'''


class Robot:
    """Представляет робота с именем."""
    # Переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        """Инициализация данных."""
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1

    def __del__(self):
        """Я умираю."""
        print('{0} уничтожается!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'\
                  .format(Robot.population))

    def sayHi(self):
        """
        Приветствие робота.

        Да, они это могут.
        """
        print('Приветствую! Мои хозяева называют меня {0}.'\
              .format(self.name))

    @staticmethod  # Это тоже самое,
    # что и howMany = staticmethod(howMany)
    def howMany():
        """Выводит численность роботов."""
        print('У нас {0:d} роботов.'.format(Robot.population))


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany()

# Наследование

'''
 Если мы добавим/изменим какую-либо функциональность в SchoolMember, 
это автоматически отобразится и во всех подтипах. Например, 
мы можем добавить новое поле удостоверения 
для преподавателей и студентов, просто добавив его 
к классу SchoolMember. С другой стороны, 
изменения в подтипах никак не влияют на другие подтипы. 
Ещё одно достоинство состоит в том, 
что обращаться к объекту преподавателя 
или студента можно как к объекту SchoolMember,
что может быть полезно в ряде случаев, например, 
для подсчёта количества человек в школе. 
Когда подтип может быть подставлен в любом месте, 
где ожидается родительский тип, т.е. объект считается экземпляром 
родительского класса, это называется полиморфизмом.

 Заметьте также, что код родительского класса используется многократно,
и нет необходимости копировать его во все классы, 
как пришлось бы в случае использования независимых классов.

 Класс SchoolMember в этой ситуации называют базовым классом 
или надклассом. Классы Teacher и Student 
называют производными классами или подклассами.
'''


class SchoolMember:
    """Представляет любого человека в школе."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    def tell(self):
        """Вывести информацию."""
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name,
                                               self.age),
              end=" ")


class Teacher(SchoolMember):
    """Представляет преподавателя."""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    """Представляет студента."""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()  # печатает пустую строку

members = [t, s]
for member in members:
    member.tell()  # работает как для преподавателя, так и для студента

'''
 Чтобы воспользоваться наследованием, 
при определении класса мы указываем имена его базовых классов 
в виде кортежа, следующего сразу за его именем. 
Далее мы видим, что метод __init__ базового класса вызывается явно 
при помощи переменной self, чтобы инициализировать часть объекта,
относящуюся к базовому классу. Это очень важно запомнить: 
поскольку мы определяем метод __init__ в подклассах Teacher и Student, 
Python не вызывает конструктор базового класса 
SchoolMember автоматически – его необходимо вызывать самостоятельно 
в явном виде.

 Напротив, если мы не определим метод __init__ в подклассе,
Python вызовет конструктор базового класса автоматически.

 Здесь же мы видим, как можно вызывать методы базового класса,
предваряя запись имени метода именем класса, 
а затем передавая переменную self вместе с другими аргументами.

 При вызове метода tell из класса SchoolMember экземпляры Teacher 
или Student можно использовать как экземпляры SchoolMember.

 Если при наследовании перечислено более одного класса, 
это называется множественным наследованием.
 
 Параметр end используется в методе tell() для того, 
чтобы новая строка начиналась через пробел после вызова print().
'''

# Метаклассы

'''
 Точно так же, как классы используются для создания объектов, 
можно использовать метаклассы для создания классов. 
Метаклассы существуют для изменения 
или добавления нового поведения в классы.

 Давайте рассмотрим пример. Допустим, мы хотим быть уверены, 
что мы всегда создаём исключительно экземпляры подклассов 
класса SchoolMember, и не создаём экземпляры самого класса SchoolMember.

 Для достижения этой цели мы можем использовать концепцию под названием
«абстрактные базовые классы». Это означает, что такой класс абстрактен,
т.е. является лишь некой концепцией, 
не предназначенной для использования в качестве реального класса.

 Мы можем объявить наш класс как абстрактный базовый класс 
при помощи встроенного метакласса по имени ABCMeta.
'''

from abc import *


class SchoolMember2(metaclass=ABCMeta):
    """Представляет любого человека в школе."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        """Вывести информацию."""
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age),
              end=" ")


class Teacher2(SchoolMember2):
    """Представляет преподавателя."""

    def __init__(self, name, age, salary):
        SchoolMember2.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember2.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student2(SchoolMember2):
    """Представляет студента."""
    def __init__(self, name, age, marks):
        SchoolMember2.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember2.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


t = Teacher2('Mrs. Shrividya', 40, 30000)
s = Student2('Swaroop', 25, 75)

# m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# SchoolMember with abstract methods tell"

print()  # печатает пустую строку

members = [t, s]
for member in members:
    member.tell()  # работает как для преподавателя, так и для студента