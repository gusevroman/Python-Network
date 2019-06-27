#!/home/vagrant/venv/pyneng-py3-7/bin/python3.7
# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# v.1
'''
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if ' Gi' in line:
            vlan, mac_address, _, intf = line.split()
            print(f'{vlan:8} {mac_address:17} {intf:8}')
'''

#v.2
with open('CAM_table.txt', 'r') as f:
   for line in f:
       if not line.startswith('-') and not line.startswith('\n') and line.split()[0].isdigit():
           vlan, mac_address, _, intf = line.split()
           print(f'{vlan:7}{mac_address:17}{intf:8}')
