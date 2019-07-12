# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
import csv


def parse_sh_cdp_neighbors(sh_cdp_n):
    '''
    The function edits command output show cdp neighbors
    :param sh_cdp_n: one string command output (not filename)
    :return: dictionary connections between devices
    '''

    regex = re.compile('(?P<device>\S+)>|(?P<dev_neighbour>\S+) +(?P<intf>\S+ \d+\/\d+) .+ (?P<intf_neighbour>\S+ \d+\/\d+)')
    result_intf = {}
    result = {}
    match = re.finditer(regex, sh_cdp_n)
    for m in match:
        if m.lastgroup == 'device':
            device = m.group(m.lastgroup)
        elif device:
            result_dev_neighbours = {}
            _, dev_neighbour, intf, intf_neighbour = m.groups()
            result_dev_neighbours[dev_neighbour] = intf_neighbour
            result_intf[intf] = result_dev_neighbours
    result[device] = result_intf
    return result

filename = 'sh_cdp_n_sw1.txt'
with open(filename) as f:
    sh_cdp_n = f.read()
    parse_sh_cdp_neighbors(sh_cdp_n)
