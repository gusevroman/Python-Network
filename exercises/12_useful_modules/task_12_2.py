# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''
from ipaddress import ip_address


def check_if_ip_is_network(ip_a):
    '''
    The function checks validity of IP addresses
    :param ip_a:                # ip-addresses
    :return: True / False
    '''
    try:
        ip_address(ip_a)
        return True
    except ValueError:
        return False


def convert_ranges_to_ip_list(list_of_ip):
    '''
    The function converts the list of IP addresses in different formats to a list where each IP address is listed
     separately.
    :param list_of_ip:      # a list of ip-addresses and/or ip-address ranges
    :return: ip_list        # a list of ip-addresses
    '''
    to_ip_list = []
    for list_ip in list_of_ip:
        if check_if_ip_is_network(list_ip):
            to_ip_list.append(list_ip)     # appended into the list a valid ip-address
        else:
            list_ip = list_ip.split('-')
            range_ip = (int(list_ip[1].split('.')[-1]) - int(list_ip[0].split('.')[-1]))
            list_ip = ip_address(list_ip[0])
            for i in range(0, range_ip + 1):
                to_ip_list.append(str(list_ip))
                list_ip += 1
                i += 1
    return to_ip_list


list_ip = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132', '8.8.8.8']
print(convert_ranges_to_ip_list(list_ip))