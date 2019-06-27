# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
import os
print(os.getcwd())
# ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ip_template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface     {}
'''

f = open('ospf.txt', 'r')
for ospf_route in f:
    ospf_route = ospf_route.replace('[', '') # убираем лишние квадратные скобки
    ospf_route = ospf_route.replace(']', '') # убираем лишние квадратные скобки
    ospf_route = ospf_route.replace(',', '') # убираем лишние запятые
    f = ospf_route.split() # получился список
    print(ip_template.format('OSPF', f[1], f[2], f[4], f[5], f[6]))