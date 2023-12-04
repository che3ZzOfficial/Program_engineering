# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Деревянкин Владислав Владимирович
- ОЗИВТ(ППК)-22-2-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/362ca4d0-6618-482f-b194-0597df558293)

## Выводы

В папку где были .py файлы закинул текстовый файл.

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('qwe.txt', 'r')
print(f.readline())
f.close()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/f0d996a6-cebb-4678-a2db-e9d638fc01a9)

## Выводы

Написали программу где выведет только первую строку из текстового файла.

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('qwe.txt', 'r')
print(f.readlines())
f.close()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/5e400eab-0e9f-41a5-917f-7fc3e97e10a7)


## Выводы

Написали программу где выведет все строки из текстового файла.


## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('qwe.txt') as f:
	print(f.readlines())
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/c32a2363-4011-423d-9540-d4795efa5ab6)

## Выводы

Написали программу где выведет все строки файла в массиве.

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('qwe.txt') as f:
	for line in f:
		print(line)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/5d5dd37a-b779-4d08-b6c2-7e61c8f4fe4a)

## Выводы

Написали программу где каждая строка выводится отдельно отделяя пустрой строкой.

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('qwe.txt', 'a+') as f:
    f.write('\nAdd stroka')

with open('qwe.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/a040251d-7ac5-4369-a0cb-f52cee42f65f)

## Выводы

Теперь в сам файл мы добавляем новую строку с названием.

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из
произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('qwe.txt', 'w') as f:
    for line in lines:
        f.write('\n Cycle Run ' + line)
    print('Done!')
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/89a72940-5f1a-4c56-a5ce-147749f2d5e3)

## Выводы

Очистили файл своей перепесью и написали данные из списка.

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f' {", ".join([folder for folder in catalog[1]])}')
    print(f' {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('/Usue/PyCharm/Tema_7/lab/zad')
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/fe9da80a-afaf-4597-baca-74a3e1929805)

## Выводы

Выводим путь и содержание.

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: Приветствие Спасибо Извините Пожалуйста До свидания Ты готов? Как дела? С днем рождения! Удача! Я тебя люблю.
Требуется реализовать функцию, которая выводит слово, имеющеемаксимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/b655fb9d-77e4-4511-aa1b-c5ebab535e22)

## Выводы

В данной программе выводится самое длиное слово в файле.

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
###№ - номер по порядку (от 1 до 300);
###Секунда - текущая секунда на вашем ПК;
###Микросекунда - текущая миллисекунда на часах.
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды..

```python
import csv
import datetime
import time
from _csv import writer

with open('rows_300.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                        datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/54b1c032-a76f-4c45-a083-e4232e2a44ba)


## Выводы
Добавляет строки и столбцы в файл rows_300.csv.

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит
самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоле в котором будет указана вся необходимая информация.

```python
def main():
    with open("words.txt", encoding="utf8") as file:
        text = file.read()
        words = text.split()
        word_count = {word: words.count(word) for word in set(words)}
        max_count = max(word_count, key=word_count.get)

    print(f"Самое частое слово: {max_count}, количество: {word_count[max_count]}")

if __name__ == "__main__":
    main()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/6f87d053-b8bd-4088-9261-6894c5b50230)
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/e6334c49-2ade-4906-8f1b-1ffe4ab884e1)

## Выводы

Сделали отчёт по статье где видно количество слов в ней и самое часто встречающееся слово.

## Самостоятельная работа №2
### У вас появилась потребность в ведение книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не
устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию
о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом
выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def read_data():
    try:
        with open("transactions.txt", "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "wrong"

def write_data(data):
    try:
        with open("transactions.txt", "w") as file:
            file.write(data)
    except PermissionError:
        print("wrong.")

def main():
    data = read_data()
    transactions = data.split("\n")
    print("Текущие операции: ")
    for transaction in transactions:
        if transaction != "":
            print(transaction)
        else:
            pass

    while True:
        amount = input("Введите сумму расходов (Enter для выхода): ")
        if amount == "":
            break
        transactions.append(amount)
        write_data("\n".join(transactions))
        print(f"Добавлена расход:  {amount}")

if __name__ == "__main__":
    main()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/572fd041-5bfe-40e2-9cba-b36929132205)

## Выводы

Сделали сохранение файла и добавление в него данных.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 
### Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
### Ожидаемый результат:
Input file contains:
108 letters
20 words
4 lines

```python
def main():
    filename = 'input.txt'
    letters, words, lines = 0, 0, 0
    with open(filename, 'r') as file:
        for line in file:
            letters += len(line)
            words += len(line.split())
            lines += 1
    print(f'Input file contains:\n{letters} letters\n{words} words\n{lines} lines')

if __name__ == '__main__':
    main()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/a71360c2-47ed-4ac3-ba5b-30044b2532c8)

## Выводы

Посчитали в программе статистику по тексту.
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в
слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить
запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam,
Exam, ExaM, EXAM и exAm должны быть заменены на ****.
### Запрещенные слова:
hello email python the exam work is
### Предложение для проверки:
Hello, world! Python IS the programming language of thE future. My
EMAIL is…
PYTHON is awesome!!!!
•Ожидаемый результат:
***** ***Id! ****** ** *** programming language of *** future. My
***** **
****** **
awesome!!!!
```python
def censor_text(sentence, banned_words):
    censored_sentence = sentence
    for word in banned_words:
        pattern = re.compile(r'\b' + word + r'\b', re.IGNORECASE)
        censored_sentence = re.sub(pattern, '*' * len(word), censored_sentence)
    return censored_sentence

def load_banned_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        banned_words = file.read().split()
    return banned_words

def main():
    banned_words = load_banned_words('qwe.txt')
    sentence = input("Введите предложение: ")
    censored_sentence = censor_text(sentence, banned_words)
    print("Цензурированное предложение:")
    print(censored_sentence)

if __name__ == "__main__":
    main()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/63528818-0405-4741-8bb8-860a13c76669)

## Выводы

Зацензурили.
  
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом. Программа для подсчета символов в текстовом файле.

```python
with open('qwe.txt', 'r', encoding='utf-8') as file:
    # Считываем все строки из файла
    lines = file.readlines()
character_count = 0
for line in lines:
    character_count += len(line)
print(f'В файле "qwe.txt" {character_count} символов.')
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/df1ba325-9a9d-462f-a691-009c4207295b)

  
## Выводы

В этой задаче я взял посчитать количество символов в файле.

## Общие выводы по теме
Простое взаимодействие с файлами.Пригодится для нейронок.
