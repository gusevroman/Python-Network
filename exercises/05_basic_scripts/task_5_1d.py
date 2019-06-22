# -*- coding: utf-8 -*-
'''
Задание 5.1d

Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра,
пользователь мог вводить название параметра в любом регистре.

Пример выполнения скрипта:
$ python task_5_1d.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): IOS
15.4


Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
'''

london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

dev = (input('Введите имя устройства: ').lower())
dev_val = input('Введите имя параметра (ios, model, vendor, location, ip): ').lower()

print(london_co[dev].get((dev_val), 'Такого параметра нет'))


# Все отлично

# вариант решения

device = input('Введите имя устройства: ')
params = ', '.join(london_co[device].keys())
parameter = str.lower(input(f'Введите имя параметра ({params}): '))

print(london_co[device].get(parameter, 'Такого параметра нет'))
