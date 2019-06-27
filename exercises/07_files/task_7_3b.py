# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlan_input = int(input('Введите VLAN: '))

result = []

with open('CAM_table.txt', 'r') as f:
    for line in f:
        if not line.startswith('-') and not line.startswith('\n') and line.split()[0].isdigit():
            vlan, mac_address, _, intf = line.split()
            result.append([int(vlan), [mac_address, intf]])
            # if int(vlan) == vlan_input: # вывод запрашиваемого VLAN без сортировки
            #    print(f'{vlan:7}{mac_address:17}{intf:8}')

print('-' * 50)

for line in sorted(result):
    if line[0] == vlan_input:
        print(f'{line[0]:<6} {line[1][0]:17}{line[1][1]:8}')

print('-' * 50)