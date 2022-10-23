# Что дальше?

"""
 Деревья

 Вернемся к примеру с бинарным поиском.
Когда пользователь вводит свое имя на сайте Facebook,
сайт должен проверить содержимое большого массива, чтобы узнать,
существует ли пользователь с таким именем. Мы выяснили,
что для нахождения значения в массиве быстрее всего воспользоваться
бинарным поиском. Однако здесь возникает проблема: каждый раз,
когда на сайте регистрируется новый пользователь,
придется заново сортировать массив,
потому что бинарный поиск работает только с отсортированными массивами.
Насколько удобнее было бы вставить пользователя
в правильную ячейку массива,
чтобы потом его не пришлось сортировать заново!
Именно эта идея заложена в основу структуры данных
бинарного дерева поиска.

 Бинарное дерево поиска выглядит так:

 Для каждого узла все узлы левого поддерева содержат меньшие значения,
а все узлы правого поддерева - большие значения.

 Предположим, вы ищете узел Maggie. Поиск начинается с корневого узла.

 Строка Maggie идет после David, поэтому идем направо.

 Строка Maggie предшествует Manning, поэтому идем налево.

 Мы нашли узел Maggie! В целом процедура поиска напоминает
бинарный поиск. Поиск элемента в бинарном дереве поиска
в среднем выполняется за время O(log п), а в худшем случае -
за время О(п). Поиск в отсортированном массиве выполняется
за время O(log п) в худшем случае - казалось бы,
отсортированный массив эффективнее.
Однако бинарное дерево поиска в среднем работает намного быстрее
при удалении и вставке элементов.

             массив    бинарное дерево поиска
  поиск      O(log n)  O(log n)
  вставка    O(n)      O(log n)
  удаление   O(n)      O(log n)

 У бинарных деревьев поиска есть и свои недостатки: во-первых,
они не поддерживают произвольный доступ. Вы не сможете потребовать:
"выдайте мне i-й элемент этого дерева". Кроме того,
в таблице приведено среднеевремя выполнения операций;
оно зависит от сбалансированности дерева. Допустим,
ваше дерево не сбалансировано, как на следующем рисунке.

 Видите, как дерево перекошено вправо? Эффективность такого дерева
оставляет желать лучшего, потому что это дерево не сбалансировано.
Существуют специальные бинарные деревья поиска,
cпособные к самобалансировке (как, например, красно-черные деревья).

Где же используются бинарные деревья поиска? В-деревья,
особая разновидность бинарных деревьев,
обычно используются для хранения информации в базах данных.

 Если вас интересуют базы данных или более сложные структуры данных,
поищите информацию по следующим темам:

  в-деревья;

  красно - черные деревья;

  кучи;

  скошенные (splay) деревья.


 Инвертированные индексы

 Перед вами сильно упрощенное объяснение того,
rак работает поисковая система. Допустим, имеются три веб-страницы
с простым содержимым.

 Построим хеш-таблицу для этого содержимого.

  Hi    A, b
  there A, C
  Adit  B
  we    C
  go    C

 Ключами хеш-таблицы являются слова, а значения указывают,
на каких страницах встречается каждое слово. Те перь предположим,
что пользователь ищет слово hi. Посмотрим,
на каких страницах это слово встречается.

 Ага, слово встречается на страницах А и В.
Выведе м эти страницы в результатах поиска. Или предположим,
что польз овател ь ищет слово there. Вы знаете,
что это слово встречается на страницах А и С. Несложно, верно?
Это очень полезная структура данных: хеш-таблица,
связывающая слова с местами, в которых эти слова встречаются.
Такая структура данных, называемая инвертированным индексом,
часто используется для построения поисковых систем.
Если вас интересует область поиска,
эта тема станет хорошей отправной точкой для дальнейшего изучения.


 Преобразование Фурье

 Преобразование Фурье - действительно выдающийся алгоритм:
великолепный, элегантный и имеющий миллион практических применений.
Лучшая аналогия для преобразования Фурье приводится на сайте
Better Explained (отличный веб-сайт,
на котором просто объясняется математическая теория):
если у вас есть коктейль, преобразование Фурье сообщает,
из каких ингредиентов он состоит.
Или для заданной песни преобразование разделяет ее на отдельные частоты.

 Оказывается, эта простая идея находит множество
практических применений. Например,
если песню можно разложить на частоты, вы можете усилить тот диапазон,
который вас интересует, - скажем, усилить низкие частоты
и приглушить высокие. Преобразование Фурье прекрасно подходит
для обработки сигналов. Также оно может применяться для сжатия музыки:
сначала звуковой файл разбивается на составляющие.
Преобразование Фурье сообщает,
какой вклад вносит каждая составляющая в музыку,
что позволяет исключить несущественные составляющие. Собственно,
именно так работает музыкальный формат МРЗ!

 Музыка - не единственный вид цифровых сигналов.
Графический формат JPG также использует сжатие
и работает по тому же принципу. Преобразование Фурье также применяется
для прогнозирования землетрясений и анализа ДНК.

 С его помощью можно построить аналог Shazam - приложение,
которое находит песни по отрывкам.
Преобразование Фурье очень часто применяется на практике.
Почти наверняка вы с ним еще столкнетесь!


Параллельные алгоритмы

 Следующие три темы связаны с масштабируемостью
и обработкой больших объемов данных.
Когда-то компьютеры становились все быстрее и быстрее. Если вы хотели,
чтобы ваш алгоритм работал быстрее,
можно было подождать несколько месяцев
и запустить программу на более мощном компьютере.
Но сейчас этот период подошел к концу.
Современные компьютеры и ноутбуки оснащаются многоядерными процессорами.
Чтобы алгоритм заработал быстрее, необходимо преобразовать его в форму,
подходящую для параллельного выполнения сразу на всех ядрах!

 Рассмотрим простой пример. Лучшее время выполнения
для алгоритма сортировки равно приблизительно О(п log п). Известно,
что массив невозможно отсортировать за время О(п),
если только не воспользоваться параллельным алгоритмом!
Существует параллельная версия быстрой сортировки,
которая сортирует массив за время О( п ).

 Параллельный алгоритм трудно разработать.
И так же трудно убедиться в том, что он работает правильно, и понять,
какой прирост скорости он обеспечивает. Одно можно заявить твердо:
выигрыш по времени не линеен. Следовательно,
если процессор вашего компьютера имеет два ядра вместо одного,
из этого не следует, что ваш алгоритм по волшебству заработает
вдвое быстрее. Это объясняется несколькими причинами.

  Затраты ресурсов на управление параллелизмом - допустим,
 нужно отсортировать массив из 1000 элементов.
 Как разбить эту задачу для выполнения на двух ядрах?
 Выделить каждому ядру 500 элементов,
 а затем объединить два отсортированных массива
 в один большой отсортированный массив?
 Слияние двух массивов требует времени.

  Распределение нагрузки - допустим, необходимо выполнить 1 О задач,
 и вы назначаете каждому ядру 5 задач. Однако ядру А достаются
 все простые задачи, поэтому оно выполняет свою работу за 1 О секунд,
 тогда как ядро В справится со сложными задачами только за минуту.
 Это означает, что ядро А целых 50 секунд простаивает,
 пока ядро В выполняет всю работу!
 Как организовать равномерное распределение работы,
 чтобы оба ядра трудились с одинаковой интенсивностью?

 Если вас интересует теоретическая сторона производительности
и масштабируемости, возможно, параллельные алгоритмы - именно то,
что вам нужно!


 MapReduce

О дна разновидность параллельных алгоритмов в последнее время
становится все более популярной: распределенные алгоритмы. Конечно,
параллельный алгоритм удобно запустить на компьютере,
если для его выполнения потребуется от двух до четырех ядер,
а если нужны сотни ядер? Тогда алгоритм записывается так,
чтобы он мог выполняться на множестве машин. Алгоритм MapReduce -
известный представитель семейства распределенных алгоритмов.
Для работы с ним можно воспользоваться популярной системой
с открытым кодом Apache Hadoop.


 Для чего нужны распределенные алгоритмы?

 Предположим, имеется таблица с миллиардами или триллионами записей
и вы хотите применить к ней сложный вопрос SQL. Выполнить его в MySQL
не удастся, потому что MySQL начнет "тормозить"
уже после нескольких миллиардов записей.
Используйте MapReduce через Hadoop!

 Или, предположим, вам нужно обработать длинный список заданий.
Обработка каждого задания занимает 1 О секунд, в
сего требует обработки 1 миллион заданий.
Если выполнять эту работу на одном компьютере,
она займет несколько месяцев!
Если бы ее можно было выполнить на 100 машинах,
работа завершилась бы за несколько дней.

 Распределенные алгоритмы хорошо работают в тех ситуациях,
когда вам нужно выполнить большой объем работы
и вы хотите сократить время ее выполнения.
В основе технологии MapReduce лежат две простые идеи:
функция отображения map и функция свертки reduce.


 Функция map

 Функция map проста: она получает массив
и применяет одну функцию к каждому элементу массива. Скажем,
в следующем примере происходит удваивание каждого элемента в массиве:
"""

arr1 = [1, 2, 3, 4, 5]
arr2 = map(lambda x: 2 * x, arr1)

print(arr2)
print(set(arr2))

'''
 Массив arr2 теперь содержит значения [2, 4, б, 8, 10] - 
все элементы arr1 увеличились вдвое! 
Удвоение выполняется достаточно быстро. Но представьте, 
что выполнение применяемой функции требует больше времени. 
Взгляните на следующий псевдокод:

arr1 = # Список URL
arr2 = map(download_page, arr1)

 Имеется список URL-aдpecoв, нужно загрузить каждую страниuу 
и сохранить содержимое в arr2.
Для каждого адреса загрузка занимает пару секунд. 
Для 1000 адресов потребуется пара часов! А теперь представьте, 
что у вас имеется 100 машин 
и map автоматически распределяет работу между ними.
Тогда в любой момент будут загружаться сразу 100 страниц одновременно,
и работа пойдет намного быстрее!


 Функция reduce
 
 Функция reduce иногда сбивает людей с толку. Идея заключается в том, 
что весь список элементов «сокращается~ до одного элемента. Напомню,
что функция map переходит от одного массива к другому.

 С функцией reduce массив преобразуется в один элемент.
 
 Пример:
'''

from functools import reduce


arr3 = [1, 2, 3, 4, 5]
a = reduce(lambda n, m: n+m, arr3)

print(a)

'''
 В данном случае все элементы в массиве просто суммируются: 
1 + 2 + 3 + 4 + 5 = 15! Я не буду рассматривать свертку более подробно, 
потому что в Интернете хватает руководств по этой теме.

 MapReduce использует эти две простые концепции
для выполнения запросов на нескольких машинах. 
При использовании большого набора данных (миллиарды записей) 
MapReduce выдаст ответ за минуты, тогда как традиционной базе данных 
на это потребуются многие часы.
'''
