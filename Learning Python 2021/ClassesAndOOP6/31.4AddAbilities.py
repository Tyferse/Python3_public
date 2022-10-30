"""
 Упражнения к шестой части

 В этих упражнениях вам будет предложено написать несколько классов
и поэкспериментировать с существующим программным кодом. Единственная
проблема существующего кода состоит в том, что он должен существовать.
Чтобы поэкспериментировать с набором классов в упражнении 5, вам нужно
либо загрузить файл с исходными текстами с веб-сайта книги (читайте
предисловие), или ввести его вручную (он достаточно короткий). Поскольку
программы становятся все сложнее, обязательно ознакомьтесь с решениями
в конце книги. Решения вы найдете в приложении B, в разделе «Часть VI,
Классы и ООП».

 1. Наследование. Напишите класс с именем Adder, экспортирующий метод
add(self, x, y), который выводит сообщение «Not Implemented»
(«Не реализовано»). Затем определите два подкласса класса Adder, которые
реализуют метод add:

 ListAdder

  С методом add, который возвращает результат конкатенации двух списков
 из аргументов.

 DictAdder

  С методом add, который возвращает новый словарь, содержащий элементы
 из обоих словарей, передаваемых как аргументы (подойдет любое
 определение сложения).

 Поэкспериментируйте с экземплярами всех трех классов в интерактивной
оболочке, вызывая их методы add.

 Теперь расширьте супер-класс Adder, добавив сохранение объекта
в экземпляре с помощью конструктора (например, присваивая список
или словарь атрибуту self.data), и реализуйте перегрузку оператора +
с помощью метода __add__ так, чтобы он автоматически вызывал ваш метод
add (например, выражение X + Y должно приводить к вызову метода
X.add(X.data, Y)). Где лучше разместить методы конструктора и перегрузки
оператора (то есть в каком из классов)? Объекты какого типа смогут
складывать ваши классы?

 На практике гораздо проще написать метод add, который принимает один
действительный аргумент (например, add(self, y)) и складывает его
с текущими данными экземпляра (например, self.data + y). Будет ли
в такой реализации больше смысла, чем в реализации, которая принимает
два аргумента? Можно ли сказать, что это делает ваши классы более
«объектно-ориентированными»?
"""


class Adder:
    def add(self, x, y):
        print('Not Implemented!')


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        x.update(y)
        return x


x, y, z = Adder(), ListAdder(), DictAdder()
x.add(1, 6)
print(y.add([7, 9, 2], [1, 7, 34]))
print(z.add({'n': 56, 'm': 156, 'r': 500},
            {'n': 67, 'r': 777, 'h': 995}))


class Adder:
    def __init__(self):
        self.data = []

    def __add__(self, b):
        return ListAdder.add(self, self.data, b)

    def add(self, x):
        self.data += x
        return self.data


w = Adder()
print(w + [34], w.add([66]), w.data + [7])

"""
 2. Перегрузка операторов. Напишите класс с именем MyList, который 
«обертывает» списки языка Python: он должен перегружать основные
операторы действий над списками, включая +, доступ к элементам 
по индексу, итерации, извлечение среза и такие методы списка, как append
и sort. Полный перечень методов, поддерживаемых списками, вы найдете
в справочном руководстве по языку Python. Кроме того, напишите 
конструктор для своего класса, который принимает существующий список
(или экземпляр класса MyList) и копирует его в атрибут экземпляра. 
Поэкспериментируйте со своим классом в интерактивной оболочке. В ходе
экспериментов выясните следующее:

 a. Почему здесь так важно копировать начальное значение?
 
 b. Можно ли использовать пустой срез (например, start[:]) 
для копирования начального значения, если им является экземпляр MyList?

 c. Существует ли универсальный способ передачи управления методам
обернутого списка?

 d. Можно ли складывать MyList и обычный список? А список и MyList?
 
 e. Объект какого типа должны возвращать операции сложения и извлечения
среза? А операции извлечения элементов по индексу?

 f. Если у вас достаточно новая версия Python (2.2 или выше), вы сможете 
реализовать такого рода класс-обертку, встраивая настоящий список 
в отдельный класс или наследуя класс list. Какой из двух способов проще 
и почему?
"""


class MyList(list):
    def __init__(self, *args):
        self.L = list(*args)

    def __add__(self, other):
        return self.L + other

    def __radd__(self, other):
        return other + self.L

    def __getitem__(self, item):
        return self.L[item]

    def __iter__(self):
        return iter(self.L)

    def __next__(self):
        for i in self.L:
            yield i

    def append(self, item):
        self.L += [item]

    def sort(self):
        if len(self.L) < 2:
            return self.L
        else:
            pivot = self.L[0]
            less = [i for i in self.L[1:] if i < pivot]

        greater = [i for i in self.L[1:] if i > pivot]

        return MyList(less).sort() + [pivot] + MyList(greater).sort()


class ListCopy:
    def __init__(self, L):
        self.L = L[:]


x = MyList([6, 9, 123, 564])
print(x[0], ListCopy(x).L, x + [4, 75], [0, 1] + x)

"""
 3. Подклассы. Напишите подкласс с именем MyListSub, наследующий класс
MyList из упражнения 2, который расширяет класс MyList возможностью
вывода сообщения на stdout перед выполнением каждой перегруженной
операции и подсчета числа вызовов. Класс MyListSub должен наследовать
методы MyList. При сложении MyListSub с последовательностями должно 
выводиться сообщение, увеличиваться счетчик вызовов операции сложения
и вызываться метод суперкласса. Кроме того, добавьте новый метод, 
который будет выводить счетчики операций на stdout, 
и поэкспериментируйте с этим классом в интерактивной оболочке. 
Как работают ваши счетчики - считают ли они операции для всего класса 
(для всех экземпляров класса) или для каждого экземпляра в отдельности?
Как бы вы реализовали каждый из этих случаев
"""

import sys


class MyListSub(MyList):
    clsops = 0

    def __init__(self, *args):
        MyList.__init__(self, *args)
        MyListSub.output(self)

    def output(self):
        MyListSub.clsops += 1
        self.ops += 1
        sys.stdout.write('Class = {0}, instance = {1}\n'
                         .format(MyListSub.clsops, self.ops))

    def __add__(self, other):
        MyList.__add__(self, other)
        MyListSub.output(self)

    def __radd__(self, other):
        MyList.__radd__(self, other)
        MyListSub.output(self)

    def __getitem__(self, item):
        MyList.__getitem__(self, item)
        MyListSub.output(self)

    def __iter__(self):
        MyList.__iter__(self)
        MyListSub.output(self)

    def __next__(self):
        MyList.__next__(self)
        MyListSub.output(self)

    def append(self, item):
        MyList.append(self, item)
        MyListSub.output(self)

    def sort(self):
        MyList.sort(self)
        MyListSub.output(self)

    def __getattr__(self, attr):
        if attr == 'ops':
            return 0
        else:
            return getattr(self, attr)


x = MyListSub([6, 9, 123, 564])
x.sort()
print(x)
y = MyListSub([12, 5, 6, 4])
x = x + [4]
y = [56] + y
print(x, y)

"""
 4. Методы метакласса. Напишите класс с именем Meta с методами, которые
перехватывают все обращения к атрибутам (как получение значения, так
и присваивание) и выводят сообщения, перечисляющие их аргументы, на
stdout. Создайте экземпляр класса Meta и поэкспериментируйте с ним 
в интерактивной оболочке. Что произойдет, если попытаться использовать
экземпляр класса в выражении? Попробуйте выполнить над своим классом
операции сложения, доступа к элементам по индексу и получения среза.
"""

import abc


class Meta(metaclass=abc.ABCMeta):
    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def __getattr__(cls, attr):
        return cls.attr

    @classmethod
    def __setattr__(cls, attr, value):
        cls.attr = value

    @classmethod
    def output(cls):
        for arg in cls.__dict__:
            sys.stdout.write(arg)
            print('')


C = Meta(MyList)
C.output()

"""
 5. Объекты множеств. Поэкспериментируйте с набором классов, описанных
в разделе «Расширение типов встраиванием». Выполните команды, которые 
выполняют следующие операции:

  Создайте два множества целых чисел и найдите их пересечение 
 и объединение с помощью операторов & и |.
 
  Создайте множество из строки и поэкспериментируйте с извлечением
 элементов множества по индексу. Какой метод в классе 
 при этом вызывается?
 
  Попробуйте выполнить итерации через множество, созданное из строки,
 с помощью цикла for. Какой метод вызывается на этот раз?
 
  Попробуйте найти пересечение и объединение множества, созданного 
 из строки, и простой строки. Возможно ли это?
 
  Теперь расширьте класс множества наследованием, чтобы подкласс мог
 обрабатывать произвольное число операндов, используя для этого форму
 аргумента *args. (Подсказка: вернитесь к рассмотрению этих алгоритмов
 в главе 18.) Найдите пересечение и объединение нескольких операндов
 с помощью вашего подкласса множества. Как можно реализовать вычисление 
 пересечения трех и более множеств, если оператор & работает всего 
 с двумя операндами?

  Как бы вы реализовали другие операции над списками в классе множества?
"""


set1 = set([1, 5, 6, 45, 32, 2])
set2 = set([1, 6, 7, 3, 8])

print(set1 | set2, set1 & set2)

set3 = set('an spamings')

print(set3)

for i in set3:
    print(i, end=' ')


class NSet(set):
    def __init__(self, it):
        self.it = set(it)

    def intersection(self, *args) -> set:
        for arg in args:
            set.intersection(self.it, arg)

        return self.it


"""
 6. Связи в дереве классов. В разделе «Пространства имен: окончание 
истории» в главе 28 и в разделе «Множественное наследование: примесные 
классы» в главе 30 я упоминал, что классы имеют атрибут __bases__, 
который возвращает кортеж объектов супер-классов (тех, что перечислены
в круглых скобках в заголовке инструкции class). Используя атрибут
__bases__, расширьте классы в файле lister.py (глава 30) так, чтобы они
выводили имена прямых супер-классов экземпляров класса. При этом первая
строка в этом выводе должна выглядеть, как показано ниже (значение 
адреса у вас может отличаться):

<Instance of Sub(Super, ListTree), address 7841200:
"""


from PatternProj303 import ListInstance, ListInherited, ListTree, Sub


class SomeList(ListInherited):
    def __init__(self, kls):
        self.kls = kls

    def __str__(self):
        return f'<Instance of {self.kls.__name__}' \
               f'{self.__basenames()}, address {id(self.kls)}'

    def __basenames(self):
        S = '('
        for base in self.kls.__bases__:
            S += str(base.__name__) + ', '

        return S + ')'


x = SomeList(Sub)
y = SomeList(ListInstance)
z = SomeList(ListTree)

for I in (x, y, z):
    print(I)


"""
 7. Композиция. Сымитируйте сценарий оформления заказа в ресторане
быстрого питания, определив четыре класса:

 Lunch
 
  Вмещающий и управляющий класс.
  
 Customer
 
  Действующее лицо, покупающее блюдо.
  
 Employee
 
  Действующее лицо, принимающее заказ.
  
 Food
  То, что приобретает заказчик.
  
 Чтобы вам было с чего начать, определите следующие классы и методы:
 
 
class Lunch:
    def __init__(self) # Создает и встраивает Customer и Employee
    def order(self, foodName) # Имитирует прием заказа
    def result(self) # Запрашивает у клиента название блюда
    
    
class Customer:
    def __init__(self) # Инициализирует название блюда значением None
    def placeOrder(self, foodName, employee) # Передает заказ официанту
    def printFood(self) # Выводит название блюда
    
    
class Employee:
    def takeOrder(self, foodName)
    # Возвращает блюдо с указанным названием
    
class Food:
    def __init__(self, name) # Сохраняет название блюда
    
    
 Имитация заказа работает следующим образом:
 
  a. Конструктор класса Lunch должен создать и встроить экземпляр класса
 Customer и экземпляр класса Employee, а кроме того, экспортировать
 метод с именем order. При вызове этот метод должен имитировать прием
 заказа у клиента (Customer) вызовом метода placeOrder. Метод placeOrder
 класса Customer должен в свою очередь имитировать получение блюда 
 (новый объект Food) у официанта (Employee) вызовом метода takeOrder
 класса Employee.

  b. Объекты типа Food должны сохранять строку с названием блюда 
 (например, «буррито»), которое передается через Lunch.order 
 в Customer.placeOrder, затем в Employee.takeOrder и, наконец, 
 в конструктор класса Food. Кроме того, класс Lunch должен 
 еще экспортировать метод result, который предлагает клиенту (Customer) 
 вывести название блюда, полученного от официанта (Employee)
 в результате выполнения заказа (этот метод может использоваться 
 для проверки имитации).

 Обратите внимание: экземпляр класса Lunch должен передавать клиенту
(Customer) либо экземпляр класса Employee (официант), либо себя самого, 
чтобы клиент (Customer) мог вызвать метод официанта (Employee).
Поэкспериментируйте с получившимися классами в интерактивной оболочке, 
импортируя класс Lunch и вызывая его метод order, чтобы запустить
имитацию, а также метод result, чтобы проверить, что клиент (Customer)
получил именно то, что заказывал. При желании можете добавить в файл
с классами программный код самотестирования, используя прием с атрибутом
__name__ из главы 24. В этой имитации активность проявляет клиент 
(Customer); как бы вы изменили свои классы, чтобы инициатором
взаимодействий между клиентом и официантом был официант (Employee)?
"""


class Lunch:
    def __init__(self):  # Создает и встраивает Customer и Employee
        self.rob = Employee('rob')

    def order(self, foodName):  # Имитирует прием заказа
        self.dish = Food(foodName)
        print(Customer().placeOrder(self.dish, self.rob),
              'is cooking by', str(self.rob.name))

    def result(self):  # Запрашивает у клиента название блюда
        import time
        
        time.sleep(3)
        print(self.dish.food, 'is done!')


class Customer:
    def __init__(self):  # Инициализирует название блюда значением None
        self.foodName = None

    def placeOrder(self, foodName, employee):
        # Передает заказ официанту
        self.foodName = foodName
        return employee.takeOrder(self.foodName)

    def printFood(self):  # Выводит название блюда
        print(self.foodName)


class Employee:
    def __init__(self, name):
        self. name = name

    def takeOrder(self, foodName):  # Возвращает блюдо
        #                             с указанным названием
        return foodName.food


class Food:
    def __init__(self, name):  # Сохраняет название блюда
        self.food = name


if __name__ == '__main__':
    ronald = Lunch()
    ronald.order('churchkhela')
    ronald.result()


"""
 8. Классификация животных в зоологии. Изучите дерево классов, 
представленное на рис. Напишите шесть инструкций class, которые 
имитировали бы эту модель классификации средствами наследования 
в языке Python. Затем добавьте к каждому из классов метод speak, который 
выводил бы уникальное сообщение, и метод reply в супер-классе Animal,
являющемся вершиной иерархии, который просто вызывал бы self.speak,
чтобы вывести текст сообщения, характерного для каждой категории,
в подклассах, расположенных ниже (это вынудит начинать поиск в дереве 
наследования от экземпляра self). Наконец, удалите метод speak из класса 
Hacker, чтобы для него по умолчанию выводилось сообщение, унаследованное 
от класса выше. Когда вы закончите, ваши классы должны работать 
следующим образом:

% python
>>> from zoo import Cat, Hacker
>>> spot = Cat()
>>> spot.reply()  # Animal.reply; вызывается Cat.speak
meow
>>> data = Hacker()  # Animal.reply; вызывается Primate.speak
>>> data.reply()
Hello world!
"""


class Animal:
    def __init__(self):
        self.speak = 'This is any animal.'

    def reply(self):
        print(self.speak)


class Mammal(Animal):
    def __init__(self):
        self.speak = 'This animal is mammal.'

    def reply(self):
        print(self.speak)


class Cat(Mammal):
    def __init__(self):
        self.speak = 'meow'

    def reply(self):
        print(self.speak)


class Dog(Mammal):
    def __init__(self):
        self.speak = 'This mammal is dog.'

    def reply(self):
        print(self.speak)


class Primate(Mammal):
    def __init__(self):
        self.speak = 'This mammal is one of the monkeys.'

    def reply(self):
        print(self.speak)


class Hacker(Primate):
    def __init__(self):
        self.speak = 'Breaking servers of Pentagon.'

    def reply(self):
        print(self.speak)


"""
 9. Сценка с мертвым попугаем. Изучите схему встраивания объектов, 
представленную на рис. 31.2. Напишите набор классов на языке Python, 
которые реализовали бы эту схему средствами композиции. Класс Scene 
(сцена) должен определять метод action и встраивать в себя экземпляры 
классов Customer (клиент), Clerk (клерк) и Parrot (попугай), каждый
из которых должен определять метод line, выводящий уникальное сообщение.
Встраиваемые объекты могут наследовать один общий суперкласс, 
определяющий метод line, который просто выводит текст указанного ему 
сообщения, или определяют собственные реализации метода line. В конечном
итоге ваши классы должны действовать, как показано ниже:

% python
>>> import parrot
>>> parrot.Scene().action()  # Активировать встроенные объекты
customer: “that’s one ex-bird!”
clerk: “no it isn’t...”
parrot: None
"""


class Scene:
    @staticmethod
    def line(I):
        print(I.massange)

    def action(self):
        for character in (Customer(), Clerk(), Parrot()):
            Scene.line(character)


class Customer:
    def __init__(self):
        self.massange = 'customer: “that’s one ex-bird!”'


class Clerk:
    def __init__(self):
        self.massange = 'clerk: “no it isn’t...”'


class Parrot:
    def __init__(self):
        self.massange = 'parrot: None'


if __name__ == '__main__':
    Scene().action()


"""
 Придется держать в уме: ООП глазами специалистов
 
 Когда я рассказываю о классах в языке Python, я все время обнаруживаю,
что в середине лекции о классах люди, имевшие опыт ООП в прошлом, 
заметно активизируются, а те, кто такого опыта не имеет, начинают
сникать (или вообще засыпают). Преимущества этой технологии 
не так очевидны.

 В такой книге, как эта, у меня есть уникальная возможность включить
обзорный материал, которой я воспользовался в главе 25, – настоятельно 
рекомендую вам перечитать эту главу, как только вам начинает казаться,
что ООП – это всего лишь некоторое украшение в программировании.

 В реальной аудитории, чтобы привлечь (и удержать) внимание начинающих 
программистов, я обычно останавливаюсь и спрашиваю у присутствующих 
опытных специалистов, почему они используют ООП. Ответы, которые 
они дают, могут пролить свет на цели, которые преследует ООП, для тех,
кто плохо знаком с этой темой.

 Ниже приводятся лишь самые общие причины, побуждающие использовать ООП, 
которые были высказаны моими студентами за эти годы:

 Повторное использование программного кода
 
  Это самая простая (и самая основная) причина использования ООП.
 Возможность наследования в классах позволяет программисту писать 
 программы, адаптируя существующий программный код, а не писать 
 каждый новый проект с самого начала.
 
 Инкапсуляция
 
  Сокрытие деталей реализации за интерфейсом объекта предохраняет 
 пользователей класса от необходимости изменять свой программный код.
 
 Организация
 
  Классы предоставляют новые локальные области видимости, которые 
 минимизируют вероятность конфликтов имен. Кроме того, они обеспечивают
 место для естественного размещения программного кода реализации 
 и управления состоянием объекта.
 
 Поддержка
 
  Классы обеспечивают естественное разделение программного кода, 
 что позволяет уменьшить его избыточность. Благодаря организации
 и возможности повторного использования программного кода в случае 
 необходимости бывает достаточно изменить всего одну копию 
 программного кода.
 
 Непротиворечивость
 
  Классы и возможность наследования позволяют реализовать 
 общие интерфейсы и, следовательно, обеспечить единообразие вашего 
 программного кода – такой код легко поддается отладке, выглядит более 
 осмысленно и прост в сопровождении.
 
 Полиморфизм
 
  Это скорее свойство ООП, чем причина его использования, но благодаря 
 поддержке общности программного кода полиморфизм делает код 
 более гибким, расширяет область его применения и, следовательно, 
 увеличивает его шансы на повторное использование.
 
 Другие
 
  И конечно, причина номер один состоит в том, что упоминание о владении 
 приемами ООП увеличивает шанс быть принятым на работу! 
 (Согласен, я привел эту причину в шутку, но если вы собираетесь 
 работать на ниве программирования, для вас очень важно будет иметь 
 знакомство с ООП.)

 И в заключение, не забывайте, что я говорил в начале шестой части: 
вы не сможете полностью оценить достоинства ООП, пока не будете 
использовать его какое-то время. Выберите себе проект, изучите большие 
примеры, поработайте над упражнениями – это заставит вас попотеть 
над объектно-ориентированным программным кодом, но оно стоит того.
"""