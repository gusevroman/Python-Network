# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
mac = 'AAAA:BBBB:CCCC'

mac = mac.replace(':', '')     # убрали двоеточие. Тип остался строка
mac = int(mac, 16)             # перевели из 16ричной системы в 10тичную

print("{0:b}".format(mac))


# Все отлично

