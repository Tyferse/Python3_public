# Алгоритм Дейкстры

"""
 В предыдущей главе вы узнали , как найти путь из точки А в точку В.

 Найденный путь необязательно окажется самым быстрым.
Этот путь считается кратчайшим,
потому что он состоит из наименьшего количества сегментов (три сегмента).
Но предположим, с каждым сегментом
связывается продолжительность перемещения. И тогда выясняется,
что существует и более быстрый путь.

 В предыдущей главе рассматривался поиск в ширину.
Этот алгоритм находит путь с минимальным количеством сегментов
(граф на первом рисунке).
А если вы захотите найти самый быстрый путь (второй граф)?
Быстрее всего это делается при помощи другого алгоритма,
который называется алгоритмом Дейкстры.


 Работа с алгоритмом Дейкстры

 Каждому ребру назначается время перемещения в минутах.
Алгоритм Дейкстры используется для поиска пути от начальной точки
к конечной за кратчайшее возможное время.
Применив к этому графу поиск в ширину,
вы получите следующий кратчайший путь.

 Этот путь занимает 7 минут. А может, существует путь,
который займет меньше времени?
Алгоритм Дейкстры состоит из четырех шагов:

1. Найти узел с наименьшей стоимостью (то есть узел,
до которого можно добраться за минимальное время).

2. Обновить стоимости соседей этого узла
(вскоре я объясню, что имеется в виду).

3. Повторять, пока это не будет сделано для всех узлов графа.

4. Вычислить итоговый путь.

Шаг 1: найти узел с наименьшей стоимостью.
Вы стоите в самом начале и думаете,
куда направиться: к узлу А или к узлу В.
Сколько времени понадобится, чтобы добраться до каждого из этих узлов?

 До узла А вы будете добираться 6 минут, а до узла В - 2 минуты.
Что касается остальных узлов, мы о них пока ничего не знаем.

 Так как время достижения конечного узла остается неизвестным,
мы считаем, что оно бесконечно (вскоре вы увидите почему).
Узел В - ближайший... он находится всего в 2 минутах.

 Шаг 2: вычислить, сколько времени потребуется для того,
чтобы добраться до всех соседей В при переходе по ребру из В.

 Ого, да мы обнаружили более короткий путь к узлу А!
Раньше для перехода к нему требовалось 6 минут.

 А если идти через узел В, то существует путь,
который занимает всего 5 минут!

 Если вы нашли более короткий путь для соседа В, обновите его стоимость.
В данном случае мы нашли:

  Более короткий путь к А (сокращение с 6 минут до 5 минут).

  Более короткий путь к конечному узлу
(сокращение от бесконечности до 7 минут).

Шаг 3:повторяем!

Снова шаr 1: находим узел, для перехода к которому
требуется наименьшее время. С узлом В работа закончена,
поэтому наименьшую оценку времени имеет узел А.

 Снова шаr 2: обновляем стоимости соседей А.

 Путь до конечного узла теперь занимает всего 6 минут!
Алгоритм Дейкстры выполнен для каждого узла
(выполнять его для конечного узла не нужно).
К этому моменту вам известно следующее:

  Чтобы добраться до узла В, нужно 2 минуты.

  Чтобы добраться до узла А, нужно 5 минут.

  Чтобы добраться до конечного узла, нужно 6 минут.

 Последний шаг - вычисление итогового пути -
откладывается до следующего раздела.

 Алгоритм поиска в ширину не найдет этот путь как кратчайший,
потому что он состоит из трех сегментов,
а от начального узла до конечного можно добраться
все го за два сегмента.

 В предыдущей главе мы использовали поиск в ширину
для нахождения кратчайшего пути между двумя точками.
Тогда под «кратчайшим путем» понимался
путь с минимальным количеством сегментов.
С другой стороны, в алгоритме Дейкстры
каждому сегменту присваивается число (вес),
а алгоритм Дейкстры находит путь с наименьшим суммарным весом.

 На всякий случай повторим: алгоритм Дейкстры состоит из четырех шагов:

1. Найти узел с наименьшей стоимостью (то есть узел,
до которого можно добраться за минимальное время).

2. Проверить, существует ли более дешевый путь к соседям этого узла,
и если существует, обновить их стоимости.

3. Повторять, пока это не будет сделано для всех узлов графа.

4. Вычислить итоговый путь (об этом в следующем разделе!).


 Терминология

 Я хочу привести еще несколько примеров применения алгоритма Дейкстры.
Но сначала стоит немного разобраться с терминологией.
Когда вы работаете с алгоритмом Дейкстры,
с каждым ребром графа связывается число, называемое весом.

 Граф с весами называется взвешенным графом.
Граф без весов называется невзвешенным графом.

 Для вычисления кратчайшего пути в невзвешенном графе
используется поиск в ширину. Кратчайшие пути во взвешенном графе
вычисляются по алгоритму Дейкстры.
В графах также могут присутствовать циклы:

 Это означает, что вы можете начать с некоторого узла,
перемещаться по графу, а потом снова оказаться в том же узле.
Предположим, вы ищете кратчайший путь в графе, содержащем цикл.

 Есть ли смысл в перемещении по циклу?
Что ж, вы можете использовать путь без прохождения цикла:

 А можете пройти по циклу

 Вы в любом случае оказываетесь в узле А, но цикл добавляет лишний вес.
Вы даже можете обойти цикл дважды, если вдруг захотите.

 Но каждый раз, когда вы проходите по циклу,
вы только увеличиваете суммарный вес на 8.
Следовательно, путь с обходом цикла никогда не будет кратчайшим.

 Наконец, вы еще не забыли наше обсуждение направленных
и ненаправленных графов из главы 6?

 Само понятие ненаправленного графа означает,
что каждый из двух узлов фактически ведет к другому узлу. А это цикл!

 В ненаправленном графе каждое новое ребро добавляет еще один цикл.
Алгоритм Дейкстры работает только с направленными ациклическими графами,
которые нередко обозначаются сокращением DAG (Directed Acyclic Graph).


 История одного обмена

 Но довольно терминологии, пора рассмотреть конкретный пример! Это Рама.
Он хочет выменять свою книгу по музыке на пианино.

 «Я тебе дам за книгу вот этот постер, - говорит Алекс. -
Это моя любимая группа Destroyer. Или могу дать за книгу
редкую пластинку Рика Эстли и еще $5». - «0, я слышала,
что на этой пластинке есть отличные песни, - говорит Эми. -
Готова отдать за постер или пластинку мою гитару или ударную установку».

 "Всю жизнь мечтал играть на гитаре, - восклицает Бетховен. -
Слушай, я отдам тебе своё пианино за любую из вещей Эми".

 Прекрасно! Рама с небольшими дополнительными тратами может поменять
свою книгу на настоящее пианино. Теперь остается понять,
как ему потратить наименьшую сумму на цепочке обменов.
Изобразим полученные им предложения в виде графа:

 Узлы графа - это предметы, на которые может поменяться Рама.
Беса ребер представляют сумму доплаты за обмен. Таким образом,
Рама может поменять постер на гитару за $30
или же поменять пластинку на гитару за $15.
Как Раме вычислить путь от книги до пианино,
при котором он потратит наименьшую сумму?
На помощь приходит алгоритм Дейкстры!
Вспомните, что алгоритм Дейкстры состоит из четырех шагов.
В этом примере мы выполним все четыре шага,
а в конце будет вычислен итоговый путь.

 Прежде чем начинать, необходимо немного подготовиться.
Постройте таблицу со стоимостями всех узлов.
(Стоимость узла определяет затраты на его достижение.)

 Таблица будет обновляться по мере работы алгоритма.
Для вычисления итогового пути в таблицу
также необходимо добавить столбец «родителм.

 Вскоре я покажу, как работает этот столбец.
А пока просто запустим алгоритм.

 Шаг 1: найти узел с наименьшей стоимостью.
В данном случае самый дешевый вариант обмена с доплатой $0 - это постер.
Возможно ли получить постер с меньшими затратами?
Это очень важный момент, хорошенько подумайте над ним.
Удастся ли вам найти серию обменов,
при которой Рама получит постер менее чем за $0?
Продолжайте читать, когда будете готовы ответить на вопрос.
Правильный ответ: нет, не удастся. Так как постер является
узлом с наименъшей стоимостъю, до которого может добратъся Рама,
снизить его стоимость невозможно. На происходящее можно взглянуть иначе:
предположим, вы едете из дома на работу.

 Если вы выберете путь к школе, э то займет 2 минуты.
Если вы выберете путь к парку, это займет 6 минут.
Существует ли путь, при котором вы выбираете путь к парку
и оказываетесь в школе менее чем за 2 минуты?
Это невозможно, потому что тол ько для того,
чтобы попасть в парк, потребуется более 2 минут.
С другой стороны, можно ли найти более быстрый путь в парк? Да, можно.

 В этом заключается ключевая идея алгоритма Дейкстры:
в графе ищется путъ с наименъшей стоимостъю.
Пути к этому узлу с менъшими затратами не существует!

 Возвращаемся к музыкальному примеру.
Вариант с постером обладает наименьшей стоимостью.

 Шаг 2: Вычислить, сколько времени потребуется для того,
чтобы добраться до всех его соседей (стоимость).

 Стоимости бас-гитары и барабана заносятся в таблицу.
Они были заданы при переходе через узел постера,
поэтому постер указывается как их родитель. А это означает,
что для того, чтобы добраться до бас-гитары,
вы проходите по ребру от постера; то же самое происходит с барабаном.

 Снова шаг 1: пластинка - следующий по стоимости узел ($5).

 Снова шаг 2: обновляются значения всех его соседей.

 Смотрите, стоимости барабана и гитары обновились! Это означает,
что к барабану и гитаре дешевле перейти через ребро,
идущее от пластинки. Соответственно,
пластинка назначается новым родителем обоих инструментов.

 Следующий по стоимости узел - бас-гитара. Обновите данные его соседей.

 Хорошо, мы наконец-то вычислили стоимость для пианино
при условии обмена гитары на пианино. Соответственно,
гитара назначается родителем. Наконец,
задается стоимость последнего узла - барабана.

 Оказывается, Рама может получить пианино еще дешевле,
поменяв ударную установку на пианино.
Таким образом, самая дешевая цепочка обменов обойдется Раме в $35.

 Теперь, как я и обещал, необходимо вычислить итоговый путь.
К этому моменту вы уже знаете, что кратчайший путь обойдется в $35,
но как этот путь определить? Для начала возьмем родителя узла «пианино».

 В качестве родителя узла «пианино» указан узел «барабан».

 А в качестве родителя узла «барабан» указан узел «пластинка».

 Следовательно, Рама обменивает пластинку на барабан.
И конечно, в самом начале он меняет книгу на пластинку.
Проходя по родительским узлам в обратном направлении,
мы получаем полный путь.

 Серия обменов, которую должен сделать Рама, выглядит так:

 книга -> пластинка

 пластинка -> барабан

 барабан -> пианино

 До сих пор я использовал термин «кратчайший путь»
более или менее буквально, понимая под ним вычисление
кратчайшего пути между двумя точками или двумя людьми.
Надеюсь, этот пример показал, что кратчайший путь
далеко не всегда связывается с физическим расстоянием:
он может быть направлен на минимизацию какой - либо характеристики.
В нашем примере Рама хотел свести к минимуму свои затраты при обмене.
Спасибо Дейкстре!
"""
