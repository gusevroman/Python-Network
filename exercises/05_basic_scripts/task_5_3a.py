# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

mode_op = ['access', 'trunk']
mode_vlan = {
    'access': 'Введите номер VLAN: ',
    'trunk': 'Введите разрешенные VLANы: '
}


mode_dict = {
    'access': access_template,
    'trunk': trunk_template
}

mode = input(f'Введите режим работы интерфейса ({mode_op[0]}/{mode_op[1]}): ')
vlan = input(mode_vlan[mode].format(mode))
interface = input('Введите тип и номер интерфейса: : ')

print('\n' + '-' * 50)
print('interface {}'.format(interface))
print('\n'.join(mode_dict[mode]).format(vlan))
