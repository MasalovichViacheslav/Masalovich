"""
Задача №1
1.	Вводится натуральное число n. Для этого числа вычислите n-ое число Фибоначчи и выведите сумму этого числа и его
факториала. Вычисление числа Фибоначчи и факториала вынесите в отдельные функции factorial(n) и fib(n). Считайте первое
число Фибоначчи равным единице.
"""
# n = int(input('Введите нарутально число n:'))
#
#
# def fib_numb(par):
#     numb1, numb2 = 1, 1
#     for i in range(par - 1):
#         numb1, numb2 = numb2, numb1+numb2
#     # print(f'n-ое число Фибоначчи - {numb1}')
#     return numb1
#
#
# def fib_numb_fact(fun):
#     factorial = 1
#     for x in range(1, fun + 1):
#         factorial *= x
#     # print(f'factorial - {factorial}')
#     return factorial
#
#
# print(f'Сумма n-го числа Фиббоначи и его факториала равна {fib_numb_fact(fib_numb(n)) + fib_numb(n)}')
"""
Задача 2
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую 
самое маленькое целое число y, такое что:
-y больше или равно x   
-y делится нацело на 5:
x 6 -> 10, x 15 -> 15
"""
# def closest_mod_5(x):
#     if x % 5 == 0:
#         y = x
#     else:
#         y = (x + 5) // 5 * 5
#     return y
#
#
# # print(closest_mod_5(int(input('Введите значение x:'))))
"""
Задача 3
3.	В языке Python есть некоторые ограничения на имена переменных. Имена переменных:
-могут состоять только из цифр, букв и знаков подчеркивания.
-не могут начинаться с цифры.                                                   
Программист вводит строки с именами переменных. Для каждой переменной нужно вывести "Можно использовать", если ее имя 
корректно, или "Нельзя использовать", если это не так. Определив все нужные переменные, программист заканчивает ввод 
строкой "Поработали, и хватит". Для проверки каждой строки используйте функцию check_variable(v). Для простоты будем 
считать, что программист использует только латинские буквы.
"""
# # список с кодами ASCII латинских букв и нижнего подчеркивания
# first_symb_list = [numb for numb in range(65, 123) if numb <= 90 or numb == 95 or numb >= 97]
# # print(first_symb_list)
# # список с кодами ASCII цифр, латинских букв и нижнего подчеркивания
# other_symb_list = [numb for numb in range(48, 58)] + first_symb_list
# # print(other_symb_list)
#
#
# def check_variable(v: str):
#     for ind in range(1, len(v)):
#         if ord(v[0]) in first_symb_list and ord(v[ind]) in other_symb_list:
#             result = 'Можно использовать'
#         else:
#             result = 'Нельзя использовать'
#     print(result)
#
#
# while True:
#     some_str = input('Введите строку:')
#     if some_str == 'Поработали, и хватит':
#         break
#     check_variable(some_str)
"""
Задача 4
Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада 
увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты). Написать 
функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
"""
# def bank(a: float, years: int):
#     for _ in range(years):
#         a *= 1.1
#     return a
#
#
# amount = bank(float(input('Введите сумму вклада:')), int(input('Введите срок вклада:')))
# # print(amount)
"""
Задача 5.
Дана функция, которая выводит все простые числа в промежутке от 1 до 100. Написать декоратор который будет проверять 
время работы этой функции. Задекорировать функцию. Вывести время работы этой функции, а так же сами простые числа.
"""
# from datetime import datetime
#
#
# def fun_exe_time(fun):
#     def wrapper():
#         start = datetime.now()
#         fun()
#         end = datetime.now()
#         print(f'Функция simple_numbs выполнена за {(end - start).microseconds} мкс')
#     return wrapper
#
#
# @fun_exe_time
# def simple_numbs():
#     dividers = 0
#     for numb in range(2, 101):
#         for i in range(1, numb + 1):
#             if numb % i == 0:
#                 dividers += 1
#         if dividers == 2:
#             print(numb)
#         dividers = 0
#
#
# simple_numbs()
"""
Задача 6.
6.	Дана функция которая запрашивает у пользователя определённые данные для регистрации на портале и запоминает их. 
Напишите декоратор, который будет засекать время проведённое пользователем на портале при регистрации.
"""
# from datetime import datetime
#
#
# def reg_time(fun):
#     def wrapper():
#         start = datetime.now()
#         fun()
#         end = datetime.now()
#         print(f'Время проведенное на портале при регистрации составило {(end - start)}')
#     return wrapper
#
#
# reg_dict = {}  # сохраняем все данные, вводимые при регистрации в словарь вглобальной области
#
#
# @reg_time
# def registration():
#     global reg_dict
#     reg_dict['Фамилиия'] = input('Введите фамилию:')
#     reg_dict['Имя'] = input('Введите имя:')
#     reg_dict['Отчество'] = input('Введите отчество:')
#     reg_dict['Дата рождения'] = input('Введите дату рождения:')
#     reg_dict['Пол'] = input('Укажите пол:')
#     reg_dict['Адрес электронной почты '] = input('Укажите адрес электронной почты:')
#     reg_dict['Логин'] = input('Укажите логин:')
#     # password1 = ""
#     # password2 = " "
#     while True:
#         password1 = input('Укажите пароль:')
#         password2 = input('Укажите пароль повторно:')
#         if password1 != password2:
#             print('Ошибка. Пароли не совпадают')
#         else:
#             reg_dict['Пароль'] = password2
#             break
#
#
# registration()
