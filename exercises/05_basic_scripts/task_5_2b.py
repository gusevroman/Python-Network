#!/home/vagrant/venv/pyneng-py3-7/bin/python3.7
# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# ~/venv/pyneng-py3-7
# /usr/bin/env python
# /usr/local/bin/ python3.7

from sys import argv

# net = input('Input ip-address: ')
net = argv[1]


ip, ip_mask = net.split('/')
mask = ip_mask

ip = ip.split('.')
ip = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])

ip_bin = f'{ip[0]:08b}{ip[1]:08b}{ip[2]:08b}{ip[3]:08b}'
ip_bin = ip_bin[:int(mask)] + '0' * (32 - int(mask))
ip_bin = int(ip_bin[:8], 2), int(ip_bin[8:16], 2), int(ip_bin[16:24], 2), int(ip_bin[24:32], 2)

ip_mask ='1'*int(ip_mask)+'0'*(32-(int(ip_mask))) # маска в виде строки из нулей и единиц
ip_mask = int(ip_mask[:8], 2), int(ip_mask[8:16], 2), int(ip_mask[16:24], 2), int(ip_mask[24:32], 2)

ip_template = '''
{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}'''

print(ip_template.format('Network:', ip_bin[0], ip_bin[1], ip_bin[2], ip_bin[3]))
print(ip_template.format('Mask: \n' + mask, ip_mask[0], ip_mask[1], ip_mask[2], ip_mask[3]))
