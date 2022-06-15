RUB = int(input('Сколько денег дашь?'))
USD = 61.47
EUR = 63.66
JPY = 0.4768
currency = str(input('В какую валюту конвертировать USD,EUR или JPY?'))

if currency == 'USD':
    print(f'Ваши сбережения в долларах {RUB / USD:.2f}')
elif currency == 'EUR':
    print(f'Ваши сбережения в Евро {RUB / EUR:.2f}')
elif currency == 'JPY':
    print(f'Ваши сбережения в японских йенах {RUB/JPY:.2f}')
else:
    print('Такой валюты нет')
