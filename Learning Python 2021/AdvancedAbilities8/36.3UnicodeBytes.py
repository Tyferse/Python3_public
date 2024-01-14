"""
 Использование текстовых и двоичных файлов

 В этом разделе мы подробно исследуем воздействие строковой модели,
реализованной в Python 3.0, на основные операции над файлами,
представленные ранее в этой книге. Как уже упоминалось выше,
режим открытия файла имеет важное значение – он определяет
типы объектов, которые будут использоваться в ваших сценариях
для представления содержимого файлов. Текстовый режим подразумевает
использование объектов типа str, а двоичный режим – объектов типа bytes:

  Содержимое файлов, открытых в текстовом режиме, интерпретируется
 как текст, состоящий из символов Юникода. При этом используется либо
 кодировка по умолчанию в соответствии с настройками системы,
 либо кодировка, которая была указана явно. Передавая название кодировки
 в функцию open, вы можете принудительно определить различные виды
 преобразований файлов Юникода. Кроме того, при работе с файлами,
 открытыми в текстовом режиме, автоматически выполняется преобразование
 символов конца строки: по умолчанию все возможные формы обозначения
 конца строки преобразуются в единственный символ ‘\n’ независимо
 от платформы, на которой выполняется сценарий. Как описывалось ранее,
 при работе с текстовыми файлами дополнительно автоматически
 выполняется чтение и запись маркера порядка следования байтов
 (Byte Order Mark, BOM), который сохраняется в начале файла
 при использовании некоторых схем кодирования Юникода.

  При работе с файлами, открытыми в двоичном режиме, их содержимое
 возвращается в виде последовательности целых чисел, представляющих
 значения байтов, без предварительного кодирования или декодирования
 и без преобразования символов конца строки.

 Второй аргумент функции open определяет режим обработки файла –
текстовый или двоичный, как и в Python 2.X. Добавление символа «b»
в эту строку определяет двоичный режим (например, “rb” обозначает
двоичный режим только для чтения). По умолчанию используется режим “rt”
– он обозначает то же самое, что и режим “r”, то есть режим чтения
из текстового файла (как и в версии 2.X).

 Однако в Python 3.0 аргумент режима в вызове функции open также
определяет тип объектов, которые будут представлять содержимое файла,
независимо от платформы, на которой выполняется сценарий, – при работе
с текстовыми файлами операциями чтения и записи будут возвращаться
и приниматься объекты типа str, а при работе с двоичными файлами
операциями чтения и записи будут возвращаться и приниматься объекты
типа bytes (операции записи могут также принимать объекты
типа bytearray).


 Основы текстовых файлов

 Начнем с демонстрации основных операций ввода-вывода. Пока вы работаете
с простыми текстовыми файлами (например, с файлами, содержащими текст
ASCII) и не беспокоитесь о тонкостях кодирования строк с использованием
кодировок, отличных от системной кодировки по умолчанию, файлы
в Python 3.0 выглядят практически так же, как и в Python 2.X (то есть
вы просто работаете с обычными строками). Например, ниже выполняется
запись одной строки текста в файл и чтение ее из файла, при этом
все выглядит точно так же, как в версии 2.6 (обратите внимание,
что в версии 3.0 слово file больше не является зарезервированным
именем типа, поэтому мы вполне можем использовать его в качестве имени
переменной):
"""

file = open('temp', 'w')
file.write('abc\n')  # Возвратит количество записанных байтов
file.close()  # Закрыть файл, чтобы вытолкнуть выходной буфер

file = open('temp')  # Режим по умолчанию – “r” (“rt”): чтение текста
text = file.read()

print(repr(text))

print(text)

"""
 Текстовый и двоичный режимы в Python 3.0
 
 В Python 2.6 не делалось больших различий между текстовыми и двоичными
файлами – в обоих случаях содержимое возвращалось и принималось в виде
строк типа str. Единственное отличие состояло в том, что при работе 
с текстовыми файлами на платформе Windows автоматически выполняется 
преобразование символа \n конца строки в последовательность \r\n 
и обратно, тогда как при работе с двоичными файлами это преобразование 
не выполняется (в следующем примере я объединил операции для краткости):
"""

open('temp', 'w').write('abd\n')  # Запись в текстовом режиме:
#                                   добавит \r
print(open('temp', 'r').read())  # Чтение в текстовом режиме:
#                                   отбросит \r

print(open('temp', 'rb').read())  # Чтение в двоичном режиме:
#                                   преобразования не выполняются
open('temp', 'wb').write(b'abc\n')  # Запись в двоичном режиме
print(open('temp', 'r').read())  # \n не преобразуется в \r\n

print(open('temp', 'rb').read())

"""
 В Python 3.0 дело обстоит несколько сложнее из-за различий между типом 
str, используемым для представления текстовых данных, и типом bytes, 
используемым для представления двоичных данных. Для демонстрации 
рассмотрим операцию записи в текстовый файл и операции чтения 
из этого же файла в обоих режимах в Python 3.0. Обратите внимание, 
что операции записи мы должны передать объект типа str, а операции 
чтения возвращают объект типа str или bytes, в зависимости от режима, 
в котором был открыт файл:
"""

# Запись и чтение текстового файла
print(open('temp', 'w').write('abc\n'))  # Текстовый режим записи,
# передается объект str
print(open('temp', 'r').read())  # Текстовый режим чтения,
# возвращает объект str
print(open('temp', 'rb').read())  # Двоичный режим чтения,
# возвращает объект bytes

"""
 Обратите внимание, что на платформе Windows при записи в текстовый файл
символ \n конца строки преобразуется в последовательность \r\n – 
при чтении в текстовом режиме последовательность \r\n преобразуется 
обратно в \n. Однако в двоичном режиме такие преобразования 
не выполняются. То же происходит и под управлением Python 2.6, 
причем именно такое поведение мы ожидаем при работе с двоичными файлами
(никаких дополнительных преобразований не должно выполняться).
Впрочем, в Python 3.0 мы можем управлять этим поведением с помощью 
третьего аргумента функции open.
 
 Теперь проделаем то же самое, но уже с двоичным файлом. На этот раз мы 
передаем операции записи объект типа bytes, а обратно получаем объект 
типа str или bytes, в зависимости от режима, в котором был открыт файл:
"""

# Запись и чтение двоичного файла

open('temp', 'wb').write(b'abc\n')  # Двоичный режим записи,
# передается объект bytes
print(open('temp', 'r').read())  # Текстовый режим чтения,
# возвращается объект str
print(open('temp', 'rb').read())  # Двоичный режим чтения,
#                                     возвращается объект bytes

"""
 Обратите внимание, что в двоичном режиме записи символ \n конца строки
не преобразуется в последовательность \r\n – это именно то, 
что требуется при ра- боте с двоичными данными. Требования к типам 
и поведение файла остаются теми же самыми, даже если данные, записанные 
в файл, по своей природе являются двоичными. В следующем примере литерал
“\x00” представляет двоичный байт с нулевым значением и не является 
печатным символом:

# Запись и чтение двоичных данных
>>> open(‘temp’, ‘wb’).write(b’a\x00c’)  # Передается объект типа bytes
3
>>> open(‘temp’, ‘r’).read()             # Возвращает объект типа str
‘a\x00c’
>>> open(‘temp’, ‘rb’).read()            # Возвращает объект типа bytes
b’a\x00c’

 При работе с файлами, открытыми в двоичном режиме, их содержимое 
возвращается в виде объекта bytes, но операции записи могут принимать 
объекты типа bytes или bytearray – это вполне естественно, потому что 
тип bytearray в действительности является всего лишь изменяемой версией 
типа bytes. Фактически большинство функций и методов в Python 3.0,
которые принимают объекты типа bytes, также могут принимать объекты 
типа bytearray:

# Также допускается передавать объекты bytearrays
>>> BA = bytearray(b’\x01\x02\x03’)
>>> open(‘temp’, ‘wb’).write(BA)
3
>>> open(‘temp’, ‘r’).read()
‘\x01\x02\x03’
>>> open(‘temp’, ‘rb’).read()
b’\x01\x02\x03’


 Несоответствие типа и содержимого

 Обратите внимание, что вам не удастся избежать неприятностей в случае 
нарушения правил использования типов str/bytes при работе с файлами. 
Как видно в следующем примере, мы получаем сообщение об ошибке 
(сокращено здесь) при попытке записать объект bytes в текстовый файл 
или объект str – в двоичный файл:

# Типы не преобразуются автоматически при работе с файлами
>>> open(‘temp’, ‘w’).write(‘abc\n’) # Текстовый режим создает и требует
4                                    # использования объектов типа str
>>> open(‘temp’, ‘w’).write(b’abc\n’)
TypeError: can’t write bytes to text stream

>>> open(‘temp’, ‘wb’).write(b’abc\n’)  # Двоичный режим создает 
4                          # и требует использования объектов типа bytes
>>> open(‘temp’, ‘wb’).write(‘abc\n’)
TypeError: can’t write str to binary stream

 В этом есть определенный смысл: в двоичном режиме текст
не имеет смысла, пока не будет закодирован. Хотя нередко имеется 
возможность выполнить преобразование между типами, закодировав объект 
типа str или декодировав объект типа bytes, тем не менее, 
как описывалось выше в этой главе, вы будете использовать либо тип str,
для представления текстовых данных, либо тип bytes, для представления 
двоичных данных. Так как типы str и bytes в значительной степени 
поддерживают похожие операции, выбор не будет для вас серьезной дилеммой
в большинстве программ (обращайтесь к последнему разделу этой главы 
с описанием инструментов, предназначенных для работы со строками, 
где приводятся некоторые примеры).

 Кроме ограничений, связанных с типами, содержимое файлов также может
иметь значение в версии 3.0. При записи в текстовый файл содержимое 
должно передаваться в виде объектов типа str, а не bytes – в Python 3.0 
нет никакого способа, позволяющего записать двоичные данные в файл, 
открытый в текстовом режиме. В зависимости от правил кодирования байты
со значениями вне диапазона набора символов по умолчанию иногда могут 
встраиваться в обычные строки, и они всегда могут быть записаны в файл,
открытый в двоичном режиме. Однако из-за того, что при работе
с текстовыми файлами, открытыми для чтения, в версии 3.0 автоматически
выполняется декодирование содержимого в соответствии с указанной 
кодировкой Юникода, в текстовом режиме отсутствует возможность прочитать
двоичные данные:
"""

# Двоичные данные невозможно прочитать в текстовом режиме
print(chr(0xFF))  # FF – допустимый символ, FE – нет

print(chr(0xFE))  # UnicodeEncodeError:
# ‘charmap’ codec can’t encode character ‘\xfe’ in position 1...
# open('temp', 'w').write(b'\xFF\xFE\xFD')  # Двоичные данные нельзя
# записать                   TypeError: can’t write bytes to text stream
# в текстовый файл!
# open('temp', 'w').write('\xFF\xFE\xFD')   # Можно записать, если байты
# включены в состав str
open('temp', 'wb').write(b'\xFF\xFE\xFD')  # Запись также можно
#                                            выполнить в двоичном режиме
print(open('temp', 'rb').read())  # Данные всегда можно прочитать
#                                   в двоичном режиме
# print(open('temp', 'r').read())  # В текстовом режиме невозможно
# прочитать данные, которые не могут быть декодированы!
# UnicodeEncodeError:
# ‘charmap’ codec can’t encode characters in position 2-3: ...

"""
 Использование файлов Юникода
 
 
 Чтение и запись Юникода в Python 3.0
 
 Фактически мы можем преобразовывать строки в различные кодировки либо
вручную, с применением методов, либо автоматически, с применением 
файловых операций ввода-вывода. Для демонстрации мы будем использовать 
в этом разделе следующую строку Юникода:

C:\misc> c:\python30\python
>>> S = ‘A\xc4B\xe8C’ # Строка из 5 символов, включает символы,
>>> S # не входящие в набор ASCII
‘AÄBèC’
>>> len(S)
5


 Кодирование вручную
 
 Как мы уже знаем, у нас всегда имеется возможность закодировать строку
в последовательность байтов в соответствии с указанной кодировкой:

# Кодирование вручную с помощью методов
>>> L = S.encode(‘latin-1’)  # 5 байтов после кодирования в latin-1
>>> L
b’A\xc4B\xe8C’
>>> len(L)
5

>>> U = S.encode(‘utf-8’)  # 7 байтов после кодирования в utf-8
>>> U
b’A\xc3\x84B\xc3\xa8C’
>>> len(U)
7


 Кодирование при записи в файл
 
 Теперь попробуем записать нашу строку в текстовый файл в определенной 
кодировке, указав ее название в вызове функции open, – мы могли бы 
сначала выполнить кодирование вручную, а затем записать результат 
в двоичном режиме, однако в этом нет никакой необходимости:

# Автоматическое кодирование при записи в файл
>>> open(‘latindata’, ‘w’, encoding=’latin-1’).write(S) 
#                                                       Запись в latin-1
5
>>> open(‘utf8data’, ‘w’, encoding=’utf-8’).write(S)  #   Запись в utf-8
5
>>> open(‘latindata’, ‘rb’).read()           # Прочитать двоичные данные
b’A\xc4B\xe8C’
>>> open(‘utf8data’, ‘rb’).read()         # Содержимое файлов отличается
b’A\xc3\x84B\xc3\xa8C’


 Декодирование при чтении из файла
 
 Точно так же при чтении произвольных данных Юникода мы просто передаем
название кодировки в вызов функции open, после чего операции чтения 
автоматически будут декодировать последовательности двоичных байтов 
в строки. Мы могли бы прочитать двоичные данные, а затем декодировать их
вручную, хотя в этом случае могут возникнуть сложности при чтении данных
блоками определенного размера (есть риск прочитать неполный символ),
 – но в этом нет никакой необходимости:
 
# Автоматическое декодирование при чтении из файла
>>> open(‘latindata’, ‘r’, encoding=’latin-1’).read()  # Декодирование
‘AÄBèC’                                       # выполняется при чтении
>>> open(‘utf8data’, ‘r’, encoding=’utf-8’).read()    # в соответствии
‘AÄBèC’                                        # с названием кодировки

>>> X = open(‘latindata’, ‘rb’).read()      # Декодирование вручную:
>>> X.decode(‘latin-1’)                     # не требуется
‘AÄBèC’

>>> X = open(‘utf8data’, ‘rb’).read()
>>> X.decode()                          # UTF-8 – кодировка по умолчанию
‘AÄBèC’


 Ошибки декодирования
 
 Наконец, имейте в виду, что такое поведение файлов в 3.0 накладывает 
ограничения на содержимое, которое можно загрузить как текст. 
Как уже говорилось в предыдущем разделе, в версии 3.0 интерпретатор 
должен иметь возможность декодировать данные из текстового файла 
в строку типа str в соответствии с кодировкой по умолчанию или указанной
явно в вызове функции open. Если, к примеру, попытаться открыть 
настоящие двоичные данные в текстовом режиме, в версии 3.0 вы, 
скорее всего, столкнетесь с ошибкой, даже если будете использовать 
объекты корректных типов:

>>> file = open(‘python.exe’, ‘r’)
>>> text = file.read()
UnicodeDecodeError: ‘charmap’ codec can’t decode byte 0x90 
in position 2: ...
>>> file = open(‘python.exe’, ‘rb’)
>>> data = file.read()
>>> data[:20]
b’MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00
\x00\x00’

 Первый из этих примеров может и не привести к появлению ошибки 
в Python 2.X (при работе с обычными файлами текст не декодируется), 
даже при том, что она должна была бы произойти: операция чтения из файла
может вернуть поврежденные данные из-за автоматического преобразования
символов конца строки, которое выполняется в текстовом режиме 
(в процессе чтения любые последовательности байтов \r\n будут 
преобразованы в Windows в символы \n). Чтобы в версии 2.6 содержимое
файла интерпретировалось как текст Юникода, вместо встроенной функции 
open необходимо использовать специальный инструмент, как будет показано 
чуть ниже.

 
 Обработка маркера BOM в Python 3.0
 
 Как описывалось выше в этой главе, некоторые кодировки подразумевают 
сохранение специальной последовательности маркера порядка следования 
байтов (byte order marker, BOM) в начале файлов, определяющей прямой 
или обратный порядок следования байтов или объявляющей тип кодировки.
В любом случае интерпретатор пропускает этот маркер при вводе из файла 
и записывает его при выводе в файл, если его наличие подразумевается 
используемой кодировкой, но иногда мы должны явно указывать 
название кодировки, чтобы явно указать порядок следования байтов.

 Например, при сохранении файла в программе Блокнот (Notepad) в системе
Windows, можно указать тип кодировки в раскрывающемся списке – простой
текст ASCII, UTF-8 или UTF-16 с прямым или обратным порядком следования
байтов. Если, например, в Блокноте сохранить однострочный текстовый файл
spam.txt, выбрав кодировку «ANSI», он будет сохранен как простой 
текстовый файл ASCII без маркера BOM. Если затем прочитать этот файл 
в двоичном режиме из программы на языке Python, можно будет увидеть 
фактические двоичные данные, сохраненные в файле. При чтении этого файла 
в текстовом режиме интерпретатор автоматически выполнит преобразование
символов конца строки – мы сможем декодировать его явно, как текст 
в кодировке UTF-8, потому что набор символов ASCII является 
подмножеством набора символов UTF-8.
"""

import sys


print(sys.getdefaultencoding())

print(open('spam.txt', 'rb').read())  # Текстовый файл ASCII (UTF-8)
print(open('spam.txt', 'r').read())  # В текстовом режиме выполняется
#                                 преобразование символов конца строки
print(open('spam.txt', 'r', encoding='utf-8').read())

"""
 Если сохранить этот файл в Блокноте, выбрав кодировку «UTF-8», в начало
файла будет добавлена трехбайтовая последовательность маркера BOM 
для кодировки UTF-8, и тогда при чтении нам потребуется указать 
более специфическое название кодировки («utf-8-sig»), чтобы вынудить 
интерпретатор пропустить маркер при чтении содержимого файла:
"""

print(open('spam.txt', 'rb').read())  # UTF-8 с 3-байтовым маркером BOM

print(open('spam.txt', 'r').read())

print(open('spam.txt', 'r', encoding='utf-8').read())

print(open('spam.txt', 'r', encoding='utf-8-sig').read())

"""
 Если сохранить этот файл в Блокноте, выбрав кодировку 
«Юникод big endian» («Unicode big endian»), данные будут записаны 
в формате UTF-16 с двухбайтовым маркером BOM – при использовании
названия кодировки «utf-16» в Python интерпретатор автоматически
пропустит маркер BOM, потому что его наличие подразумевается 
этой кодировкой (все файлы с кодировкой UTF-16 имеют маркер BOM). О
днако, если указать кодировку «utf-16-be», интерпретатор 
будет обрабатывать файл как текст в формате UTF-16 с прямым (big-endian)
порядком следования байтов, но не будет пропускать маркер BOM:
"""

open('spam.txt', 'rb').read()

print(open('spam.txt', 'r').read())

# print(open('spam.txt', 'r', encoding='utf-16').read())
# UnicodeDecodeError: 'utf-16-le'
# codec can't decode byte 0x0a in position 10: truncated data

# print(open('spam.txt', 'r', encoding='utf-16-be').read())
# UnicodeDecodeError: 'utf-16-be'
# codec can't decode byte 0x0a in position 10: truncated data

"""
 То же верно и для операции записи. Чтобы из программы на языке Python 
записать в начало файла Юникода маркер BOM кодировки UTF-8, мы должны
явно указать более специфическую кодировку «utf-8-sig», потому что
при использовании имени кодировки «utf-8» запись маркера BOM 
не выполняется:
"""

print(open('temp.txt', 'w', encoding='utf-8').write('spam\nSPAM\n'))

print(open('temp.txt', 'rb').read())  # Нет маркера BOM

print(open('temp.txt', 'w', encoding='utf-8-sig').write('spam\nSPAM\n'))

print(open('temp.txt', 'rb').read())  # Маркер BOM был записан

print(open('temp.txt', 'r').read())

print(open('temp.txt', 'r', encoding='utf-8').read())  # Прочитает BOM

print(open('temp.txt', 'r', encoding='utf-8-sig').read())
#                                                          Пропустит BOM

"""
 Обратите внимание: несмотря на то, при использовании кодировки «utf-8» 
запись маркера BOM не производится, тем не менее мы сможем прочитать 
содержимое этого файла при использовании любой из кодировок, «utf-8» 
и «utf-8-sig», – используйте последнюю при чтении файла,
если вы не уверены в том, присутствует ли маркер BOM в файле.
"""

print(open('temp.txt', 'w').write('spam\nSPAM\n'))

print(open('temp.txt', 'rb').read())  # Данные без маркера BOM

print(open('temp.txt', 'r').read())  # Допускается использование
#                                        любой кодировки семейства utf-8
print(open('temp.txt', 'r', encoding='utf-8').read())

print(open('temp.txt', 'r', encoding='utf-8-sig').read())

"""
 Наконец, при использовании кодировки «utf-16» обработка маркера BOM 
производится автоматически: при выводе данные записываются 
с использованием аппаратного порядка следования байтов, а маркер BOM
всегда записывается в файл; при вводе данные декодируются с учетом BOM, 
а сам маркер BOM всегда пропускается. С помощью более специфичных 
кодировок UTF-16 можно явно указать иной порядок следования байтов, 
однако при этом вам, возможно, придется вручную записывать и пропускать 
маркер BOM, если он необходим или присутствует в файле:
"""

print(sys.byteorder)

print(open('temp.txt', 'w', encoding='utf-16').write('spam\nSPAM\n'))

print(open('temp.txt', 'rb').read())

print(open('temp.txt', 'r', encoding='utf-16').read())

print(open('temp.txt', 'w', encoding='utf-16-be')
      .write('\ufeffspam\nSPAM\n'))

print(open('spam.txt', 'rb').read())

print(open('temp.txt', 'r', encoding='utf-16').read())

print(open('temp.txt', 'r', encoding='utf-16-be').read())

"""
 Более специфичные кодировки UTF-16 отлично подходят для работы 
с файлами, в которых отсутствует маркер BOM, тогда как при использовании 
кодировки «utf-16» требуется наличие маркера в файле, 
чтобы при выполнении операции чтения интерпретатор мог определить 
порядок следования байтов:
"""

print(open('temp.txt', 'w', encoding='utf-16-le').write('SPAM'))

print(open('temp.txt', 'rb').read())  # Маркер BOM отсутствует
#                                                         и не ожидается
print(open('temp.txt', 'r', encoding='utf-16-le').read())

# print(open('temp.txt', 'r', encoding='utf-16').read())
# UnicodeError: UTF-16 stream does not start with BOM

"""
 Другие инструменты для работы со строками в Python 3.0
 
 
 Модуль re для сопоставления с шаблонами
 
 Модуль re, реализующий средства сопоставления строк с шаблонами 
и входящий в состав стандартной библиотеки Python, обеспечивает более 
универсальные способы работы со строками, чем простые строковые методы, 
такие как find, split и replace. При использовании модуля re строки, 
которые требуется отыскать или по которым требуется выполнить разбиение
исходного текста, могут быть описаны в виде обобщенных шаблонов, 
а не буквального текста. В Python 3.0 этот модуль способен работать
с любыми строковыми типами – str, bytes и bytearray – и в качестве
результата возвращает строки того же типа, что и испытуемый 
строковый объект.

 Ниже демонстрируется, как можно использовать этот модуль в Python 3.0
для извлечения подстрок из текстовой строки. В пределах строки шаблон
конструкция (.*) означает ноль или более (*) любых символов (.), 
которые должны сохраняться в виде подстроки совпадения (()). 
Части исходной строки, совпавшие с частями шаблона в круглых скобках,
можно получить после успешного поиска с помощью метода group или groups:
"""

import re


S = 'Bugger all down here on earth!'  # Строка текста
B = b'Bugger all down here on earth!'  # То, что обычно получается
# в результате чтения из файла
print(re.match('(.*) down (.*) on (.*)', S).groups())  # Выборка
#                                                  совпадений с шаблоном
# Совпавшие подстроки
print(re.match(b'(.*) down (.*) on (.*)', B).groups())
# Подстроки типа bytes

"""
 Поскольку объекты типов bytes и str поддерживают практически одни 
и те же операции, различия между ними становятся практически 
незаметными. Но, обратите внимание, что как и в случае других функций,
в Python 3.0 вы не сможете смешивать объекты типов str и bytes
в вызовах функций модуля re (впрочем, если вы не планируете производить
поиск по шаблону в двоичных данных, то вам не о чем беспокоиться):


print(re.match('(.*) down (.*) on (.*)', B).groups())
TypeError: can’t use a string pattern on a bytes-like object

print(re.match(b'(.*) down (.*) on (.*)', S).groups())
TypeError: can’t use a bytes pattern on a string-like object

print(re.match(b'(.*) down (.*) on (.*)', bytearray(B)).groups())
TypeError: can’t use a string pattern on a bytes-like object

print(re.match('(.*) down (.*) on (.*)', bytearray(B)).groups())
TypeError: can’t use a string pattern on a bytes-like object


 Модуль struct для работы с двоичными данными
 
 Модуль struct в языке Python используется для создания и извлечения 
упакованных двоичных данных из строк. В версии 3.0 он действует 
точно так же, как и в версии 2.X, с той лишь разницей, что упакованные
двоичные данные могут быть представлены исключительно объектами 
типа bytes и bytearray (что имеет определенный смысл, особенно 
если учесть, что эти типы предназначены для работы с двоичными данными
а не с произвольным текстом). 

 Ниже приводится пример, в котором в строку упаковываются три объекта,
в соответствии с двоичной спецификацией (создаются четырехбайтное целое,
четырех байтовая строка и двухбайтовое целое):
"""

# print(pack('>i4sh', 7, 'spam', 8))
# struct.error: argument for 's' must be a bytes object
# Тип bytes в 3.0 (строка 8-битных данных)

"""
 Однако поскольку тип bytes имеет интерфейс, практически идентичный 
интерфейсу типа str в обеих версиях Python, 3.0 и 2.6, большинству 
программистов, вероятно, не придется беспокоиться – различия между ними
не скажутся на работоспособности большинства существующих программ,
особенно если учесть, что при чтении из двоичных файлов объекты 
типа bytes создаются автоматически. Даже при том, что последняя операция
в примере ниже терпит неудачу из-за несоответствия типов, тем не менее, 
в большинстве программ двоичные данные обычно читаются из файла, 
а не создаются в виде строк:
"""

import struct


B = struct.pack('>i4sh', 7, b'spam', 8)
print(B)

vals = struct.unpack('>i4sh', B)
print(vals)

# vals = struct.unpack('>i4sh', B.decode())
# TypeError: a bytes-like object is required, not 'str'

"""
 За исключением нового синтаксиса определения объектов типа bytes,
создание и чтение двоичных данных из файлов в версии 3.0 выполняется 
точно так же, как и в версии 2.X. Ниже приводится программный код,
в котором тип bytes объектов становится наиболее заметным:
"""

# Запись упакованных двоичных данных в двоичный файл
F = open('data.bin', 'wb')  # Открыть файл в двоичном режиме для записи

data = struct.pack('>i4sh', 7, b'spam', 8)
# Создать упаков. двоич. данные
print(data)  # В 3.0 – тип bytes, не str

F.write(data)  # Записать в файл

F.close()
# Чтение упакованных двоичных данных из двоичного файла
F = open('data.bin', 'rb')  # Открыть файл в двоичном режиме для чтения
data = F.read()  # Прочитать байты
print(data)

values = struct.unpack('>i4sh', data)  # Извлечь упаков. двоичные данные
print(values)  # обратно в объекты языка Python

"""
 После извлечения упакованных двоичных данных в объекты языка Python,
как в этом примере, вы можете попробовать еще глубже погрузиться 
в двоичный мир – из строк можно извлекать значения отдельных байтов 
и получать срезы; из целых чисел с помощью битовых операций можно 
извлекать отдельные биты и так далее.
"""

# Доступ к отдельным битам в целых числах
print(bin(values[0]))  # Можно получить целое число в двоичном виде

print(values[0] & 0x01)  # Проверит первый (младший) бит в целом числе

print(values[0] | 0b1010)  # Битовое ИЛИ: установит указанные биты

print(bin(values[0] | 0b1010))  # 15 – десятичное, 1111 – двоичное

print(bin(values[0] ^ 0b1010))  # Битовое ИСКЛЮЧАЮЩЕЕ ИЛИ: сбросит биты
# с одинаковыми значениями
print(bool(values[0] & 0b100))  # Проверит, установлен ли бит 3

print(bool(values[0] & 0b1000))  # Проверит, установлен ли бит 4

"""
 Так как строки bytes, получающиеся в результате извлечения двоичных 
данных, являются последовательностями коротких целых чисел, мы можем 
применить те же самые операции к отдельным байтам строки:
"""

# Доступ к байтам в получившихся строках и к битам внутри них
print(values[1])

print(values[1][0])  # Строка байтов: последовательность целых чисел

print(values[1][1:])  # Выведет в виде символов ASCII

print(bin(values[1][0]))  # Байты в строках можно получить
#                           в двоичном виде

print(bin(values[1][0] | 0b1100))  # Установит указанные биты

print(values[1][0] | 0b1100)

"""
 Модуль pickle для сериализации объектов
 
 Имейте в виду, что в Python 3.0 модуль pickle всегда создает объекты
типа bytes независимо от используемой версии «протокола» 
(формата данных). Убедиться в этом можно, воспользовавшись функцией 
dumps из модуля, которая возвращает строку с объектом 
в последовательной форме:
"""

import pickle  # dumps() возвращает строку с сериализованным объектом


print(pickle.dumps([1, 2, 3]))  # В Python 3.0 протокол
#                                 по умолчанию=3=двоичный

print(pickle.dumps([1, 2, 3], protocol=0))  # Протокол ASCII 0,
# но все равно возвращает объект bytes!

"""
 Вследствие этого подразумевается, что файлы, в которых сохраняются 
сериализованные объекты, в Python 3.0 всегда должны открываться 
в двоичном режиме, потому что для представления данных в текстовых
файлах используются объекты типа str, а не bytes – функция dump просто 
пытается записать строку с объектом в файл, открытый для записи:
"""

# pickle.dump([1, 2, 3], open('temp', 'w'))  # В текстовый файл нельзя
# TypeError: write() argument must be str, not bytes
# записать объект bytes! Независимо от протокола

# pickle.dump([1, 2, 3], open('temp', 'w'), protocol=0)
# TypeError: write() argument must be str, not bytes

pickle.dump([1, 2, 3], open('temp', 'wb'))  # Всегда используйте
print(open('temp', 'r').read())  # двоичный режим в 3.0

"""
 Поскольку сериализованные данные не декодируются в текст Юникода, то же
самое относится к операциям чтения из файла – в версии 3.0 запись 
и чтение сериализованных данных всегда должны выполняться 
в двоичном режиме:
"""

print(pickle.load(open('temp', 'rb')))

print(open('temp', 'rb').read())

"""
 Поскольку в большинстве программ сохранение и извлечение 
сериализованных объектов производится интерпретатором автоматически
и программному коду не приходится иметь дело непосредственно 
с сериализованными данными, требование всегда использовать 
двоичный режим при работе с файлами является единственным существенным 
отличием новой модели сохранения объектов в Python 3.0.


 Инструменты синтаксического анализа разметки XML
 
 XML – это язык разметки, основанный на тегах, используемый 
для представления информации в структурированном виде. Часто применяется
для оформления документов и данных, доставляемых через Веб. Некоторую 
долю информации можно извлечь из текста XML с помощью простых 
строковых методов или модуля re, однако для извлечения информации 
из многоуровневых конструкций и из атрибутов тегов требуется выполнять 
более точный и более полный синтаксический анализ разметки.

 Вследствие того, что формат XML получил чрезвычайно широкое 
распространение, в состав Python был включен целый пакет инструментов
для синтаксического анализа разметки XML, поддерживающих модели парсинга
SAX и DOM, а также пакет, известный под названием ElementTree – 
интерфейс на языке Python, позволяющий анализировать и конструировать 
документы XML. Помимо простого синтаксического анализа среди свободного 
программного обеспечения можно найти поддержку дополнительных 
инструментов XML, таких как XPath, Xquery, XSLT, и многих других.

 Формат XML по умолчанию представляет текст в виде Юникода с целью 
обеспечить поддержку интернационализации. Большинство инструментов 
синтаксического анализа XML в языке Python всегда возвращали строки 
Юникода, однако тип результатов изменился с unicode в Python 2.X 
на более универсальный str в Python 3.0. Это вполне объяснимо, 
если вспомнить, что в Python 3.0 строки типа str являются строками 
Юникода независимо от того, используется кодировка ASCII 
или какая-то другая.

 Предположим, что у нас имеется простой файл XML mybooks.xml:
 
<books>
      <date>2009</date>
      <title>Learning Python</title>
      <title>Programming Python</title>
      <title>Python Pocket Reference</title>
      <publisher>O’Reilly Media</publisher>
</books>

 и нам требуется извлечь и отобразить содержимое всех вложенных 
тегов title, как показано ниже:

      Learning Python
      Programming Python
      Python Pocket Reference
      
 Существует по меньшей мере четыре основных способа решить поставленную
задачу (не учитывая дополнительных инструментов, таких как XPath). 
Во первых, мы могли бы выполнить поиск по шаблону, однако такой способ 
не дает желаемой точности, когда содержимое документа XML невозможно 
предсказать. Там, где это применимо, с подобной работой прекрасно 
справляется модуль re, с которым мы познакомились выше. Его метод match 
отыскивает совпадения с начала строки, метод search заглядывает вперед 
в поисках совпадений, а метод findall, используемый здесь, отыскивает 
в строке все совпадения с шаблоном (и возвращает результат в виде списка 
совпавших подстрок, соответствующих группам в круглых скобках,
или кортежей для множественных групп):
"""

text = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found:
    print(title)

"""
 Во-вторых, для большей надежности мы могли бы выполнить полный 
синтаксический анализ разметки XML с помощью парсера DOM, имеющегося
в стандартной библиотеке. Парсер DOM преобразует документ XML в дерево
объектов и предоставляет интерфейс для навигации по дереву, извлечения
атрибутов и значений тегов – интерфейс имеет формальную спецификацию,
не зависящую от языка Python:
"""

from xml.dom.minidom import parse, Node


xmltree = parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType == Node.TEXT_NODE:
            print(node2.data)

"""
 В качестве третьего варианта можно было бы использовать парсер SAX, 
также входящий в стандартную библиотеку. В модели SAX в процессе анализа 
производятся вызовы методов класса, которым передается дополнительная 
информация, позволяющая определить, в каком месте документа находится
парсер, и выбрать необходимые данные:
"""

import xml.sax.handler


class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False

    def startElement(self, name, attributes):
        if name == 'title':
            self.inTitle = True

    def characters(self, data):
        if self.inTitle:
            print(data)

    def endElement(self, name):
        if name == 'title':
            self.inTitle = False


import xml.sax


parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('mybooks.xml')

"""
 Наконец, система ElementTree, доступная в виде пакета etree 
в стандартной библиотеке, часто позволяет добиться того же эффекта, 
что и парсеры XML DOM, но за счет меньшего объема программного кода. 
Этот характерный для Python способ позволяет анализировать 
и конструировать документы XML. После анализа документа система 
ElementTree обеспечивает доступ к компонентам документа:
"""

from xml.etree.ElementTree import parse


tree = parse('mybooks.xml')
for E in tree.findall('title'):
    print(E.text)