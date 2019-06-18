# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

net = input('Input ip-address: ')

ip, ip_mask = net.split('/')
mask = ip_mask

ip = ip.split('.')
ip = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])

ip_mask ='1'*int(ip_mask)+'0'*(32-(int(ip_mask)))
ip_mask = int(ip_mask[:8], 2), int(ip_mask[8:16], 2), int(ip_mask[16:24], 2), int(ip_mask[24:32], 2)

ip_template = '''
{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''

print(ip_template.format('Network:', ip[0], ip[1], ip[2], ip[3]))
print(ip_template.format('Mask: \n' + mask, ip_mask[0], ip_mask[1], ip_mask[2], ip_mask[3]))


# variant 2:
"""
# Output Network, v.1
print(f'''Network:
{ip[0]:<8}  {ip[1]:<8}  {ip[2]:<8}  {ip[3]:<8}
{ip[0]:08b}  {ip[1]:08b}  {ip[2]:08b}  {ip[3]:08b}
''')

# Output Mask, v.1
print(f'''Mask:
/{mask}
{ip_mask[0]:<8}  {ip_mask[1]:<8}  {ip_mask[2]:<8}  {ip_mask[3]:<8}
{ip_mask[0]:08b}  {ip_mask[1]:08b}  {ip_mask[2]:08b}  {ip_mask[3]:08b}''')
"""
