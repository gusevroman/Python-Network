# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            if 'switchport mode access' in line:    # формируем словарь access_mode_template
                line_next = f.readline()            # чтение следующей строки и проверка VLAN
                if 'access vlan' in line_next:
                    vlan = line_next.split()[-1]
                else:
                    vlan = 1
                access_mode_template[intf] = int(vlan)
            if 'trunk allowed vlan' in line:         # формируем словарь trunk_mode_template
                vlan = line.split()[-1].split(',')
                vlan = [int(vlan) for vlan in vlan]
                trunk_mode_template[intf] = vlan
    result = (access_mode_template, trunk_mode_template)
    return result

# print(get_int_vlan_map('config_sw2.txt'))
