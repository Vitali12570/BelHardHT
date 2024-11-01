#1
total_guests = int(input('Введите кол-во гостей: '))
if total_guests > 50:
    print('Ресторан')
elif 50 >= total_guests >= 20:
    print('Кафе')
elif 20 > total_guests >= 1:
    print('Дом')


#2
rub = int(input('Введите кол-во рублей: '))
coins = int(input('Введите кол-во копеек: '))
text_rub = 'рублей'
text_coins = 'копеек'

if coins >= 100:
    rub += coins // 100
    coins = coins % 100

rub_last_dig = rub % 10
coins_last_dig = coins % 10

if rub_last_dig == 1:
    text_rub = 'рубль'
if 4 >= rub_last_dig >= 2:
    text_rub = 'рубля'

if 20 >= rub % 100 >= 10:
    text_rub = 'рублей'

if coins_last_dig == 1:
    text_coins = 'копейка'
if 4 >= coins_last_dig >= 2:
    text_coins = 'копейки'

if 20 >= coins % 100 >= 10:
    text_coins = 'копеек'

print(f'{rub} {text_rub}, {coins} {text_coins}')