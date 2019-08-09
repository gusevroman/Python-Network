# -*- coding: utf-8 -*-
'''
Задание 20.3

Создать функцию send_command_to_devices, которая отправляет
разные команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Intesend_show, rface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
'''
import yaml

from netmiko import ConnectHandler, NetMikoAuthenticationException
from datetime import datetime
import logging
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed
from task_20_2 import send_show, send_show_command_to_devices
from pprint import pprint
import time


commands = {'192.168.100.1': 'sh ip int br',
            '192.168.100.2': 'sh arp',
            '192.168.100.3': 'sh ip int br'}

logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_command_to_devices(devices, commands_dict, filename, limit=3):
    """
    The function sends different commands show to device in parallel threads. Then write results into file.
    :param devices: list of dictionaries with parameters of connection to device
    :param commands_dict: dictionary, says which command send to which device
    :param filename: name of file where write output of commands
    :param limit: maximum of threads(default is 3)
    :return: writes output into file
    """

    with open(filename, 'w') as dest:
        with ThreadPoolExecutor(max_workers=limit) as executor:
            future_list = []
            for device in devices:
                future = executor.submit(send_show, device, commands_dict[device['ip']])
                future_list.append(future)
            for f in as_completed(future_list):
                result = f.result()
                host_name, command_send, command_output = result
                dest.write(host_name + command_send+'\n')
                dest.write(command_output + '\n')


if __name__ == '__main__':
    with open('devices.yaml') as src:
        devices_y = yaml.safe_load(src)
        start_time = datetime.now()
        send_command_to_devices(devices_y, commands, 'devices_show.txt', 3)
        print('time of running command', datetime.now() - start_time)
