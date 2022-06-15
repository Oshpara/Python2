# s = r'C:\d\new.txt'   # знак r - перед опострафами объявляет строку сырой (Питон не станет обрабатывать экранирующую последовательность)
# print(s)

# s = 'Py' 'thon'
# print(s)

# s1 = 'Hello, '
# s2 = 'world!'
# s3 = s1 + s2
# print(s3)

# name = 'John'
# age = 20
# print('My name is ' + name + " I'm " + str(age))

# print('Hi ' * 5)

# s = 'Hello world!'
# print(s[0])
# print(s[-12])
# s[0] = 'D'            # невозможно менять значение символа в строке, питон выдаст ошибку

s = 'Hello world!'
print(s[0:12])          # Hello world!
print(s[-1])            # !
print(s[0:5])           # Hello
print(s[:5])            # Hello
print(s[6:])            # world! (Получение строки начиная с символа 6 и до конца строки)
print(s[::2])           # Hlowrd (Получение символов строки с шагом 2
print(s[::-1])          # !dlrow olleH (Строка наоборот)
print(s[:5] + s[6:])    # Helloworld! (Сложение выбраных последовательностей символов)