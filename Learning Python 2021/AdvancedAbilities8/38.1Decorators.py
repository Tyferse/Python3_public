"""
 Что такое декоратор?

 Декорирование – это способ управления функциями и классами.
Сами декораторы имеют форму вызываемых объектов (таких, как функции),
которые обрабатывают другие вызываемые объекты. Как мы видели ранее
в этой книге, декораторы в языке Python имеют две родственные
разновидности:

  Декораторы функций связывают имя функции с другим вызываемым объектом
 на этапе определения функции, добавляя дополнительный уровень
 логики, которая управляет функциями и методами или выполняет некоторые
 действия в случае их вызова.

  Декораторы классов связывают имя класса с другим вызываемым объектом
 на этапе его определения, добавляя дополнительный уровень логики,
 которая управляет классами или экземплярами, созданными при обращении
 к этим классам.

 В двух словах, декораторы предоставляют возможность в конце инструкции
def определения функции в случае декораторов функций или в конце
инструкции class определения класса в случае декораторов классов
добавить автоматически вызываемый программный код. Этот программный код
может служить самым разным целям, как описывается в следующих разделах.


 Управление вызовами и экземплярами

 Например, в типичном случае, автоматически запускаемый программный код
может использоваться для выполнения дополнительных операций при вызове
функций и классов. Для достижения этой цели устанавливается
объект-обертка, который вызывается позднее:

  Декораторы функций устанавливают объекты-обертки, перехватывающие
 вызовы функций и выполняющие необходимые операции.

  Декораторы классов устанавливают объекты-обертки, перехватывающие
 попытки создания экземпляров и выполняющие необходимые операции.

 Этот эффект достигается декораторами автоматически, за счет
автоматического связывания имен функций и классов с другими вызываемыми
объектами в конце инструкций def и class. При последующих вызовах
эти вызываемые объекты могут выполнять самые разные операции, такие как
трассировка и хронометраж вызовов функций, управление доступом
к атрибутам экземпляров классов и так далее.


 Управление функциями и классами

 В большей части примеров этой главы будут демонстрироваться обертки,
перехватывающие вызовы функций, и операции создания экземпляров классов,
но это не все, что могут делать декораторы:

  Декораторы функций могут также управлять не только вызовами функций,
 но и самими объектами функций, например регистрировать функции
 в некотором прикладном интерфейсе. Однако основное наше внимание будет
 уделяться здесь наиболее типичному применению декораторов – управлению
 вызовами.

  Декораторы классов могут также использоваться не только для управления
 вызовами классов с целью создания экземпляров, но и самими объектами
 классов, например, добавлять новые методы в классы. Поскольку
 эта область применения декораторов в значительной степени пересекается
с областью применения метаклассов (в действительности и декораторы,
 и метаклассы добавляют логику, которая выполняется в конце процедуры
 создания класса), дополнительные примеры такого их использования
 мы увидим в следующей главе.

 Другими словами, декораторы функций могут использоваться для управления
вызовами функций и самими объектами функций, а декораторы классов могут
использоваться для управления процедурой создания экземпляров классов
и самих классов. Возвращая сам декорируемый объект вместо обертки,
декораторы могут служить простым способом выполнения дополнительных
операций после создания функций и классов.


 Определение и использование декораторов

 В зависимости от характера вашей работы, вы можете быть пользователем
декораторов или их разработчиком. Как вы уже видели, в составе Python
поставляется множество встроенных декораторов, которые играют
специализированные роли, – объявление статических методов, создание
свойств и многие другие. Кроме того, многие популярные библиотеки
на языке Python включают декораторы, позволяющие решать такие задачи,
как управление базой данных или логикой работы пользовательского
интерфейса. В подобных случаях мы можем использовать декораторы,
даже не зная, как они реализованы.

 Для решения своих задач программисты могут создавать собственные
декораторы. Например, декораторы функций могут использоваться
для добавления возможности трассировки в другие функции, для проверки
допустимости значений аргументов в процессе отладки, для автоматического
приобретения и освобождения блокировок, для хронометража вызовов функций
в процессе оптимизации и так далее. Выполнение любых операций, которые
по вашему представлению можно было бы добавить в вызовы функций,
можно рассматривать как функциональность, которую можно реализовать
в виде собственного декоратора.

 С другой стороны, декораторы функций предназначены только
для расширения функциональных возможностей отдельных функций
или методов, а не интерфейса объекта в целом. С последней ролью лучше
справляются декораторы классов – благодаря их возможности перехватывать
операции создания экземпляров, они могут использоваться для расширения
или управления интерфейсами объектов. Например, можно создать декораторы
классов, способные отслеживать или проверять все обращения к атрибутам
объекта. Они могут использоваться также для создания прокси-объектов,
классов, допускающих создание единственного экземпляра, и реализации
других распространенных шаблонов проектирования. Фактически,
как вы увидите ниже, многие декораторы классов очень близко напоминают
реализацию шаблона делегирования, который мы рассматривали в главе 30.


 Зачем нужны декораторы?

 Подобно многим другим дополнительным инструментам языка Python
декораторы никогда не становятся единственным возможным средством,
с технической точки зрения: их функциональные возможности часто
могут быть реализованы в виде вспомогательных функций
или с использованием других приемов.

 Но, как бы то ни было, декораторы обеспечивают явный синтаксис
для решения таких задач, а это делает намерения программиста
более очевидными, позволяет уменьшить избыточность программного кода
и может помочь гарантировать корректное использование прикладного
интерфейса:

  Декораторы имеют очень очевидный синтаксис, что делает их
 более заметными, чем вызовы вспомогательных функций, которые могут
 находиться очень далеко от функций и классов, к которым они
 применяются.

  Декораторы применяются к функции или классу только один раз, когда
 они определяются, – нет никакой необходимости добавлять дополнительный
 программный код (который может изменяться со временем) при каждом
 вызове класса или функции.

  Благодаря двум предыдущим особенностям снижается вероятность, что
 пользователь забудет дополнить функцию или класс декоратором согласно
 требованиям прикладного интерфейса.

 Другими словами, кроме технической модели, декораторы предлагают ряд
дополнительных преимуществ, с точки зрения простоты сопровождения
программного кода и его удобочитаемости. Кроме того,
как структурированные инструменты декораторы естественным образом
способствуют инкапсуляции программного кода, что снижает его
избыточность и упрощает внесение изменений в будущем.

 Однако у декораторов имеются и недостатки – при добавлении обертывающей
логики они могут изменять типы декорируемых объектов и выполнять
дополнительные вызовы функций. С другой стороны, все это справедливо
для любого приема, связанного с добавлением к объектам обертывающей
логики. Мы исследуем эти «за» и «против» на практичных примерах далее
в этой главе. Принятие решения об использовании декораторов во многом
зависит от личных предпочтений, тем не менее, благодаря своим
преимуществам они получают все более широкое применение в мире Python.


 Основы

 Начнем рассмотрение декораторов с точки зрения синтаксиса. Вскоре
мы напишем первый действующий программный код, но так как основное
волшебство декораторов сводится к автоматической операции повторного
присваивания, для начала важно понять, как это происходит.


 Декораторы функций

 Декораторы функций впервые появились в Python2.5. Как мы уже видели
ранее в этой книге, они в значительной степени являются всего лишь
синтаксическим подсластителем – конструкцией, которая передает одну
функцию в вызов другой в конце инструкции def и присваивает результат
оригинальному имени первой функции.


 Порядок использования

 Декораторы функций являются своего рода объявлениями времени выполнения
для функций, определения которых следуют за декораторами. Декоратор
указывается в отдельной строке непосредственно перед инструкцией def,
определяющей функцию или метод, и состоит из символа @, за которым
следует имя метафункции – функции (или другого вызываемого объекта),
управляющей другой функцией.

 С точки зрения программирования, декоратор функции автоматически
отображает следующую конструкцию:

@decorator # Декорирование функции
def F(arg):
...
F(99) # Вызов функции

 в эквивалентную ей форму, где decorator – это вызываемый объект,
принимающий единственный аргумент и возвращающий вызываемый объект,
который принимает тот же набор аргументов, что и оригинальная функция F:

def F(arg):
...
F = decorator(F) # Присваивает имени функции результат вызова декоратора
F(99) # Фактически вызывается decorator(F)(99)

 Такое автоматическое повторное присваивание имени оригинальной функции
может применяться к любым инструкциям def, будь то определение обычной
функции или определение метода внутри инструкции class. Когда позднее
производится вызов функции F, фактически вызывается объект, возвращаемый
декоратором, который может быть или другим объектом, реализующим
необходимую логику, обертывающую логику оригинальной функции, или самой
оригинальной функцией.

 Другими словами, декорирование по сути заключается в отображении
первого вызова из следующих ниже во второй (при том, что декоратор
в действительности вызывается только один раз – на этапе декорирования):

func(6, 7)
decorator(func)(6, 7)

 Такое автоматическое повторное связывание имени объясняет синтаксис
объявления статических методов и свойств, который мы видели ранее
в книге:


class C:
    @staticmethod
    def meth(...): ... # meth = staticmethod(meth)


class C:
    @property
    def name(self): ... # name = property(name)


 В обоих случаях в конце инструкции def имени метода присваивается
результат вызова встроенного декоратора. Вызов оригинального имени
позднее приведет к вызову объекта, который вернул декоратор.


 Реализация

 Декоратор сам по себе является вызываемым объектом, который возвращает
вызываемый объект. То есть он возвращает объект, который
будет вызываться при вызове декорируемой функции по ее оригинальному
имени, – это может быть объект-обертка, перехватывающий вызовы
оригинальной функции, или сама оригинальная функция, дополненная новыми
возможностями. Фактически декораторы могут быть вызываемыми объектами
любого типа и могут возвращать вызываемые объекты любого типа: могут
использоваться любые комбинации функций и классов, однако некоторые
из таких комбинаций лучше подходят только для решения определенного
 круга задач.

 Например, чтобы понять, как действует протокол декорирования,
позволяющий организовать управление функциями сразу после их создания,
можно создать декоратор, имеющий следующий вид:

def decorator(F):
    # Обработка функции F
    return F

@decorator
def func(): ... # func = decorator(func)

 Поскольку имени функции опять присваивается оригинальная функция, этот
декоратор просто выполняет некоторые действия после определения функции.
Такие декораторы могут использоваться для регистрации функций
в прикладном интерфейсе, для присоединения атрибутов к функциям
и тому подобного. В более типичном случае, чтобы добавить некоторую
логику, которая перехватывает вызов функции, мы могли бы реализовать
декоратор, возвращающий другой объект, отличный от оригинальной функции:

def decorator(F):
    # Сохраняет или использует функцию F
    # Возвращает другой вызываемый объект:
    # вложенная инструкция def, class с методом __call__ и так далее.

@decorator
def func(): ... # func = decorator(func)

 Этот декоратор вызывается на этапе декорирования, а возвращаемый им
вызываемый объект будет вызываться позднее, при обращении
к оригинальному имени функции. Сам декоратор принимает декорируемую
функцию – возвращаемый им вызываемый объект принимает любые аргументы,
которые только могут передаваться оригинальной функции. То же самое
происходит и при декорировании методов классов: подразумеваемый объект
экземпляра является всего лишь первым аргументом возвращаемого
вызываемого объекта. Ниже приводится типичный шаблон построения
декоратора, демонстрирующий эту идею, – декоратор возвращает обертку,
которая сохраняет оригинальную функцию в области видимости объемлющей
функции:

def decorator(F): # На этапе декорирования @
    def wrapper(*args): # Обертывающая функция
        # Использование F и аргументов
        # F(*args) – вызов оригинальной функции

    return wrapper

@decorator # func = decorator(func)
def func(x, y): # func передается декоратору в аргументе F
...
func(6, 7) # 6, 7 передаются функции wrapper в виде *args

 Когда позднее в программе будет встречен вызов функции func,
в действительности будет вызвана функция wrapper, возвращаемая
декоратором; функция wrapper в свою очередь может вызвать оригинальную
функцию func, которая остается доступной ей в области видимости
объемлющей функции. При таком подходе для каждой декорированной функции
создается новая область видимости, в которой сохраняется информация
о состоянии. Чтобы реализовать то же с помощью классов, мы можем
реализовать метод перегрузки операции вызова и вместо области видимости
объемлющей функции использовать атрибуты экземпляра:


class decorator:
    def __init__(self, func): # На этапе декорирования @
        self.func = func

    def __call__(self, *args): # Обертка вызова функции
        # Использование self.func и аргументов
        # self.func(*args) – вызов оригинальной функции


@decorator
def func(x, y): # func = decorator(func)
... # func будет передана методу __init__

func(6, 7) # 6, 7 передаются методу __call__ в виде *args

 Когда позднее в программе будет встречен вызов функции func,
в действительности будет вызван метод __call__ перегрузки операторов
экземпляра, созданного декоратором; метод __call__, в свою очередь,
может вызвать оригинальную функцию func, которая доступна ему в виде
атрибута экземпляра. При таком подходе для каждой декорированной функции
создается новый экземпляр, хранящий информацию о состоянии в своих
атрибутах.


 Поддержка декорирования методов

 Здесь следует сделать одно важное замечание, касающееся предыдущего
примера декоратора на основе класса: такой декоратор можно использовать
для перехвата вызовов простых функций, но он вообще непригоден
для декорирования методов классов:


class decorator:
    def __init__(self, func): # func – это метод, не связанный
        self.func = func # с экземпляром
    def __call__(self, *args): # self – это экземпляр декоратора
        # вызов self.func(*args) потерпит неудачу!
        # Экземпляр C отсутствует в args!


class C:
    @decorator
    def method(self, x, y): # method = decorator(method)
... # то есть имени method присваивается экземпляр
# класса decorator


 При таком подходе имени декорируемого метода присваивается экземпляр
класса decorator, а не функция.

 Проблема, собственно, состоит в том, что позднее, при вызове метода
method, в аргументе self методу __call__ декоратора будет передан
экземпляр класса decorator, а экземпляр класса C не будет включен
в список аргументов *args. Это делает невозможным вызов оригинального
метода – объект декоратора сохраняет оригинальную функцию метода,
но он не может передать ей ссылку на экземпляр.

 Для одновременной поддержки возможности декорирования функций и методов
лучше всего подходит прием, основанный на применении вложенных функций:

def decorator(F): # F – функция или метод, не связанный с экземпляром
    def wrapper(*args): # для методов - экземпляр класса в args[0]
        # F(*args) – вызов функции или метода

    return wrapper

@decorator
def func(x, y): # func = decorator(func)
...
func(6, 7) # В действительности вызовет wrapper(6, 7)


class C:
    @decorator
    def method(self, x, y): # method = decorator(method)
... # Присвоит простую функцию


X = C()
X.method(6, 7) # В действительности вызовет wrapper(X, 6, 7)

 При таком подходе функция wrapper будет принимать экземпляр класса C
в виде первого аргумента, поэтому она сможет вызвать оригинальный метод
и передать всю необходимую информацию.

 С технической точки зрения, работоспособность версии на основе
вложенной функции обусловлена тем, что интерпретатор создает объект
связанного метода и передает подразумеваемый экземпляр класса
в аргументе self, только когда атрибут метода ссылается на простую
функцию. Когда он ссылается на экземпляр вызываемого класса,
в аргументе self ему передается экземпляр вызываемого класса,
чтобы обеспечить доступ к собственным данным. Какое значение это может
иметь на практике, мы увидим в более реалистичных примерах ниже
в этой главе.

 Обратите также внимание, что вложенные функции обеспечивают, пожалуй,
самый простой способ поддержки декорирования функций и методов
одновременно, но он не единственный. Дескрипторы, обсуждавшиеся
в предыдущей главе, например, принимают при вызове сам дескриптор
и подразумеваемый экземпляр класса. Ниже в этой главе мы увидим,
как можно использовать дескрипторы для создания декораторов, хотя такое
решение выглядит более сложным.


 Декораторы классов

 Декораторы функций оказались настолько удобными, что в Python 2.6 и 3.0
эта модель была расширена, чтобы обеспечить возможность декорирования
классов. Декораторы классов тесно связаны с декораторами функций –
фактически они используют тот же самый синтаксис и очень похожий способ
реализации. Вместо того чтобы обертывать отдельные функции или методы,
декораторы классов обеспечивают способ управления классами
или обертывания операции создания экземпляров дополнительной логикой,
управляющей или расширяющей логику создания экземпляров класса.


 Порядок использования

 Синтаксически декораторы классов располагаются непосредственно перед
инструкциями class (так же, как декораторы функций располагаются
непосредственно перед определениями функций). Если исходить из того,
что декоратор – это функция, принимающая единственный аргумент
и возвращающая вызываемый объект, то синтаксис декоратора класса:


@decorator # Декорирование класса
class C:
...
x = C(99) # Создает экземпляр

 эквивалентен следующей конструкции – класс автоматически передается
функции-декоратору, а возвращаемый ею результат присваивается
оригинальному имени класса:


class C:
...
C = decorator(C) # Присваивает имени класса результат,
# возвращаемый декоратором
x = C(99) # Фактически вызовет decorator(C)(99)

 Суть заключается в том, что позднее, при вызове имени класса,
для создания экземпляра вместо оригинального класса будет вызван
вызываемый объект, возвращенный декоратором.


 Реализация

 Для создания декораторов классов используются почти те же приемы,
которые используются при создании декораторов функций. Поскольку
декоратор класса также является вызываемым объектом, который возвращает
вызываемый объект, могут быть сконструированы любые комбинации функций
и классов.

 При таком подходе результат работы декоратора вызывается, когда позднее
в программе производится попытка создать экземпляр класса. Например,
чтобы просто выполнить некоторые операции сразу после создания класса,
нужно вернуть сам оригинальный класс:

def decorator(C):
    # Обработать класс C
    return C


@decorator
class C: ... # C = decorator(C)

 Чтобы добавить уровень обертывающей логики, которая позднее будет
перехватывать попытки создания экземпляров, декоратор должен вернуть
вызываемый объект:

def decorator(C):
    # Сохранить или использовать класс C
    # Возвращает другой вызываемый объект:
    # вложенная инструкция def, class с методом __call__ и так далее.


@decorator
class C: ... # C = decorator(C)


 Вызываемый объект, возвращаемый таким декоратором класса, обычно
создает и возвращает новый экземпляр оригинального класса, изменяя
или дополняя его интерфейс. Например, следующий декоратор, который
добавляет в объект обработку операций обращения к неопределенным
атрибутам:
"""


def decorator(cls):  # На этапе декорирования @

    class Wrapper:
        def __init__(self, *args):  # На этапе создании экземпляра
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            # Вызывается при обращении к атрибуту
            return getattr(self.wrapped, name)
        
    return Wrapper


@decorator
class C:  # C = decorator(C)
    def __init__(self, x, y):  # Вызывается методом Wrapper.__init__
        self.attr = 'spam'


x = C(6, 7)  # В действительности вызовет Wrapper(6, 7)
print(x.attr)  # Вызовет Wrapper.__getattr__, выведет “spam”

"""
 В этом примере декоратор присвоит оригинальному имени класса другой
класс, который сохраняет оригинальный класс в области видимости 
объемлющей функции, создает и встраивает экземпляр оригинального класса
при вызове. Когда позднее будет выполнена попытка прочитать значение 
атрибута экземпляра, она будет перехвачена методом __getattr__ обертки 
и делегирована встроенному экземпляру оригинального класса. Кроме того,
для каждого декорированного класса создается новая область видимости 
объемлющей функции, в которой сохраняется оригинальный класс. 

 Подобно декораторам функций декораторы классов обычно создаются в виде
«фабричных» функций, которые создают и возвращают вызываемые объекты,
классы с методами __init__ или __call__ для перехвата операций вызова 
или их комбинации. Фабричные функции обычно сохраняют информацию 
о состоянии в области видимости объемлющей функции, а классы –
в атрибутах.


 Поддержка множества экземпляров
 
 Как и в случае с декораторами функций, одни комбинации типов вызываемых
объектов лучше подходят для решения определенных задач, чем другие. 
Рассмотрим следующую альтернативную и ошибочную реализацию декоратора из
предыдущего примера:
"""


class Decorator:
    def __init__(self, C):  # На этапе декорирования @
        self.C = C

    def __call__(self, *args):  # На этапе создания экземпляра
        self.wrapped = self.C(*args)
        return self

    def __getattr__(self, attrname):
        # Вызывается при обращении к атрибуту
        return getattr(self.wrapped, attrname)


"""
@Decorator
class C: ... # C = Decorator(C)
x = C()
y = C() # Затрет x!

 Эта версия может использоваться для декорирования множества классов 
(для каждого из них будет создан новый экземпляр класса Decorator) 
и будет перехватывать попытки создания экземпляров (каждый раз будет 
вызываться метод __call__). Однако в отличие от предыдущей версии, 
данная версия не поддерживает работу с множеством экземпляров одного 
класса – операция создания очередного экземпляра будет затирать 
предыдущий экземпляр. Первоначальная версия поддерживает возможность 
создания множества экземпляров, потому что при создании каждого 
экземпляра создается новый, независимый объект-обертка. В более общем 
смысле, любой из следующих вариантов поддерживает возможность создания 
множества обернутых экземпляров:
"""


def decorator(C):  # На этапе декорирования @
    class Wrapper:
        def __init__(self, *args):  # Вызывается при создании экземпляра
            self.wrapped = C(*args)
            
    return Wrapper


class Wrapper:
    def __init__(self, *args):  # Вызывается при создании экземпляра
        self.wrapped = C(*args)


def decorator(C):  # На этапе декорирования @
    def onCall(*args):  # На этапе создания экземпляра
        return Wrapper(C(*args))  # Встраивает экземпляр в экземпляр
    
    return onCall


"""
Мы изучим это явление на более реалистичном примере ниже в этой главе –
однако на практике необходимо проявлять осторожность
и выбирать комбинации типов вызываемых объектов,
которые лучше соответствуют нашим намерениям.


 Вложение декораторов
 
 Иногда одного декоратора бывает недостаточно. Для поддержки 
многоступенчатых расширений синтаксис декораторов позволяет добавлять 
несколько уровней обертывающей логики к декорируемой функции или методу.
При использовании такой возможности каждый декоратор должен указываться
в отдельной строке. Синтаксическая конструкция следующего вида:

@A
@B
@C
def f(...):
...

 равноценна следующей:
 
def f(...):
...
f = A(B(C(f)))

 Здесь оригинальная функция передается трем различным декораторам, 
а получившийся в результате вызываемый объект присваивается 
оригинальному имени. Каждый декоратор обрабатывает результат, 
возвращаемый предыдущим декоратором, который может быть оригинальной 
функцией или объектом-оберткой.

 Если все декораторы возвращают обертки, то при вызове функции 
по оригинальному имени будет выполнена логика всех трех обертывающих
объектов, расширяя возможности функции тремя различными способами. 
Последний декоратор в списке будет задействован первым и окажется 
самым глубоко вложенным.

 Так же как и в случае декорирования функций, применение нескольких 
декораторов классов приведет к вызову нескольких вложенных функций и,
возможно, к созданию нескольких уровней обертывающей логики вокруг 
операции создания экземпляров. Например, следующий фрагмент:


@spam
@eggs
class C:
...
X = C()

 эквивалентен следующему:
 
 
class C:
...
C = spam(eggs(C))
X = C()

 Как и прежде, каждый декоратор может возвращать оригинальный класс или
объект-обертку. Если оба декоратора в примере возвращают обертки, 
то позднее, когда будет предпринята попытка создать экземпляр 
оригинального класса C, вызов будет направлен обертывающим объектам, 
созданным обоими декораторами, spam и eggs, которые могут преследовать 
совершенно разные цели. Например, следующие декораторы просто возвращают 
декорируемую функцию, не выполняя никаких дополнительных действий:
"""


def d1(F):
    return F


def d2(F):
    return F


def d3(F):
    return F


@d1
@d2
@d3
def func():  # func = d1(d2(d3(func)))
    print('spam')


func()  # Выведет “spam”

"""
 При применении аналогичных ничего не делающих декораторов к классам 
результат будет похожим.

 Однако когда декораторы добавляют обертывающие объекты функций, они
могут расширять возможности оригинальных функций – в следующем примере 
происходит объединение результатов в ходе выполнения уровней 
обертывающей логики декораторов от внутренней к внешней:
"""


def d1(F):
    return lambda: 'X' + F()


def d2(F):
    return lambda: 'Y' + F()


def d3(F):
    return lambda: 'Z' + F()


@d1
@d2
@d3
def func():  # func = d1(d2(d3(func)))
    return 'spam'


print(func())  # Выведет “XYZspam”

"""
 Аргументы декораторов
 
 Обе разновидности декораторов, декораторы функций и декораторы классов,
могут принимать дополнительные аргументы, хотя в действительности эти
аргументы передаются вызываемому объекту, возвращающему декоратор,
который в свою очередь возвращает вызываемый объект. Например, следующий
программный код:

@decorator(A, B)
def F(arg):
...
F(99)

 автоматически будет преобразован в эквивалентную форму, где decorator –
это вызываемый объект, возвращающий фактический декоратор. Возвращаемый
фактический декоратор, в свою очередь, возвращает вызываемый объект,
который позднее будет использоваться для перехвата вызовов оригинальной
функции:

def F(arg):
...
F = decorator(A, B)(F)  # Присваивает имени F результат вызова объекта,
# возвращаемого вызываемым объектом decorator
F(99) # Фактически вызывается decorator(A, B)(F)(99)

 Аргументы декораторов интерпретируются еще до того как будет выполнена
операция декорирования, и обычно в них передаются значения 
для использования в последующих вызовах. В подобных случаях функция 
decorator, например, может иметь такой вид:

def decorator(A, B):
    # Сохранить или использовать A, B
    def actualDecorator(F):
        # Сохранить или использовать функцию F
        # Возвращает другой вызываемый объект:
        # вложенная инструкция def, class с методом __call__ 
        # и так далее.
        return callable
    return actualDecorator
    
 При такой организации внешняя функция обычно сохраняет аргументы 
декоратора вместе с другой информацией о состоянии для последующего 
использования внутри фактического декоратора – вызываемого объекта, 
возвращаемого функцией. Этот фрагмент сохраняет аргументы в области 
видимости объемлющей функции, но для этих целей можно также использовать 
атрибуты классов.

 Другими словами, аргументы декораторов часто подразумевают три уровня
вызываемых объектов: вызываемый объект, принимающий аргументы
декоратора, возвращает вызываемый объект, который будет играть роль 
декоратора, который в свою очередь возвращает вызываемый объект 
для обработки вызовов оригинальной функции или класса. Каждый из этих 
трех уровней может быть функцией или классом и может сохранять 
информацию в области видимости объемлющей функции или 
в атрибутах класса.

 
 Декораторы могут управлять функциями и классами одновременно

 В оставшейся части главы основное наше внимание будет уделяться 
обертыванию вызовов функций и классов, тем не менее, я должен заметить, 
что механизм декораторов обладает более широкими возможностями – 
это протокол передачи функций и классов вызываемым объектам сразу же 
после их создания. Таким образом, декораторы могут использоваться 
для выполнения произвольных операций сразу после создания декорируемых 
объектов:

def decorate(O):
    # Сохраняет или дополняет функцию или класс O
    return O
    
@decorator
def F(): ... # F = decorator(F)


@decorator
class C: ... # C = decorator(C)


 Если декоратор возвращает не обертку, а оригинальный декорируемый
объект, как показано выше, он может использоваться для управления 
самими функциями и классами.
"""