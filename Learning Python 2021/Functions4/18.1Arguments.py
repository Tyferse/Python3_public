"""
 Аргументы


 Передача аргументов

 Раньше уже говорилось, что передача аргументов производится посредством
операции присваивания. Здесь имеется несколько моментов, не всегда
очевидных для начинающих, о которых будет говориться в этом разделе.
Ниже приводится несколько важных замечаний, касающихся передачи
аргументов в функции:

  Аргументы передаются через автоматическое присваивание объектов
 локальным переменным. Аргументы функции – ссылки на объекты, которые
 (возможно) используются совместно с вызывающей программой, –
 это всего лишь результат еще одной из разновидностей операции
 присваивания. Ссылки в языке Python реализованы в виде указателей,
 поэтому все аргументы фактически передаются по указателям. Объекты,
 которые передаются в виде аргументов, никогда не копируются
 автоматически.

  Операция присваивания именам аргументов внутри функции не оказывает
 влияния на вызывающую программу. При вызове функции имена аргументов,
 указанные в ее заголовке, становятся новыми локальными именами
 в области видимости функции. Это не является совмещением имен между
 именами аргументов и именами в вызывающей программе.

  Изменение внутри функции аргумента, который является изменяемым
 объектом, может оказывать влияние на вызывающую программу. С другой
 стороны, так как аргументы – это всего лишь результат операции
 присваивания полученных объектов, функции могут воздействовать
 на полученные изменяемые объекты и тем самым оказывать влияние
 на вызывающую программу. Изменяемые объекты могут рассматриваться
 функциями как средство ввода, так и вывода информации.

 За дополнительной информацией о ссылках обращайтесь к главе 6 – все,
что там говорится, вполне применимо и к аргументам функций,
несмотря на то, что присваивание именам аргументов выполняется
автоматически и неявно. Схема передачи аргументов посредством
присваивания, принятая в языке Python, это далеко не то же самое,
что передача аргументов по ссылке в языке C++, но она очень близка
к модели передачи аргументов в языке C:

  Неизменяемые объекты передаются «по значению». Такие объекты,
 как целые числа и строки, передаются в виде ссылок на объекты,
 а не в виде копий объектов, но так как неизменяемые объекты невозможно
 изменить непосредственно, передача таких объектов очень напоминает
 копирование.

  Изменяемые объекты передаются «по указателю». Такие объекты,
 как списки и словари, также передаются в виде ссылок на объекты,
 что очень похоже на то, как в языке C передаются указатели
 на массивы, – изменяемые объекты допускают возможность
 непосредственного изменения внутри функции так же, как и массивы
 в языке C.

 Конечно, если вы никогда ранее не использовали язык C, модель передачи
аргументов в языке Python покажется вам еще проще – согласно этой модели
выполняется присваивание объектов именам аргументов, и она одинаково
работает с любыми объектами, как с изменяемыми, так и с неизменяемыми.


 Аргументы и разделяемые ссылки

 Для иллюстрации особенностей, свойственных механизму передачи
аргументов, рассмотрим следующий пример:

\>>> def f(a):  # Имени a присваивается переданный объект
... a = 99  # Изменяется только локальная переменная
...
\>>> b = 88
\>>> f(b)
# Первоначально имена a и b ссылаются на одно и то же число 88
\>>> print(b)  # Переменная b не изменилась
88

 В этом фрагменте в момент вызова функции f(b) переменной a
присваивается объект 88, но переменная a существует только внутри
вызванной функции. Изменение переменной a внутри функции не оказывает
влияния на окружение, откуда была вызвана функция, – просто в момент
вызова создается совершенно новый объект a.

 Это именно то, что подразумевалось выше под словами «не является
совмещением имен», – операция присваивания значений аргументам внутри
функции (такая, как a=99) не изменяет, как по волшебству, переменные,
подобные переменной b, находящиеся в области видимости программного
кода, вызывающего функцию. Первоначально переменные и аргументы могут
ссылаться на одни и те же объекты (фактически они являются указателями
на эти объекты), но лишь временно, в первые мгновения после вызова.
Как только имени аргумента будет присвоено другое значение,
эта связь исчезнет.

 По крайней мере, это относится к случаю, когда выполняется операция
присваивания значений самим аргументам. Когда в аргументах передаются
изменяемые объекты, такие как списки и словари, мы должны понимать,
что непосредственные изменения в таких объектах никуда не исчезнут после
завершения функции и тем самым могут оказывать влияние на вызывающую
программу. Ниже приводится пример, который демонстрирует
эту особенность:

\>>> def changer(a, b):  # В аргументах передаются ссылки на объекты
...     a = 2  # Изменяется только значение локального имени
...     b[0] = ‘spam’  # Изменяется непосредственно разделяемый объект
...
\>>> X = 1
\>>> L = [1, 2]  # Вызывающая программа
\>>> changer(X, L)  # Передаются изменяемый и неизменяемый объекты
\>>> X, L  # Переменная X – не изменилась, L - изменилась
(1, [‘spam’, 2])

 В этом фрагменте функция changer присваивает значения аргументу a
и компоненту объекта, на который ссылается аргумент b. Две операции
присваивания в функции имеют незначительные синтаксические различия,
но дают совершенно разные результаты:

  Так как a – это локальная переменная в области видимости функции,
 первая операция присваивания не имеет эффекта для вызывающей программы
 – она всего лишь изменяет локальную переменную a, записывая
 в нее ссылку на совершенно другой объект, и не изменяет связанное
 с ней имя X в вызывающей программе. Здесь все происходит точно так же,
 как в предыдущем примере.

  b – также локальная переменная, но в ней передается изменяемый объект
 (список, на который ссылается переменная L в вызывающей программе).
 Поскольку вторая операция присваивания воздействует непосредственно
 на изменяемый объект, результат присваивания элементу b[0] в функции
 оказывает влияние на значение имени L после выхода из функции.

 В действительности вторая операция присваивания в функции changer
не изменяет объект b – она изменяет часть объекта, на который ссылается
аргумент b. Это изменение оказывает влияние на вызывающую программу
только потому, что измененный объект продолжает существовать
после завершения функции. Значение переменной L никак не изменилось –
она по-прежнему ссылается на тот же самый, пусть и измененный объект,
но все выглядит так, как будто переменная L изменилась после вызова
функции. Это объясняется тем, что внутри функции был изменен объект,
на который она ссылается.

 Если этот пример все еще кажется вам непонятным, попробуйте представить
себе автоматическое присваивание переданным аргументам,
как последовательность простых инструкций присваивания. Для первого
аргумента операции присваивания не оказывают влияния на вызывающую
программу:

\>>> X = 1
\>>> a = X  # Разделяют один и тот же объект
\>>> a = 2  # Изменяется только ‘a’, значение ‘X’ остается равным 1
\>>> print(X)
1

 Но для второго аргумента операция присваивания сказывается на значении
переменной, участвующей в вызове, так как она производит
непосредственное изменение объекта:

\>>> L = [1, 2]
\>>> b = L  # Разделяют один и тот же объект
\>>> b[0] = ‘spam’  # Изменение в самом объекте: ‘L’ также изменяется
\>>> print(L)
[‘spam’, 2]

 Вспомните обсуждение вопросов совместного использования изменяемых
объектов в главах 6 и 9, и вы узнаете это явление: непосредственное
воздействие на изменяемый объект может сказываться на других ссылках
на этот объект. В данном случае один из параметров функции играет
одновременно роль средства ввода и вывода информации.


 Как избежать воздействий на изменяемые аргументы

 Такое поведение изменяемых объектов не является ошибкой – оно лишь
отражает способ, каким передаются аргументы. В языке Python аргументы
по умолчанию передаются в функции по ссылкам (то есть по указателям),
потому что в большинстве случаев именно это и требуется. Это означает,
что мы можем передавать крупные объекты в любые точки программы
без создания множества копий, и легко изменять эти объекты в процессе
работы. В действительности, как мы увидим в шестой части книги, модель
классов в языке Python в значительной степени опирается на возможность
изменения объектом собственного состояния с помощью аргумента «self».

 Однако если нам требуется избежать влияния непосредственных изменений
объектов, производимых в функциях, на вызывающую программу, мы можем
просто явно копировать изменяемые объекты, как описывалось в главе 6.
В случае с аргументами функций мы всегда можем скопировать список
в точке вызова:

L = [1, 2]
changer(X, L[:])  #  Передается копия, поэтому переменная ‘L’
                  # не изменится

 Можно также создать копию внутри функции, если для нас нежелательно,
чтобы функция изменяла объект, независимо от способа его передачи:

def changer(a, b):
    b = b[:]  # Входной список копируется, что исключает воздействие
              # на вызывающую программу
    a = 2
    b[0] = ‘spam’  # Изменится только копия списка

 Оба варианта копирования не мешают функции изменять объект, они лишь
препятствуют воздействию этих изменений на вызывающую программу. Чтобы
действительно предотвратить изменения, мы всегда можем преобразовать
изменяемые объекты в неизменяемые, что позволит выявить источники
проблем. Например, при попытке изменения кортежа будет возбуждено
исключение:

L = [1, 2]
changer(X, tuple(L))  # Передается кортеж, поэтому попытка изменения
                      # возбудит исключение

 Здесь используется встроенная функция tuple, которая создает новый
кортеж из всех элементов последовательности (в действительности –
любого итерируемого объекта). Это особенно важно, потому что вынуждает
писать функцию так, чтобы она никогда не пыталась изменять передаваемые
ей аргументы. Однако такое решение накладывает на функцию больше
ограничений, чем следует, поэтому его вообще следует избегать
(нельзя знать заранее, когда изменение аргументов окажется необходимым).
Кроме того, при таком подходе функция теряет возможность применять
к аргументу методы списков, включая методы, которые не производят
непосредственных изменений.

 Главное, что следует запомнить, – функции могут оказывать воздействие
на передаваемые им изменяемые объекты, такие как списки и словари. Это
не всегда является проблемой и часто может приносить пользу. Кроме того,
функции, которые изменяют объекты, наверняка проектировались
и предназначались именно для этого – внесение изменений, скорее всего,
является составной частью четко определенного интерфейса, который
не следует портить, создавая копии.

 Однако вам действительно необходимо знать об этой особенности – если
изменения в объектах происходят неожиданно для вас, проверьте вызываемые
функции и в случае необходимости передавайте им копии объектов.


 Имитация выходных параметров

 Мы уже обсудили инструкцию return и использовали ее в нескольких
примерах. Эта инструкция может возвращать объект любого типа, поэтому
с ее помощью можно возвращать сразу несколько значений, упаковав их
в кортеж или в коллекцию любого другого типа. В языке Python фактически
отсутствует такое понятие, которое в некоторых других языках называется
«передача аргументов по ссылке», однако мы можем имитировать
такое поведение, возвращая кортеж и выполняя присваивание результатов
оригинальным именам аргументов в вызывающей программе:

\>>> def multiple(x, y):
...     x = 2  # Изменяется только локальное имя
...     y = [3, 4]
...     return x, y  # Новые значения возвращаются в виде кортежа
...
\>>> X = 1
\>>> L = [1, 2]
\>>> X, L = multiple(X, L)  # Результаты присваиваются именам
\>>> X, L                   # в вызывающей программе
(2, [3, 4])

 Выглядит так, как будто функция возвращает два значения, но на самом
деле – это единственный кортеж, состоящий из двух элементов,
а необязательные окружающие скобки просто опущены. После возврата
из функции можно использовать операцию присваивания кортежа,
чтобы извлечь отдельные элементы. (Если вы забыли, как это работает,
вернитесь к разделу «Кортежи» в главе 4, к главе 9 и к разделу
«Инструкции присваивания» в главе 11.) Такой прием позволяет имитировать
выходные параметры, имеющиеся в других языках программирования, за счет
использования явной операции присваивания. Переменные X и L изменятся
после вызова функции, но только потому, что мы явно это предусмотрели.

 Распаковывание аргументов в Python 2.X: В предыдущем примере
выполняется операция распаковывания кортежа, возвращаемого функцией
и полученного операцией присваивания кортежа. В Python 2.6 существует
возможность автоматического распаковывания кортежей, передаваемых
функциям в виде аргументов. В версии 2.6 функции, объявленной как:

def f((a, (b, c))):

 можно передавать кортежи, соответствующие ожидаемой структуре:
в результате вызова f((1, (2, 3))) переменным a, b и c будут присвоены
значения 1, 2 и 3 соответственно. Естественно, передаваемый кортеж может
быть объектом, созданным перед вызовом (f(T)). Этот синтаксис инструкции
def больше не поддерживается в версии Python 3.0. Теперь подобные
функции должны объявляться так:

def f(T): (a, (b, c)) = T

 А распаковывание должно производиться явной инструкцией присваивания.
Эта явная форма может применяться в обеих версиях, 3.0 и 2.6. Операция
распаковывания аргументов неочевидна и редко используется на практике
в Python 2.X. Кроме того, в заголовке функции, в версии 2.6,
поддерживается только форма передачи кортежей – при попытке использовать
в версии 2.6 более общую форму присваивания последовательностей
(например, def f((a, [b, c])):) будет возбуждено исключение с сообщением
о синтаксической ошибке и требованием использовать явную
форму присваивания.

 Синтаксис распаковывания кортежей в аргументах в версии 3.0 также
был запрещен к использованию в списках аргументов lambda-выражений:
смотрите врезку «Придется держать в уме: генераторы списков и map»,
где приводятся примеры. Несколько нарушая это правило, в версии 3.0
до сих пор сохранилась поддержка операции автоматического распаковывания
кортежей в циклах for – смотрите примеры в главе 13.


 Специальные режимы сопоставления аргументов

 Как только что было показано, в языке Python аргументы всегда
передаются через операцию присваивания – передаваемые объекты
присваиваются именам, указанным в заголовке инструкции def. Однако
на основе этой модели язык Python обеспечивает дополнительные
возможности влиять на способ, которым объекты аргументов сопоставляются
с именами аргументов в заголовке функции. Эти возможности можно
и не использовать, но они позволяют писать функции, поддерживающие более
гибкие схемы вызова, и вы можете встретиться с некоторыми библиотеками,
требующими использования этого способа.

 По умолчанию сопоставление аргументов производится в соответствии
с их позициями, слева направо, и функции должно передаваться столько
аргументов, сколько имен указано в заголовке функции. Но кроме этого
существует возможность явно указывать соответствия между аргументами
и именами, определять значения по умолчанию и передавать дополнительные
аргументы.


 Основы

 Это достаточно сложный раздел, и прежде чем окунуться в обсуждение
синтаксиса, я хотел бы подчеркнуть, что эти специальные режимы
не являются обязательными и имеют отношение только к сопоставлению
объектов и имен – основным механизмом передачи аргументов по-прежнему
остается операция присваивания. Фактически некоторые из этих режимов
предназначены в первую очередь для разработчиков библиотек,
а не для разработчиков приложений. Но так как вы можете столкнуться
с этими режимами, даже не используя их в своих программах,
я коротко опишу их:

 Сопоставление по позиции: значения и имена ставятся в соответствие
по порядку, слева направо

  Обычный случай, который мы использовали до сих пор, значения и имена
 аргументов ставятся в соответствие в порядке их следования слева
 направо.

 Сопоставление по именам: соответствие определяется по указанным именам
аргументов

  Вызывающая программа имеет возможность указать соответствие между
 аргументами функции и их значениями в момент вызова, используя
 синтаксис name=value.

 Значения по умолчанию: указываются значения аргументов, которые
могут не передаваться

  Функции могут определять значения аргументов по умолчанию на тот
 случай, если вызывающая программа передаст недостаточное количество
 значений. Здесь также используется синтаксис name=value.

 Переменное число аргументов: прием произвольного числа аргументов,
позиционных или именованных

  Функции могут использовать специальный аргумент, имени которого
 предшествует один или два символа *, для объединения произвольного
 числа дополнительных аргументов в коллекцию (эта особенность часто
 называется varargs, как в языке C, где также поддерживаются списки
 аргументов переменной длины).

 Переменное число аргументов: передача произвольного числа аргументов,
позиционных или именованных

  Вызывающая программа также может использовать синтаксис с символом *
 для распаковывания коллекции аргументов в отдельные аргументы. В данном
 случае символ * имеет обратный смысл по отношению к символу *
 в заголовке функции – в заголовке он означает коллекцию произвольного
 числа аргументов, тогда как в вызывающей программе – передачу коллекции
 в виде произвольного числа отдельных аргументов.

 Только именованные аргументы: аргументы, которые должны передаваться
только по имени

  В Python 3.0 (но не в 2.6) функции могут определять аргументы, которые
 должны передаваться по именам, то есть в виде именованных,
 а не позиционных аргументов. Такие аргументы обычно используются
 для определения параметров настройки, дополняющих фактические
 аргументы.


 Синтаксис сопоставления

  Синтаксис                  Местоположение   Интерпретация
  func(value)                Вызывающая       Обычный аргумент:
                             программа        сопоставление производится
                                              по позиции

  func(name=value)           Вызывающая       Именованный аргумент:
                             программа        сопоставление производится
                                              по указанному имени

  func(*sequence)            Вызывающая       Все объекты в указанной
                             программа        последовательности
                                              передаются как отдельные
                                              позиционные аргументы

  func(**dict)               Вызывающая       Все пары ключ/значение
                             программа        в указанном словаре
                                              передаются как отдельные
                                              именованные аргументы

  def func(name)             Функция          Обычный аргумент: с
                                              опоставление производится
                                              по позиции или по имени

  def func(name=value)       Функция          Значение аргумента
                                              по умолчанию, на случай,
                                              если аргумент
                                              не передается функции

  def func(*name)            Функция          Определяет и объединяет
                                              все дополнительные
                                              аргументы в кортеж

  def func(**name)           Функция          Определяет и объединяет
                                              все дополнительные
                                              именованные аргументы
                                              в словарь

  def func(*args, name)      Функция          Аргументы, которые должны
  def func(*, name=value)                     передаваться функции
                                              только по именам (3.0)

 Эти специальные режимы сопоставления делятся на случаи вызова функции
и определения функции:

  В инструкции вызова функции (первые четыре строки таблицы)
 при использовании простых значений соответствие именам аргументов
 определяется по позиции, но при использовании формы name=value
 соответствие определяется по именам аргументов – это называется
 передачей именованных аргументов. Использование форм *sequence
 и **dict в вызовах функций позволяет передавать произвольное число
 объектов по позиции или по именам в виде последовательностей
 и словарей соответственно.

  В заголовке функции (остальная часть таблицы) при использовании п
 ростых значений соответствие определяется по позиции или по имени,
 в зависимости от того, как вызывающая программа передает значения,
 но при использовании формы name=value определяются значения
 по умолчанию. При использовании формы *name все дополнительные
 позиционные аргументы объединяются в кортеж, а при использовании формы
 **name все дополнительные именованные аргументы объединяются в словарь.
 В версии Python 3.0 и выше любые обычные аргументы или аргументы
 со значениями по умолчанию, следующие за формой *name или
 за единственным символом *, являются именованными аргументами,
  которые при вызове функции должны передаваться только по имени.

 Наиболее часто в программном коде на языке Python используются форма
передачи именованных аргументов и аргументов со значениями по умолчанию.
Мы уже встречались с обеими формами ранее в книге:

  Мы уже пользовались именованными аргументами для передачи
 необязательных параметров функции print в Python 3.0, но они имеют
 более универсальный характер – именованные аргументы позволяют
 указывать значения аргументов вместе с их именами, чтобы придать вызову
 функции больше смысла.

  Со значениями по умолчанию мы также уже встречались, когда
 рассматривали способы передачи значений из объемлющей области
 видимости, но на самом деле эта форма имеет более широкую область
 применения – она позволяет определять необязательные аргументы
 и указывать значения по умолчанию в определении функции.

 Как мы увидим далее, комбинирование аргументов со значениями
по умолчанию в заголовках функций с именованными аргументами в вызовах
функций дает нам возможность выбирать и переопределять значения,
используемые по умолчанию.

 Специальные режимы сопоставления позволяют обеспечить свободу выбора
числа аргументов, которые должны передаваться функции в обязательном
порядке. Если функция определяет значения по умолчанию, они будут
использоваться, когда функции передается недостаточное число аргументов.
Если функция использует форму * определения списка аргументов переменной
длины, она сможет принимать большее число аргументов – дополнительные
аргументы будут собраны в структуру данных под именем с символом *.


 Тонкости сопоставления

 Ниже приводится несколько правил в языке Python, которым вам необходимо
следовать, если у вас появится потребность использовать специальные
режимы сопоставления аргументов:

  В вызове функции аргументы должны указываться в следующем порядке:
 любые позиционные аргументы (значения), за которыми могут следовать
 любые именованные аргументы (name=value) и аргументы в форме *sequence,
 за которыми могут следовать аргументы в форме **dict.

  В заголовке функции аргументы должны указываться в следующем порядке:
 любые обычные аргументы (name), за которыми могут следовать аргументы
 со значениями по умолчанию (name=value), за которыми следуют аргументы
 в форме *name (или * в 3.0), если имеются, за которыми могут следовать
 любые имена или пары name=value аргументов, которые передаются только
 по имени (в 3.0), за которыми могут следовать аргументы в форме **name.

 В обоих случаях, и в вызове, и в заголовке функции, форма **arg должна
следовать последней в списке. Если попытаться расставить аргументы
в любом другом порядке, вы получите сообщение о синтаксической ошибке,
потому что все остальные комбинации могут порождать неоднозначность.
Действия, которые выполняет интерпретатор при сопоставлении аргументов
перед присваиванием, грубо можно описать так:

 1. Сопоставление неименованных аргументов по позициям.

 2. Сопоставление именованных аргументов по именам.

 3. Сопоставление дополнительных неименованных аргументов
с кортежем *name.

 4. Сопоставление дополнительных именованных аргументов
со словарем**name.

 5. Сопоставление значений по умолчанию с отсутствующими именованными
аргументами.

 После этого интерпретатор убеждается, что каждому аргументу
соответствует только одно значение, – в противном случае возбуждается
исключение. По окончании сопоставления всех аргументов интерпретатор
связывает имена аргументов с полученными объектами.

 В действительности интерпретатор использует более сложный алгоритм
сопоставления (например, он также должен учитывать сопоставление
аргументов, которые могут передаваться только по имени, – появившихся
в версии 3.0), поэтому мы оставим более точное описание за руководством
по языку программирования Python. Хотя знание этого алгоритма
и не является обязательным, тем не менее его понимание может помочь
разобраться в некоторых сложных ситуациях, особенно когда в деле
замешаны режимы сопоставления.

 В Python 3.0 имена аргументов в заголовке функции могут также
снабжаться аннотациями в форме name:value (или name:value=default,
если имеется значение по умолчанию). Это просто возможность вставлять
дополнительное описание аргументов, которая никак не влияет
и не изменяет правила, определяющие порядок следования аргументов.
Сама функция также может снабжаться аннотацией в форме def f()->value.
Подробнее об аннотациях функций рассказывается в главе 19.
"""