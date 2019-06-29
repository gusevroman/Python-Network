# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(config_filename):
    '''
    Функция обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:
    - access_mode_template
    - trunk_mode_template
    :param config_filename:
    :return: result             # кортеж из двух словарей
    '''
    access_mode_template = {}
    trunk_mode_template = {}

    with open(config_filename) as f:
        for line in f:
            if 'FastEthernet' in line:
                line = line.split()
                intf = line[-1]
            if 'access vlan' in line:   # формируем словарь access_mode_template
                vlan = line.split()[-1]
                access_mode_template[intf] = int(vlan)
            if 'trunk allowed vlan' in line:    # формируем словарь trunk_mode_template
                vlan = line.split()[-1].split(',')
                vlan = [int(vlan) for vlan in vlan]
                trunk_mode_template[intf] = vlan

    result = (access_mode_template, trunk_mode_template)
    return result

print(get_int_vlan_map('config_sw1.txt'))
