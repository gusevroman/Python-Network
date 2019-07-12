# -*- coding: utf-8 -*-
'''
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей со значениями

Функция возвращает результат в виде списка словарей, где ключи - взяты из первого списка,
а значения подставлены из второго.

Например, если функции передать как аргументы список headers и список
[('FastEthernet0/0', 'up', 'up', '10.0.1.1'),
 'FastEthernet0/1', 'up', 'up', '10.0.2.1')]

Функция должна вернуть такой список со словарями (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
 {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

Проверить работу функции:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функция parse_sh_ip_int_br из задания 15.2, если ей как аргумент передать sh_ip_int_br.txt.

Функцию parse_sh_ip_int_br не нужно копировать.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from task_15_2 import parse_sh_ip_int_br

headers = ['interface', 'address', 'status', 'protocol']


def convert_to_dict(headers, dev_status):
    '''
    The function is result the list of dictionaries with key from headers and values
    :param headers: list of keys
    :param dev_status:  is result of function parse_sh_ip_int_br from task_15_2
    :return: result
    '''
    result = []
    for line in dev_status:
        dict_line = dict(zip(headers, line))
        result.append(dict_line)
    return result


dev_status = parse_sh_ip_int_br('sh_ip_int_br.txt')
convert_to_dict(headers, dev_status)
