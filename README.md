Софт для получения открытых данных из проекта
http://115.бел от граждан для граждан. Присоединиться:

* telegram: https://t.me/Minsk_115

Софт является [общественным достоянием](https://github.com/opendataby/115/blob/gh-pages/UNLICENSE).

### Данные

Исходный json и полученные из него csv вместе с итоговым
.zip архивом находятся на сайте https://115.netlify.com/ и
обновляются
[автоматически](https://app.netlify.com/sites/115/deploys).

Чтобы запустить на своей машине, нужен Python3 и bash.
Cкачать исходники и запустить

    ./go.sh

Ещё можно запустить все питон скрипты по порядку.

### Как работает автообновление

Репозиторий связан с сервисом https://netlify.com
который предоставляет хостинг для статических сайтов,
и может запускать скрипты для сборки контента, такие
как `go.sh`. Сборка запускается при любом изменении в
репозитории.

### Теория - Сферический парсер в вакууме

Получение открытых данных обычно требует одного шага
- скачать. В остальных случаях шагов будет несколько.
В виде схемы, pipeline получения и трансформации данных:

    +--------+    +---------+    +---------+
    | Order  |--->| Fetch   |--->| Parse   |--->
    +--------+    +---------+    +---------+    

    +--------+    +---------+    +---------+
    | Map    |--->| Norm    |--->| Export  |--->
    +--------+    +---------+    +---------+    

    +--------+    +---------+    +---------+
    | Read   |--->| Build   |--->| Render  |
    +--------+    +---------+    +---------+    

* 001 - Order - подготовка списка ссылок
* 002 - Fetch - получение страничек
* 003 - Parse - извлечение данных из содержимого


* 004 - Map   - привязка данных к полям
* 005 - Norm  - приведение значений к нормальному виду
* 006 - Export - экспорт датасета в нужный формат


* 007 - Read  - чтение машиночитабельного датасета
* 008 - Build - обработка
* 009 - Render - визуализация

В парсере 115.бел каждый шаг - это питоновский файл с
соответствующим номером. Какие-то шаги не нужны или
объединены вместе. Данные между шагами передаются
также в файлах с соответствующими номерами.


---

### Для исследователей данных: описание датасета.

**Описание**:
115.bel: качество работы коммунальных служб, служб озеленения, и других городских сервисов Минска и Витебска за 2016-2017гг.
Статистика работы электронного центра обработки заявок от пользователей, показываются все решённые/нерешённые заявки по месяцам и районам, рейтинг организаций ЖКХ Минска.

В датасете используются данные портала электронных обращений по коммунальным вопросам Минска и Витебска 115.бел, показывается количество решённых в срок и нерешённых, а также решённых после срока заявок и оценки пользователей в среднем по всем заявкам с ноября 2015 по июль 2017 года. Оценки в датасете выставлены за 22806 заявок на портале 115.бел. Всего на 01.01.2017 на портале 46 072 заявок от 25 157 пользователей, из них решено 41 832 заявок. На 01 апреля 2017г было 63543 заявок от почти 40 000 пользователей.

Открытые вопросы для хакатонов (примеры): улучшается ли качество обслуживания со временем, как влияет электронная обработка запросов на качество услуг, с чем связан гендерный перекос (намного активнее оставляют заявки мужчины), какие районы Минска обслужены лучше, а какие - хуже, и почему, как зависит от стоимости недвижимости и года постройки дома, насколько хорошо справляются со своей работой частные ЖКХ организации по сравнению с государственными.

На апрель 2017г: большинство запросов, поступивших на портал в 2017 году, касаются многоквартирных домов, и кроме этого проблемы, касающиеся придворовых территорий, зелёных насаждений, велодорожек, рекламы, вывоза мусора и т.п.

Более 70 % запросов выполняются в течение 7,45 календарного дня (норматив - до 11 суток максимум, т.е. до 8 суток после 72 часов модерации). На контроле остаются запросы, связанные с наличием выбоин на проезжей части, брошенными автомобилями и техническим состоянием покрытий пешеходных дорожек и парковок.

В рейтинге районов по исполнению запросов лидирует Советский район, а на последнем месте (большинство заявок не решены или не решены не в срок- Центральный район Минска).

Возраст основных пользователей портала 115.бел составляет 25–34 года. За 2017г значительно выросло число заявителей-женщин. Если в октябре 2016 года они составляли до 20 %, то в марте 2017-го — 52 %.

Дополнительные ссылки:
1) другие городские данные по Минску:
https://opendata.by/group/1430

2) Датасет - дополнительно границы ЖЭСов Минска в json (данные могли устареть, т.к. используется датасет за 2014г)
https://opendata.by/node/493

3) Датасет - годы постройки жилых домов в Минске (жилищный фонд - выборочный сэмпл из 7000 домов во всех районах), 2010-2015
https://opendata.by/node/372

4) Дополнительно: рейтинг организаций, осуществяющих выполнение заявок пользователей:  https://115.бел/rating

### Нужные функции, которые хотелось бы добавить в скрипт

На данном этапе приоритет - добавить в скрипт по возможности 
- описания проблем
- добавлено: человеческая расшифровка статуса задач, категорий (доступна легенда: )
- в системе появились: Кричев, Солигорск, десятки других городов. коды городов записаны в задачах на гитхабе
- багфиксы?
- делаем дэшборд: https://app.powerbi.com/view?r=eyJrIjoiYThhZDc4ZTEtY2FmMy00NzAxLTg2ODQtZGQ4OTJkODExMGVlIiwidCI6IjBhYWNjZmQ4LTM4M2ItNGU4Yy1hNmM0LTM5OTZhOGI5NzE3OCIsImMiOjl9
- анализируем дэшборд!
- добавились в систему 01.08.2018:  Берестовица, Волковыск, Вороново, Зельва, Кричев, Щучин
- 01.09.2018 портад ЖКХ 115.бел заработал в Гродно, районах Гродненской области и Бресте
- Витебские данные (на 04.12.2017 по Витебску: ПРИНЯТЫЕ ЗАПРОСЫ: 2 812, ПРОБЛЕМ РЕШЕНО: 502). Now, 18.05.2018: ПРИНЯТЫЕ ЗАПРОСЫ
4 830, ПРОБЛЕМ РЕШЕНО 1 157)
- обнаружен баг - парсер выдаёт пустые файлы джейсон за некоторые месяцы (часть проблемы в том, что 115.бел чистит БД https://github.com/opendataby/115/issues/17). Получить данные можно или постоянной архивацией или опросом базы по ID.

- всего на середину июня 2017 - 82585 строк в результатах, а должно быть около 120 000. Пробуем пересклеить старые архивные копии, чтобы найти потерянные заявки. Склеили, добавили архивные ЦСВ. Склеили, добавили айди, чистим дубли.

- В ЦСВ добавлены айди организаций. https://github.com/opendataby/115/issues/16

- Расшифровки в качестве легенды добавлены в отдельный CSV https://115.netlify.com/organizations.csv

- анализируем количество заявок по месяцам: https://github.com/opendataby/115/issues/11

- Найдена офиц. статистика - С 1 января по 29 мая 2018 года на портале «Мой Горад» 115.бел:
— принято запросов — 34 932;
— отклонено — 4 474;
— выполнено — 21 950;
— активных пользователей (которые отправили хотя бы один запрос) — 11 153.
Всего зарегистрировано 61 923 пользователя.
По многоквартирным домам 4 901 человек отправил 11 856 запросов.

Район Минска	Всего с начала года	Выполнено с начала года	Отклонено
Советский	3 263	2 178	350
Заводской	3 661	2 446	476
Первомайский	3 980	2 478	400
Партизанский	1 821	1 135	207
Фрунзенский	7 918	5 054	897
Центральный	2 771	1 638	310
Московский	4 734	2 865	533
Октябрьский	3 134	2 038	288
Ленинский	3 058	2 113	330
https://minsknews.by/sotrudniki-portala-115-bel-mnogie-minchane-oshibochno-otozhdestvlyayut-nas-so-sluzhboy-prinimayushhey-zvonki-po-nomeru-115/


