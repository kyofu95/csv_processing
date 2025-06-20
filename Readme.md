## Реализация скрипта для обработки CSV-файла.

Поддерживаемые операции:
- Фильтрация. Поддерживаются операторы 'больше', 'меньше' и 'равно'
- Агрегация. Поддерживаются функции 'минимум(min)', 'максимум(max)' и 'среднее значение(avg)'
- Сортировка. Поддерживаются 'восходящая(asc)' и 'нисходящая(desc)'
Скрипт написан таким образом, чтобы можно было быстро добавить новые операторы фильтрации или функции агрегации.
В скрипте реализована обработка ошибок, включая обработку пользовательских ошибок.

Проект написан на Python 3.12, тесты требуют `pytest`. В проекте используется `poetry`, для удобства зависимости экспортированы в requirements.txt.



## Работа со скриптом:
Скрипт вызывается следующим образом:
```sh
python3 main.py
```
По умолчанию это покажет помощь по работе аргументов.

<br>

Для работы с CSV файлом нужно указать имя файла с аргументом `--file`:
```sh
python3 main.py --file products.csv
```
<details>
<summary>Скриншот примера работы</summary>
<br>

![all.jpg](/.github/all.jpg?raw=true)
</details>

<br>

Скрипт так же поддерживает следующие аргументы:

Фильтрация, с аргументом `--where`:
```sh
python3 main.py --file products.csv --where "rating>4.5"
```
Поддерживаются операторы `=`, `>` и `<`
<details>
<summary>Скриншот примера работы фильтрации</summary>
<br>

![all.jpg](/.github/filter.jpg?raw=true)
</details>

<br>

Агрегация, с аргументом `--aggregate`:
```sh
python3 main.py --file products.csv --aggregate "rating=min"
```
Поддерживаются функции `min`, `max` и `avg`
<details>
<summary>Скриншот примера работы аггрегации</summary>
<br>

![all.jpg](/.github/aggregate.jpg?raw=true)
</details>

<br>

Сортировка, с аргументом `--order-by`:
```sh
python3 main.py --file products.csv --order-by "rating=desc"
```
Поддерживаются направления `asc` и `desc`
<details>
<summary>Скриншот примера работы сортировки</summary>
<br>

![all.jpg](/.github/sorting.jpg?raw=true)
</details>
