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


# Все отлично

# только, например, при таком адресе будет ошибка
# потому что в списке ip_address не будет элементов
'''
Input ip-address: 500.1.1.1
Attention! Неправильный ip-адрес.
Traceback (most recent call last):
  File "task_6_2a.py", line 32, in <module>
    if ip_address[0] in range(1, 224):
IndexError: list index out of range
'''

# вариант решения

ip_address = input('Enter ip address: ')
octets = ip_address.split('.')
correct_ip = True

if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:
        #тут второе условие int(octet) in range(256)
        # проверяется только в том случае, если первое условие истина
        #Если встретился хоть один октет с нарушением,
        # дальше можно не смотреть
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break

if not correct_ip:
    print('Incorrect IPv4 address')
else:
    octets_num = [int(i) for i in octets]

    if octets_num[0] in range(1,224):
        print('unicast')
    elif octets_num[0] in range(224,240):
        print('multicast')
    elif set(octets_num) == {255}:
        print('broadcast')
    elif set(octets_num) == {0}:
        print('unassigned')
    else:
        print('unused')


####### Второй вариант

ip = input('Введите IP-адрес в формате x.x.x.x: ')
octets = ip.split('.')
valid_ip = len(octets) == 4

for i in octets:
    valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

if valid_ip:
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
else:
    print('Неправильный IP-адрес')

