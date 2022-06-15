# Урок 16: Методы списков (массивов)

# list.append(x)	Добавляет элемент в конец списка
# list.extend(L)	Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x)	Вставляет на i-ый элемент значение x
# list.remove(x)	Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i])	    Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]])	Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x)	    Возвращает количество элементов со значением x
# list.sort([key=функция])	Сортирует список на основе функции
# list.reverse()	Разворачивает список
# list.copy()	    Поверхностная копия списка
# list.clear()	    Очищает список
# Информация с ресурса: https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html

l = [1, 2, 3, 'Hello', ['test', 10], 'world', True]
names = ['Иванов', 'Петров', 'Сидоров']

# print(names[1])   # Результат: Иванов
# print(l[4][0])    # Результат: test
# print(len(l))     # Результат: кол-во элементов массива
# print(l[0:3])     # Диапазон вывода значений списка

l[2] = 'world'
# l[:2] = [10, 15]

l.append('new')
l.extend([5, 7])
l2 = ['hi', 19]
l += l2
l.insert(1, 'test')
# l.remove('world')
# el = l.pop()
# l.sort()
l3 = ['hello', 'hi', 'David', 'world', 'test']
# l3.sort()
# l3 = sorted(l3)
print(l, l.count('test'), l3, sep='\n')
# print('h' > 'a')