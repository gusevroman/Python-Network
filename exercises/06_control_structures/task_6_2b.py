# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

input_ip_address = input('Input ip-address: ').split('.')

ip_correct = False

# Проверка правильности ввода ip-адреса
while not ip_correct:
    if len(input_ip_address) != 4:
        print('Неправильный ip-адрес - не состоит из 4 элементов разделенных точкой')
    if (len(input_ip_address)) == 4:
        ip_address = [int(octet) for octet in input_ip_address if octet.isdigit() and int(octet) in range(256)]
        if len(ip_address) == 4:
            ip_correct = True
        else:
            print('Неправильный ip-адрес')
            input_ip_address = input('Введите ip-address еще раз: ').split('.')
    else:
        input_ip_address = input('Введите ip-address еще раз: ').split('.')

# Классификация ip-адреса
print('-' * 50, end='')
if ip_address[0] in range(1, 224):
    result = 'unicast'
elif ip_address[0] in range(224, 239):
    result = 'multicast'
elif ip_address == [255, 255, 255, 255]:
    result = 'local broadcast'
elif ip_address == [0, 0, 0, 0]:
    result = 'unassigned'
else:
    result = 'unused'
print()
print(result)
