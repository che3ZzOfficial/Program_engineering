# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
numbers = [1,2,3,4,6,8,9]
value = int(input('Введите значение переменной: '))
if value in numbers:
    print('Переменная есть в данном массиве')
else:
    print('Переменной нет в этом массиве')