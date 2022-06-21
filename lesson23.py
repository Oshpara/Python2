# Урок 23: Словари

d = {}
product1 = {            # для читабельности использовать такую структуру записи
    'title': 'Sony',
    'price': 100
}

product2 = dict(title='iPhone', price=110)

print(d)
print(product1)
print(product2)

# преобразование списка в словарь

users = [
    ['bob@gmail.com', 'Bob'],
    ['Katy@gmail.com', 'Katy'],
    ['john@gmail.com', 'john']
]
d_users = dict(users)
print(users)
print(d_users)

# преобразование картежа в словарь

users_t = (
    ('bob@gmail.com', 'Bob'),
    ('Katy@gmail.com', 'Katy'),
    ('john@gmail.com', 'john')
)
t_users = dict(users_t)
print(users_t)
print(t_users)

# Создание словаря с однотипными значениями

product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
print(product3)

nums = {i: i + 1 for i in range(1, 10)}
print(nums)

# Получение значений из словаря

product1_1 = {'title': 'Sony', 'price': 100}
product2_2 = dict(title='iPhone', price=110)
nums1 = {i: i + 1 for i in range(1, 10)}

print(product1_1['title'])
print(product2_2['price'])
# print(nums1['1'])           # Будет ошибка, т.к. в nums значение типа int, а запрос в типе str
print(nums1.get('1'))         # Вместо ошибки выйдет None. Можно задать значение на вывод вместо ошибки: get('1', 'No')

# Вывод всех значений словаря

for key in product1_1:
    print(f'{key}: {product1_1[key]}')

# print(product1_1.items())
for key, value in product1_1.items():   # Альтернативный вариант
    print(key, value)

# Создание и вывод списка словарей
products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]
print(products)

for product in products:
    print(product['title'], product['price'])