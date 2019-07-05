# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла).
Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def parse_cdp_neighbors(command_output):
    '''
    Function edits output commands - show cdp neighbors.
        Function with one parameter - command_output
    :return:  # A dictionary that describes the connections between devices.
    for example for SW1:
       'SW1>show cdp neighbors\n\n'
        'Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n'
        '                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone\n\n'
        'Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID\n'
        'R1           Eth 0/1         122           R S I           2811       Eth 0/0\n'
    {(('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
    '''
    neighbors = {}

    command_output = command_output.split('\n')
    for line in command_output:
        if line.split() != []:
            if 'neighbors' in line:
                dev = line.split('>')[0]
            if 'Eth' in line:
                line = line.split()
                dev_port = line[1] + line[2]
                dev_ne = line[0]
                dev_ne_port = line[-2] + line[-1]
                neighbors[(dev, dev_port)] = (dev_ne, dev_ne_port)
    return neighbors


with open('sh_cdp_n_sw1.txt') as f:
    sh_command = f.read()


parse_cdp_neighbors(sh_command)