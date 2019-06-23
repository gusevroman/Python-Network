# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

input_ip_address = input('Input ip-address: ').split('.')

if len(input_ip_address) != 4:
    print('Неправильный ip-адрес - не состоит из 4 элементов разделенных точкой')
else:
    ip_address = []

    for octet in input_ip_address:
        if octet.isdigit() and int(octet) in range(256):
            ip_address.append(int(octet)) # octets are integers
        else:
            print('Attention! Неправильный ip-адрес.')
            break

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
    print(result)
