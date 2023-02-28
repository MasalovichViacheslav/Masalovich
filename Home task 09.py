# Задачи на файлы
'''
Задача 1
Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла добавлен
восклицательный знак.

ПРИМЕЧАНИЕ. То, что написано в условии, понял следующим образом: надо считать все строки в текстовом файле и вывести
эти строки, добавив в конце '!'. Решение для такой интепретации условия ниже
'''
# with open('Task 1 text.txt', 'r', encoding='UTF-8') as file:
#     for line in file:
#         s = line.rstrip() + '!'
#         print(s)
'''
На занятии условие задачи было объяснено по-другому: имеется текстовый файл с несколькими строками, надо считать данные 
файла и вывести только те строки, в которых в конце стоит '!'.
Решение для такого условия задачи
'''
# with open('Task 1 text.txt', 'r', encoding='UTF-8') as file:
#     for line in file:
#         s = line.rstrip()
#         if s[-1] == '!':
#             print(s)
'''
Задача 2
Создать файл input.txt и записать в него 10 чисел через пробел. Считать из него эти числа. Затем записать их
произведение в файл output.txt.
'''
# import random
#
# with open('input.txt', 'w', encoding='UTF-8') as file:
#     file.write(' '.join([str(random.randint(1, 5)) for _ in range(10)]))
# with open('input.txt', 'r', encoding='UTF-8') as file:
#     product = 1
#     for elem in list(map(int, file.read().split())):
#         product *= elem
# with open('output.txt', 'w', encoding='UTF-8') as file:
#     file.write(str(product))
'''
Задача 3
3.	Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара, цену единицы
и дату поступления товара на склад. Вывести список товаров, хранящихся больше месяца и стоимость которых
превышает 1 000 000 р.
'''
# from datetime import datetime
# from datetime import timedelta
#
# lst = []
# the_date = datetime.now() - timedelta(31)
# print(the_date)
# with open('Task 3 - List of goods.txt', 'r', encoding='UTF-8') as file:
#     for line in file:
#         s = line.strip().split(',')
#         lst.append(s)
#     for elem in lst:
#         inbound_date = datetime.strptime(elem[3].strip(), '%Y-%m-%d')
#         if int(elem[2].strip()[:len(elem[2]) - 2]) > 1000000 and inbound_date < the_date:
#             print(','.join(elem))
'''
Задача 4
Написать программу “Викторина”. У вас есть 2 файла. В первом содержаться 10 вопросов(каждый вопрос в своей строке) во 
втором 10 ответов( каждый ответ как и вопрос в своей строке). Вам нужно считывать по 1 вопросу из файла с вопросами и 
давать на них ответ. Если ответ верный, добавлять к счётчику верных ответов 1 балл. В конце программа выводит количество
верных ответов на вопросы.
'''
# score = 0
# for elem in range(10):
#     with open('Task 4 - Questions.txt', 'r', encoding='UTF-8') as questions:
#         quest_lst = questions.read().split('\n')
#         print(f'Вопрос № {elem + 1}: {quest_lst[elem]}')
#     answer = input('Введите ответ:')
#     with open('Task 4 - Answers.txt', 'r', encoding='UTF-8') as answers:
#         answ_lst = answers.read().lower().split('\n')
#         if answer.lower() in answ_lst[elem]:
#             score += 1
# print(f'Правильных ответов - {score}')
'''
Задача 5
Создать словарь в качестве ключа которого будет 5-ти значное число, а в качестве значений кортеж состоящий из 2-ух 
элементов – имя(str) и возраста(int). Сделать 5-6 элементов словаря и записать данный словарь на диск в файл json 
формата
'''
# import random
# import json
#
# dict1 = {}
# for i in range(5):
#     dict1[random.randint(10000, 99999)] = (input('Введите имя:'), int(input('Введите возраст:')))
# print(dict1)
# with open('Task 5 dictionary.json', 'w', encoding='UTF-8') as json_file:
#     json.dump(dict1, json_file)
'''
Задача 6
Прочитать сохранённый json – файл и записать данные на диск в csv файл. Первое значение каждой строки должно начинаться 
со слова person, значения разделить ;
'''
# import json
#
# person_dict = {}
# with open('Task 5 dictionary.json', 'r', encoding='UTF-8') as file_json:
#     person_dict = json.load(file_json)
# some_str = ''
# for key, value in person_dict.items():
#     some_str += 'person' + ';' + str(key) + ';' + str(value) + ';' + '\n'
# with open('Task 6 file.csv', 'w', encoding='UTF-8') as file_csv:
#     file_csv.write(some_str)
'''
Задача 7
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое 
слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести 
лексикографически первое. Для решение вам необходимо открыть файл для чтения 7.txt .
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''
# with open('7.txt', 'r', encoding='utf-8') as file:
#     lst = file.read().lower().replace('\n', ' ').split()
# dict1 = {}
# for elem in lst:
#     dict1[elem] = lst.count(elem)
# maximum = 0
# for value in dict1.values():
#     if value > maximum:
#         maximum = value
# dict2 = {}
# for key, value in dict1.items():
#     if value == maximum:
#         dict2[key] = value
# minimal = '~' if '~' not in dict1 else print('Присвоить другое значение minimal')  # вывод пары "ключ-значение" с
# # лексиграфически первым ключом, если в dict2 несколько ключей
# for key in dict2:
#     if key < minimal:
#         minimal = key
# print(minimal, dict2[minimal])
'''
Задача 8
Вашей задачей будет восстановление исходной строки обратно. Напишите программу, которая считывает из файла строку, 
соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст. 
Для решение вам необходимо открыть файл для чтения 8.txt .

Sample Input:
a3b4c2e10b1
Sample Output:
Aaabbbbcceeeeeeeeeeb 
'''
# input_str = ''
# with open('8.txt', 'r', encoding='UTF-8') as file:
#     input_str = file.read()
# temp_str = ''
# for elem in input_str:
#     if elem.isalpha():
#         temp_str += ' ' + elem
#     else:
#         temp_str += elem
# lst = temp_str.lstrip().split()
# output_str = ''
# for elem in lst:
#     output_str += elem[0] * int(elem[1:])
# print(output_str)