# -*- coding: utf-8 -*-
'''
Задание 20.1
Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.
l
Для проверки доступности IP-адреса, используйте ping.
'''
import sys
sys.path.append('../12_useful_modules/')
from task_12_1 import ping_ip
from concurrent.futures import ThreadPoolExecutor
# import subprocess

list_of_ips = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']


# def ping_ip(ip_address):
#     """
#     The result of the function is True on success or False if ip-address is unreachable.
#     :param ip_address:
#     :return:
#     """
#     reply = subprocess.run(['ping', '-c', '2', '-n', ip_address])
#     return reply.returncode == 0


def ping_ip_addresses(ip_list, limit=4):
    """
    The function test availible ip-addreses in parallel threads
    :param ip_list: list of ip-addresses
    :param limit: maximum parallel threads (default = 3)
    :return: tuple of two lists - (availible, unavailble)
    """
    available = []
    unavailable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip, ip_list)
        for ip, pingable in zip(ip_list, result):
            if pingable:
                available.append(ip)
            else:
                unavailable.append(ip)

    return available, unavailable



if __name__ == '__main__':
    print(ping_ip_addresses(list_of_ips, 4))
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(ping_ip_addresses(list_of_ips))
#     print(ping_ip_addresses(list_of_ips))
