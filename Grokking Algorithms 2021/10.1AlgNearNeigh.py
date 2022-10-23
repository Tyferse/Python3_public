# Алгоритм k ближайших соседей

"""
 Построение рекомендательной системы

 Представьте, что вы работаете на сайте NetЛix
и хотите построить систему, которая будет рекомендовать фильмы
для ваших пользователей. На высокомуровне эта задача
похожа на задачу с гр е йпфрутами!
Информация о каждом пользователе наносится на график.

 Положе ние пол ьз ователя определя ется его в кусами,
поэтому пользователи с похожими вкусами располагаются недалеко
друг от друга. Предположим, вы хотите порекомендовать фильмы Приянке.
Найдите пять пользователей, ближайших к ней.

 У Джастина, Джей-Си, Джозефа, Ланса и Криса похожие вкусы. Значит,
те фильмы, которые нравятся им,
с большой вероятностью понравятся и Приянке!

 После того как у вас появится такая диаграмма,
построить рекомендательную систему будет несложно.
Если Джастину нравится какой-нибудь фильм,
порекомендуйте этот фильм Приянке.

  1. Джастин смотрит фильм -> 2. Ему понравился фильм ->
  -> 3. Рекомендуем этот фильм Приянке


 Извлечение признаков

 В примере с грейпфрутами мы сравнивали фрукты на основании их размера
и цвета кожуры. Размер и цвет - признаки, по которым ведется сравнение.
Теперь предположим, что у вас есть три фрукта.
Вы можете извлечь из них информацию,
то есть провести извлечение признаков.

 Данные трех фруктов наносятся на график.

 Из диаграммы хорошо видно , что фрукты А и В похожи.
Давайте измерим степень их сходства.
Для вычисления расстояния между двумя точками
применяется формула Пифагора.

  sqrt((x1-x2)**2 + (y1-y2)**2)

 Например , расстояние между А и В вычисляется так:

  sqrt((2-2)**2 + (2-1)**2)

  = sqrt(0 + 1)

  = sqrt(1)

  = 1

 Расстояние между А и В равно 1.
Другие расстояния вычисляются аналогично.

 Формула расстояния подтверждает то, что мы видим:
между фруктами Аи В есть сходство. Допустим,
вместо фруктов вы сравниваете пользователей Netflix.
Пользователей нужно будет как-то нанести на график. Следовательно,
каждого пользователя нужно будет преобразовать в координаты - так же,
как это было сделано для фруктов.

 Когда вы сможете нанести пользователей на график,
вы также сможете из мерить расстояние между ними.

 Начнем с преобразования пользователей в набор чисел.
Когда пользователь регистрируется на Netflix,
предложите ему оценить несколько категорий фильмов:
нравятся они лично ему или нет.
Таким образом у вас появляется набор оценок для каждого пользователя!

 Приянка и Джастин обожают мелодрамы и терпеть не могут ужасы.
Морфеусу нравятся боевики, но он не любит мелодрамы
(хороший боевик не должен прерываться слащавой романтической сценой).
Помните, как в задаче об апельсинах и грейпфрутах
каждый фрукт представлялся двумя числами?
Здесь каждый пользователь представляется набором из пяти чисел.

 Математик скажет, что вместо вычисления расстояния в двух измерениях
вы теперь вычисляете расстояние в пяти измерениях.
Тем не менее формула расстояния остается неизменной.

  sqrt((a1-a2)**2 + (b1-b2)**2 + (c1-c2)**2 + (d1-d2)**2 + (e1-e2)**2)

 Просто на этот раз используется набор из пяти чисел вместо двух.
Формула расстояния универсальна: даже если вы используете набор
из миллиона чисел, расстояние вычисляется по той же формуле.
Естественно спросить: какой смысл передает метрика расстояния
с пятью числами? Она сообщает, насколько близки между собой
эти наборы из пяти чисел.

  sqrt((3-4)**2 + (4-3)**2 + (4-5)**2 + (1-1)**2 + (4-5)**2)

  = sqrt(1 + 1 + 1 + 0 + 1)

  = sqrt(4)

  = 2

 Это расстояние между П риянкой и Джастином.

 Вкусы Приянки и Джастина похожи. А насколько различаются
вкусы Приянки и Морфеуса? Вычислите расстояние между ними,
прежде чем продолжить чтение.

 Сколько у вас получилось? Приянка и Морфеус находятся на расстоянии 24.
По этому расстоянию можно понять,
что у Приянки больше общего с Джастином, чем с Морфеусом.

 Прекрасно! Теперь порекомендовать фильм Приянке будет несложно:
если Джастину понравился какой-то фильм, мы рекомендуем его Приянке,
и наоборот. Вы только что построили систему, рекомендующую фильмы.

 Если вы являетесь пользователем Netflix,
то Netflix постоянно напоминает вам:
«Пожалуйста, оценивайте больше фильмов. Чем больше фильмов вы оцените,
тем точнее будут наши рекомендации~. Теперь вы знаете почему:
чем больше фильмов вы оцениваете, тем точнее Netflix определяет,
с какими пользователями у вас общие вкусы.


 Упражнения

 10.1 В примере с Netflix сходство между двумя пользователями
оценивалось по формуле расстояния. Но не все пользователи
оценивают фильмы одинаково. Допустим, есть два пользователя,
Йоги и Пинки, вкусы которых совпадают.
Но Йоги ставит 5 баллов любому фильму, который ему понравился,
а Пинки более разборчива и ставит "пятерки" только самым лучшим фильмам.
Вроде бы вкусы одинаковые, но по метрике расстояния
они не являются соседями. Как учесть различия
в стратегиях выставления оценок?
 Ответ: Можно воспользоваться нормализацией: вы вычисляете среднюю
оценку для каждого человека и используете ее для масштабирования
оценок. Если пользователь очень часто ставит "пятёрки",
можно на уровне программы немного занижать эти оценки,
чтобы эти рекомендации лучше сооответствовали
и среднее расстояние между пользователями было меньше.

 10.2 Предположим, Netflix определяет группу "авторитетов". Скажем,
Квентин Тарантино и Уэс Андерсон относятся к числу авторитетов Netflix,
поэтому их оценки оказывают более сильное влияние,
чем оценки рядовых пользователей. Как изменить систему рекомендаций,
чтобы она учитывала повышенную ценность оценок авторитетов?
 Ответ: можно сделать так, что оценки авторитетов
будут дублироваться несколько раз, чтобы они имели больший вес
среди оценок рядовых пользователей.


 Регрессия

 А теперь предположим, что просто порекомендовать фильм недостаточно:
вы хотите спрогнозировать, какую оценку Приянка поставит фильму.
Возьмите 5 пользователей, находящихся вблизи от нее.

 Кстати, я уже не в первый раз говорю о "ближайших пяти".
В числе "5" нет ничего особенного:
с таким же успехом можно взять 2 ближайших пользователей, 10 или 10 ООО.
Поэтому-то алгоритм и называется "алгоритмом k ближайших пользователей",
а не "алгоритмом 5 ближайших пользователе й"!

 Допустим, вы пытаетесь угадать оценку Приянки для фильма «Идеальный
голос». Как этот фильм оценили Джастин, Джей-Си, Джозеф, Ланс и Крис?

 Если вычислить среднее арифметическое их оценок , вы получите 4,2.
Такой метод прогнозирования называется регрессией.
У алгоритма k ближайших соседей есть два основных применения:
классификация и регрессия:

  классификация = распределение по категориям;

  регрессия = прогнозирование ответа (в числовом выражении).

 Регрессия чрезвычайно полезна. Представьте,
что вы открыли маленькую булочную в Беркли
и каждый день выпекаете свежий хлеб. Вы пытаетесь предсказать,
сколько буханок следует испечь на сегодня. Есть несколько признаков:

  погода по шкале от 1 до 5 ( 1 = плохая, 5 = отличная);

  праздник или выходной? ( 1, если сегодня праздник или выходной,
 О в противном случае);

  проходят ли сегодня спортивные игры? (1 =да , О= нет).

 И вы знаете, сколько буханок хлеба было продано в прошлом
при разных сочетаниях признаков.

  A. (5, 1, 0) = 300 буханок B. (3, 1, 1) = 225 буханок
  C. (1, 1, 0) = 75 буханок  D. (4, 0, 1) = 200 буханок
  E. (4, 0, 0) = 150 буханок F. (2, 0, 0) = 50 буханок

 Сегодня выходной и хорошая погода. Сколько буханок вы продадите
на основании только что приведенных данных?
Используем алгоритм k ближайших соседей для k = 4.
Сначала определим четырех ближайших соседей для этой точки.

  (4, 1, 0) = ?

 Ниже перечислены расстояния. Точки А, В, D и Е являются ближайшими.

 A. 1 < B. 2 <
 C. 9   D. 2 <
 E. 1 < F. 5

 Вычисляя среднее арифметическое продаж в эти дни, вы получаете 218,75.
Значит, именно столько буханок нужно выпекать на сегодня!


 Близость косинусов

 До сих пор мы использовали формулу расстояния
для вычисления степени сходства двух пользователей.
Но является ли эта формула лучшей? На практике также часто применяется
метрика близости косинусов. Допустим, два пользователя похожи,
но один из них является более консервативным в своих оценках.
Обоим пользователям понравился фильм Монмохана Десан
"Амар Акбар Антони". Пол поставил фильму оценку 5 звёзд,
но Роуэн оценил его только в 4 звезды.
Если использовать формулу расстояния,
эти два пользователя могут не оказаться соседями,
несмотря на сходство вкусов.

 Метрика близости косинусов не измеряет расстояние
между двумя векторами. Вместо этого она сравнивает углы двух векторов
и в целом лучше подходит для подобных случаях. Тема близости косинусов
выходит за рамки этой книги, но вам стоит
самостоятельно поискать информацию о ней, если вы будете применять
алгоритм k ближайших соседей.
"""
