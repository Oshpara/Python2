# Урок 24: Методы словаря

# dict.clear() - очищает словарь.
# dict.copy() - возвращает копию словаря.
# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
# dict.items() - возвращает пары (ключ, значение).
# dict.keys() - возвращает ключи в словаре.
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# dict.values() - возвращает значения в словаре.

product1 = {'title': 'Sony', 'price': 100}

# print(product1.items())
# print(product1.keys())
# print(product1.pop('title2', 'No'))
# print(product1.popitem())

print(product1)
# print(product1.setdefault('title2', 'test'))
product1.update({'test': 'value'})
product1.update({'price': 200})
print(product1)

print(product1.values())