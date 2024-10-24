#3
firstname = str(input('Введите ваше имя: '))
lastname = str(input('Ведите вашу фамилию: '))
age = int(input('Введите ваш возраст: '))
print(f'Привет, меня зовут {firstname} {lastname},мне {age} лет')
#4
my_str = f'Привет, меня зовут {firstname} {lastname},мне {age} лет'
print('3 символ строки:',my_str[2])
#5
print('Предпоследний символ строки:',my_str[-2])
#6
print('Первые пять символов строки:',my_str[0:5:1])
#7
print('Строка без последних 2 символов:', my_str[0:-2:1])
#8
some_str = 'Hello, World!'
print(some_str.replace('Hello',f'{firstname}'))
