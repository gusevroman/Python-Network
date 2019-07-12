# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''

import re


def get_ints_without_description(config_dev):
    '''
    The Function edits configurations and return list of names interfaces that hasn't descriptions
    :param config_dev: file for edits, for example config_r1.txt
    :return: list of names interfaces
    '''
    regex = re.compile(r'^interface (?P<device>\S+)'
                       r'| ip address +(?P<ip_address>\S+) +(?P<mask>\S+)'
                       r'| (?P<description>description) ')
    result = []


    with open(config_dev) as f:
        for line in f.readlines():
            match = re.search(regex, line)
            if match:
                if match.lastgroup == 'device':
                    device = match.group(match.lastgroup)
                    result.append(device)
                elif device:
                    description = match.group('description')
                    if description:
                        result.remove(device)
    return result

get_ints_without_description('config_r1.txt')

# Все отлично

# вариант решения


# в этом варианте все посторено на том, что регулярки в которых стоит |,
# матчатся до первого совпадения
# если на интерфейсе было описание, проматчится первая часть, если нет - вторая
def get_ints_without_description(file_name):
    regex = ('interface \S+\n description (?P<desc>.+)\n'
             '|interface (?P<intf>\w+\S+)\n')
    with open (file_name) as f:
        intf_without_desc = []
        for m in re.finditer(regex, f.read()):
            if not m.group('desc'):
                intf_without_desc.append(m.group('intf'))
    return intf_without_desc


# тут мы считываем интерфейсы секциями и проверяем в каждой секции есть ли слово description
def get_ints_without_description(cfg_filename):
    regex = r'interface (?P<intf>\S+)\n( .*\n)*'
    with open(cfg_filename) as f:
        intf_without_desc = []
        intf_cfg = re.finditer(regex, f.read())
        for match in intf_cfg:
            if not 'description' in match.group():
                intf_without_desc.append(match.group('intf'))
    return intf_without_desc


# те же варианты с генератором списка
def get_ints_without_description(file_name):
    regex = ('interface \S+\n description (?P<desc>.+)\n'
             '|interface (?P<intf>\w+\S+)\n')
    with open (file_name) as f:
        intf_without_desc = [m.group('intf')
                             for m in re.finditer(regex, f.read())
                             if not m.group('desc')]
    return intf_without_desc

def get_ints_without_description(cfg_filename):
    regex = r'interface (?P<intf>\S+)\n( .*\n)*'
    with open(cfg_filename) as f:
        intf_without_desc = [match.group('intf')
                             for match in re.finditer(regex, f.read())
                             if not 'description' in match.group()]
    return intf_without_desc

