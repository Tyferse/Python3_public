"""
 Инструкция raise

 Чтобы явно возбудить исключение, можно использовать инструкцию raise.
В общем виде она имеет очень простую форму записи – инструкция raise
состоит из слова raise, за которым может следовать имя класса
или экземпляра возбуждаемого исключения:

raise <instance>     # Возбуждает экземпляр класса-исключения
raise <class>        # Создает и возбуждает экземпляр класса-исключения
raise                # Повторно возбуждает самое последнее исключение

 Как уже упоминалось ранее, исключение в Python 2.6 и 3.0 – это всегда э
кземпляр класса. Следовательно, первая форма инструкции raise является
наиболее типичной – ей непосредственно передается экземпляр класса,
который создается перед вызовом инструкции raise или внутри нее.
Если инструкции передается класс, интерпретатор вызовет конструктор
класса без аргументов, а полученный экземпляр передаст инструкции raise
– если после имени класса добавить круглые скобки, мы получим
эквивалентную форму. Третья форма инструкции raise просто повторно
возбуждает текущее исключение – это удобно, когда возникает
необходимость передать перехваченное исключение другому обработчику.

 Чтобы лучше понять вышесказанное, рассмотрим несколько примеров.
Следующие две формы возбуждения встроенных исключений эквивалентны –
они обе возбуждают экземпляр по имени класса, но первая из них создает
экземпляр неявно:

raise IndexError      # Класс (экземпляр создается неявно)
raise IndexError()    # Экземпляр (создается в инструкции)

 Мы также можем создать экземпляр заранее – инструкция raise принимает
ссылки на объекты любых типов, поэтому следующие два примера точно так
же возбуждают исключение IndexError, как и предыдущие:

exc = IndexError() # Экземпляр создается заранее
raise exc

excs = [IndexError, TypeError]
raise excs[0]

 При возбуждении исключения интерпретатор отправляет возбужденный
экземпляр вместе с исключением. Если инструкция try включает предложение
вида except name as X:, переменной X будет присвоен экземпляр,
переданный инструкции raise:

try:
    ...
except IndexError as X:  # Переменной X будет присвоен экземпляр
    ...                    исключения

 Ключевое слово as является необязательным в обработчиках инструкции try
(если оно опущено, интерпретатор просто не будет присваивать экземпляр
переменной), но с его помощью можно получить доступ к данным экземпляра
и методам класса исключения.

 Точно так же действуют и исключения, определяемые пользователем в виде
классов. Ниже приводится пример передачи аргумента конструктору класса
исключения, значение которого становится доступным в обработчике
через экземпляр, присвоенный переменной:

class MyExc(Exception): pass
...
raise MyExc(‘spam’)  # Вызов конструктора класса с аргументом
...
try:
    ...
except MyExc as X:   # Атрибуты экземпляра доступны в обработчике
    print(X.args)

 Однако это описание пересекается с темой следующей главы, поэтому
я пока отложу описание дополнительных подробностей.

 Независимо от того, какие исключения будут использованы, они всегда
идентифицируются обычными объектами и только одно исключение может быть
активным в каждый конкретный момент времени. Как только исключение
перехватывается предложением except, находящимся в любом месте
программы, исключение деактивируется (то есть оно не будет передано
другой инструкции try), если не будет повторно возбуждено при помощи
инструкции raise или в результате ошибки.


 Пример: возбуждение и обработка собственных исключений

 Программы на языке Python с помощью инструкции raise могут возбуждать
как встроенные, так и собственные исключения. В настоящее время
собственные исключения в программе должны быть представлены объектами
экземпляров классов, как, например, MyBad в следующем примере:


class MyBad: pass


def stuff():
    raise MyBad()  # Возбудить исключение вручную


try:
    stuff()  # Возбуждает исключение
except MyBad:
    print('got it')  # Здесь выполняется обработка исключения
# С этого места продолжается выполнение программы

 На этот раз исключение происходит внутри функции, но в действительности
это не имеет никакого значения – управление немедленно передается блоку
except. Обратите внимание, что инструкция try перехватывает собственные
исключения программы точно так же, как и встроенные исключения.


 Пример: повторное возбуждение исключений с помощью инструкции raise

 Инструкция raise, в которой отсутствует имя исключения
или дополнительные данные, просто повторно возбуждает текущее
исключение. В таком виде она обычно используется, когда необходимо
перехватить и обработать исключение, но при этом не требуется
деактивировать исключение:

\>>> try:
...     raise IndexError(‘spam’)  # Исключения сохраняют аргументы
... except IndexError:
...     print(‘propagating’)
...     raise  # Повторное возбуждение последнего исключения
...
propagating
Traceback (most recent call last):
  File “<stdin>”, line 2, in <module>
IndexError: spam

 При таком использовании инструкция raise повторно возбуждает
исключение, которое затем передается обработчику более высокого уровня
(или обработчику по умолчанию, который останавливает выполнение
программы и выводит стандартное сообщение об ошибке). Обратите внимание,
как отображается значение аргумента в тексте сообщения об ошибке,
который был передан конструктору класса, – почему это происходит,
вы узнаете в следующей главе.


 Изменения в Python 3.0: raise from

 В Python 3.0 (но не в 2.6) инструкция raise может также включать
дополнительное предложение from:

raise exception from otherexception

 При использовании предложения from второе выражение определяет еще один
класс исключения или экземпляр, который будет присвоен атрибуту
__cause__ возбуждаемого исключения. Если возбужденное исключение
не будет перехвачено, интерпретатор выведет информацию об обоих
исключениях:

\>>> try:
...     1 / 0
... except Exception as E:
...     raise TypeError(‘Bad!’) from E
...
Traceback (most recent call last):
  File “<stdin>”, line 2, in <module>
ZeroDivisionError: int division or modulo by zero

The above exception was the direct cause of the following exception:
(Исключение выше стало прямой причиной следующего исключения:)

Traceback (most recent call last):
  File “<stdin>”, line 4, in <module>
TypeError: Bad!

 Когда исключение возбуждается в обработчике исключения, подобная
процедура выполняется неявно: предыдущее исключение присваивается
атрибуту __context__ нового исключения и также выводится в стандартный
поток ошибок, если исключение не будет перехвачено. Это достаточно
сложное и малопонятное расширение языка, поэтому за дополнительной
информацией обращайтесь к руководствам по языку Python.


 Инструкция assert

 Язык Python включает инструкцию assert в качестве особого случая
возбуждения исключений на этапе отладки. Это сокращенная форма типичного
шаблона использования инструкции raise, которая представляет собой
условную инструкцию raise. Инструкция вида:

assert <test>, <data>  # Часть <data> является необязательной

 представляет собой эквивалент следующего фрагмента:

if __debug__:
    if not <test>:
        raise AssertionError(<data>)

 Другими словами, если условное выражение возвращает ложное значение,
интерпретатор возбуждает исключение: элемент данных (если присутствует)
играет роль аргумента конструктора исключения. Как и все исключения,
исключение AssertionError приводит к завершению программы, если не будет
перехвачено инструкцией try, и в этом случае элемент данных отображается
как часть сообщения об ошибке.

 Существует дополнительная возможность удалить все инструкции assert из
скомпилированного байт-кода программы за счет использования флага
командной строки -O при запуске интерпретатора и тем самым
оптимизировать программу. Исключение AssertionError является встроенным
исключением, а имя __debug__ – встроенным флагом, который автоматически
получает значение True (истина), когда не используется флаг -O.
Используйте команду вида python –O main.py, чтобы запустить программу
в оптимизированном режиме и отключить все инструкции assert.


 Пример: проверка соблюдения ограничений (но не ошибок)

 Обычно инструкция assert используется для проверки условий выполнения
программы во время разработки. При отображении в текст сообщений
об ошибках, полученных в результате выполнения инструкции assert,
автоматически включается информация из строки исходного программного
кода и значения, перечисленные в инструкции. Рассмотрим файл
asserter.py:

def f(x):
    assert x < 0, ‘x must be negative’
    return x ** 2

% python
\>>> import asserter
\>>> asserter.f(1)
Traceback (most recent call last):
  File “<stdin>”, line 1, in <module>
  File “asserter.py”, line 2, in f
    assert x < 0, ‘x must be negative’
AssertionError: x must be negative

 Важно не забывать, что инструкция assert главным образом предназначена
для проверки соблюдения ограничений, накладываемых программистом,
а не для перехвата настоящих ошибок. Так как интерпретатор Python
в состоянии сам выявлять ошибки во время выполнения программы,
обычно нет необходимости использовать assert для выявления таких
проблем, как выход индекса за допустимые пределы, несоответствие типов
или деление на ноль:

def reciprocal(x):
    assert x != 0  # Бесполезная инструкция assert!
    return 1 / x   # Интерпретатор автоматически проверит
                     на равенство нулю

 Такие инструкции assert являются лишними, потому что встретив ошибку,
интерпретатор автоматически возбудит исключение, и вы вполне можете
положиться в этом на него.1 Еще один пример типичного использования
инструкции assert приводится в примере абстрактного супер-класса
в главе 28 – там инструкция assert использовалась для того, чтобы вызов
неопределенных методов приводил к исключению с определенным текстом
сообщения.


 Контекстные менеджеры with/as

 В версии Python 2.6 и 3.0 появилась новая инструкция, имеющая отношение
к исключениям – with, с необязательным предложением as. Эта инструкция
предназначена для работы с объектами контекстных менеджеров, которые
поддерживают новый протокол взаимодействия, основанный на использовании
методов. Данная особенность доступна также в Python 2.5 в виде
необязательного расширения, которое можно активировать инструкцией:

from __future__ import with_statement

 В двух словах, инструкция with/as может использоваться как альтернатива
известной идиомы try/finally; подобно этой инструкции она предназначена
для выполнения заключительных операций независимо от того, возникло ли
исключение на этапе выполнения основного действия. Однако, в отличие
от инструкции try/finally, инструкция with поддерживает более богатый
возможностями протокол, позволяющий определять как предварительные,
так и заключительные действия для заданного блока программного кода.

 Язык Python дополняет некоторые встроенные средства контекстными
менеджерами, например файлы, которые закрываются автоматически,
или блокировки потоков выполнения, которые автоматически запираются
и отпираются. Однако программист также может создавать с классами
и свои контекстные менеджеры.


 Основы использования

 Основная форма инструкции with выглядит, как показано ниже:

with выражение [as переменная]:
    блок with

 Здесь предполагается, что выражение возвращает объект, поддерживающий
протокол контекстного менеджера (вскоре я расскажу об этом протоколе
подробнее). Этот объект может возвращать значение, которое будет
присвоено переменной, если присутствует необязательное предложение as.

 Обратите внимание, что переменной необязательно будет присвоен
результат выражения – результатом выражения является объект, который
поддерживает контекстный протокол, а переменной может быть присвоено
некоторое другое значение, предназначенное для использования внутри
инструкции. Объект, возвращаемый выражением, может затем выполнять
предварительные действия перед тем, как будет запущен блок with,
а также завершающие действия после того, как этот блок будет выполнен,
независимо от того, было ли возбуждено исключение при его выполнении.

 Некоторые встроенные объекты языка Python были дополнены поддержкой
протокола управления контекстом и потому могут использоваться
в инструкции with. Например, объекты файлов снабжены менеджером
контекста, который автоматически закрывает файл после выполнения блока
with независимо от того, было ли возбуждено исключение при его
выполнении:

with open(r’C:\misc\data’) as myfile:
    for line in myfile:
    print(line)
    ...остальной программный код...

 Здесь вызываемая функция open возвращает объект файла, который
присваивается имени myfile. Применительно к переменной myfile мы можем
использовать обычные средства, предназначенные для работы с файлами, –
в данном случае с помощью итератора выполняется чтение строки за строкой
в цикле for. Однако данный объект поддерживает протокол управления
контекстом, используемый инструкцией with. После того как инструкция
with начнет выполнение, механизм управления контекстом гарантирует,
что объект файла, на который ссылается переменная myfile, будет закрыт
автоматически, даже если в цикле for во время обработки файла произойдет
исключение.

 Объекты файлов закрываются автоматически в момент их утилизации
сборщиком мусора, однако нет никакой возможности узнать заранее,
когда это произойдет. Инструкция with, используемая в таком качестве,
представляет альтернативное решение, позволяющее гарантировать, что файл
будет закрыт сразу после выполнения определенного блока программного
кода. Как мы уже видели выше, аналогичного эффекта можно добиться
с помощью более универсальной и более явной инструкции try/finally,
но в данном случае для этого потребуется написать четыре строки
программного кода вместо одного:

myfile = open(r’C:\misc\data’)
try:
    for line in myfile:
        print(line)
        ...остальной программный код...
finally:
    myfile.close()

 Мы не будем рассматривать в этой книге многопоточную модель выполнения
в языке Python (за дополнительной информацией по этой теме вам следует
обращаться к книгам, посвященным прикладному программированию, таким как
«Программирование на Python»), но блокировка и средства синхронизации
посредством условных переменных также поддерживаются инструкцией
with за счет обеспечения поддержки протокола управления контекстом:

lock = threading.Lock()
with lock:
    # Критическая секция программного кода
    ...доступ к совместно используемым ресурсам...

 Здесь механизм управления контекстом гарантирует, что блокировка
автоматически будет приобретена до того, как начнет выполняться блок,
и освобождена по завершении работы блока независимо от того, было ли
возбуждено исключение при его выполнении.

 Модуль decimal, представленный в главе 5, также использует менеджеры
контекста для упрощения сохранения и восстановления текущего контекста
вычислений, определяющего параметры точности и округления, используемые
в вычислениях:

with decimal.localcontext() as ctx:
    ctx.prec = 2
    x = decimal.Decimal(‘1.00’) / decimal.Decimal(‘3.00’)

 После выполнения этой инструкции менеджер локального контекста текущего
потока выполнения автоматически восстановит его в прежнее состояние,
предшествовавшее началу выполнения инструкции. Чтобы реализовать то же
самое с помощью инструкции try/finally, нам потребовалось бы
предварительно сохранить контекст, а затем восстановить его вручную.


 Протокол управления контекстом

 Некоторые встроенные типы данных уже содержат реализацию менеджеров
контекста, однако точно так же мы можем сами добавлять менеджеры
контекста в свои собственные классы. Для реализации менеджеров контекста
используются специальные методы классов, которые относятся к категории
методов перегрузки операторов и обеспечивают взаимодействие
с инструкцией with. Интерфейс, который должны реализовать объекты
для использования совместно с инструкцией with, достаточно сложен,
хотя большинству программистов достаточно лишь знать, как используются
существующие контексты менеджеров. Однако разработчикам программных
инструментов может потребоваться знание правил создания новых
менеджеров, поэтому коротко рассмотрим основные принципы.

 Ниже описывается, как в действительности работает инструкция with:

 1. Производится вычисление выражения, возвращающего объект, известный
как менеджер контекста, который должен иметь методы __enter__
и __exit__.

 2. Вызывается метод __enter__ менеджера контекста. Возвращаемое
значение метода присваивается переменной в предложении as, если оно
имеется, в противном случае значение просто уничтожается.

 3. Затем выполняется блок программного кода, вложенный
в инструкцию with.

 4. Если при выполнении блока возбуждается исключение, вызывается метод
__exit__(тип, значение, диагностическая_информация), которому передается
подробная информация об исключении. Обратите внимание, что это те же
самые значения, которые возвращает функция sys.exec_info, описываемая
в руководстве по языку Python и далее в этой книге. Если этот метод
возвращает ложное значение, исключение возбуждается повторно,
в противном случае исключение деактивируется. Обычно исключение следует
возбуждать повторно, чтобы оно могло выйти за пределы инструкции with.

 5. Если в блоке with исключение не возникает, метод __exit__ все равно
вызывается, но в аргументах тип, значение и диагностическая_информация
ему передается значение None.

 Рассмотрим небольшой пример, демонстрирующий работу протокола.
Следующий фрагмент определяет объект менеджера контекста, который
сообщает о входе и выходе из блока программного кода любой инструкции
with, с которой он используется:
"""


class TraceBlock:
    def message(self, arg):
        print('running', arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception!', exc_type)
            
        return False  # повторное возбуждение


with TraceBlock() as action:
    action.message(['test 1'])
    print('reached')

with TraceBlock() as action:
    action.message('test 2')
    # raise TypeError
    print('not reached')

"""
 Обратите внимание, что метод __exit__ должен возвращать False, 
чтобы разрешить дальнейшее распространение исключения – отсутствие
инструкции return обеспечивает тот же самый эффект, потому что в этом 
случае по умолчанию возвращается значение None, которое по определению
является ложным. Кроме того, следует заметить, что метод __enter__ 
возвращает сам объект self, который присваивается переменной 
в предложении as; при желании этот метод может возвращать совершенно
другой объект.

 При запуске этого фрагмента менеджер контекста с помощью своих методов 
__enter__ и __exit__ отмечает моменты входа и выхода из блока инструкции 
with. Ниже демонстрируется работа этого сценария под управлением 
Python 3.0 (он также будет работать под управлением Python 2.6, 
но в выводе появятся дополнительные круглые скобки):

% python withas.py
starting with block
running test 1
reached
exited normally

starting with block
running test 2
raise an exception! <class ‘TypeError’>
Traceback (most recent call last):
  File “withas.py”, line 20, in <module>
    raise TypeError
TypeError

 Менеджеры контекста являются новейшими механизмами, предназначенными 
для разработчиков инструментальных средств, поэтому мы не будем 
рассматривать здесь дополнительные подробности (за полной информацией 
обращайтесь к стандартным руководствам по языку; например, новый
стандартный модуль contextlib содержит дополнительные средства, которые 
могут использоваться при создании менеджеров контекстов). 
В более простых случаях инструкция try/finally обеспечивает достаточную
поддержку для выполнения завершающих действий.

 В грядущей версии Python 3.1 в инструкции with можно будет также 
определять сразу несколько (иногда их называют «вложенными») менеджеров 
контекста через запятую. В следующем фрагменте, например при выходе 
из блока инструкции with автоматически выполняются заключительные 
операции для обоих файлов независимо от наличия исключений:
"""

with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)

"""
 В одной инструкции with может быть перечислено любое количество
менеджеров контекста, которые будут действовать как вложенные инструкции
with. Вообще говоря, реализация в версии 3.1 (и выше):

with A() as a, B() as b:
    ...инструкции...
    
 эквивалентна следующей реализации, которая будет работать в 3.1, 3.0 
и 2.6:

with A() as a:
    with B() as b:
        ...инструкции...
        
 Дополнительные подробности вы найдете в примечаниях к выпуску 
Python 3.1.
"""
