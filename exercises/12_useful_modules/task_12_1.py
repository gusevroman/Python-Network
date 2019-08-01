# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess


def ping_ip(ip_address):
    '''
    The result of the function is True on success or False if ip-address is unreachable.
    :param ip_address:
    :return:
    '''
    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address])
    return reply.returncode == 0
    # if reply.returncode == 0:
    #     return True
    # else:
    #     return False


def ping_ip_addresses(ip_addresses):
    '''
    The result of the function is a tuple with two lists of transmitted ip-addresses. One of them is a list
    of received. The second list of losses.
    :param ip_addresses:            # list of ip-addresses
    :return: trans_ip_addresses     # tuple([received], [losses])
    '''
    trans_received = []
    trans_losses = []
    for ip_address in ip_addresses:
        if ping_ip(ip_address):
            trans_received.append(ip_address)
        else:
            trans_losses.append(ip_address)
    result = (trans_received, trans_losses)
    return result

"""
# v.1
def ping_ip_addresses(ip_addresses):
    '''
    The result of the function is a tuple with two lists of transmitted ip-addresses. One of them is a list
    of received. The second list of losses.
    :param ip_addresses:            # list of ip-addresses
    :return: trans_ip_addresses     # tuple([received], [losses])
    '''
    trans_received = []
    trans_losses = []
    for ip_address in ip_addresses:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_address])
        if reply.returncode == 0:
            trans_received.append(ip_address)
        else:
            trans_losses.append(ip_address)
    result = (trans_received, trans_losses)
    return result
"""

list_of_ip = ['1.1.1.3', '8.8.8.8', '8.8.4.4', '8.8.7.1']

if __name__ == '__main__':
    print(ping_ip_addresses(list_of_ip))
# print(ping_ip('8.8.8'))