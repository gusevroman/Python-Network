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


# Все отлично

# вариант решения
while True:
    ip_address = input('Введите адрес: ')
    octets = ip_address.split('.')
    correct_ip = True

    for octet in octets:
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break
    if correct_ip:
        break
    print('Incorrect IPv4 address')

first_octet = int(octets[0])

if 1 <= first_octet <= 223 :
    print('unicast')
elif 224 <= first_octet <= 239 :
    print('multicast')
elif ip_address == '0.0.0.0':
    print('unassigend')
elif ip_address == '255.255.255.255':
    print ('local broadcast')
else:
    print('unused')

# еще один вариант

while True:
    ip = input('Введите IP-адрес в формате x.x.x.x: ')
    octets = ip.split('.')
    valid_ip = len(octets) == 4

    for i in octets:
        valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

    if valid_ip:
        break
    print('Incorrect IPv4 address')

if 1 <= int(octets[0]) <= 127:
    print('unicast')
elif 224 <= int(octets[0]) <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

