# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_address = input('Input ip-address: ').split('.')

ip_octet = []
for octet in ip_address:
    ip_octet.append(int(octet))

# v. 1
if ip_octet[0] in range(1, 224):
    result = 'unicast'
elif ip_octet[0] in range(224, 239):
    result = 'multicast'
elif ip_octet == [255, 255, 255, 255]:
    result = 'local broadcast'
elif ip_octet == [0, 0, 0, 0]:
    result = 'unassigned'
else:
    result = 'unused'
print(result)


"""
# v.2
if 1 <= ip_octet[0] <= 223:
    print('unicast')
elif 224 <= ip_octet[0] <= 239:
    print('multicast')
elif ip_octet == [255, 255, 255, 255]:
    print('local broadcast')
elif ip_octet == [0, 0, 0, 0]:
    print('unassigned')
else:
    print('unused')
"""