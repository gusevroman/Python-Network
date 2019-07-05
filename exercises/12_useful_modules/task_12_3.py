# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''

from tabulate import tabulate


def print_ip_table(list_of_reachable, list_of_unreachable):
    '''
    The function prints two of lists in table
    :param list_of_reachable:
    :param list_of_unreachable:
    :return:
    '''
    return tabulate({'Reachable': list_of_reachable, 'Unreachable': list_of_unreachable}, headers='keys')


list_of_reachable = ['10.1.1.1', '10.1.1.2']
list_of_unreachable = ['10.1.1.7', '10.1.1.8', '10.1.1.9']

print(print_ip_table(list_of_reachable, list_of_unreachable))