# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
'''
import yaml
from netmiko import ConnectHandler
from datetime import datetime
import logging
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor


logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show(device, command):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received:   {}'
    ip = device['ip']
    logging.info(start_msg.format(datetime.now().time(), ip))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        host_name = ssh.find_prompt()
        result = ssh.send_command(command)
        logging.info(received_msg.format(datetime.now().time(), ip))
        return host_name, command, result


def send_show_command_to_devices(devices, command, filename, limit=3):
    """
    The function sends command show to device in parallel threads. Then write results into file.
    :param devices: list of dictionaries with parameters of connections to devices
    :param command: command (ex. show)
    :param filename: name of file where to write output of all commands
    :param limit: maximum count parallel threads (default 3)
    :return: The function hasn't result
    """
    with open(filename, 'w') as dest:
        with ThreadPoolExecutor(max_workers=limit) as executor:
            result = executor.map(send_show, devices, repeat(command))
            for device, output in zip(devices, result):
                host_name, command_send, command_output = output
                dest.write(host_name + command_send+'\n')
                dest.write(command_output + '\n')


if __name__ == '__main__':
    with open('devices.yaml') as src:
        devices = yaml.safe_load(src)
        start_time = datetime.now()
        send_show_command_to_devices(devices, 'sh ip int br', 'devices_sh_br.txt', 3)
        print('time of running command', datetime.now() - start_time)
