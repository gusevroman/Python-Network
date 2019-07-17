# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет перечень команд в конфигурационном режиме
на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает строку с результатами выполнения команды:

In [7]: r1
Out[7]:
{'device_type': 'cisco_ios',
 'ip': '192.168.100.1',
 'username': 'cisco',
 'password': 'cisco',
 'secret': 'cisco'}

In [8]: commands
Out[8]: ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

In [9]: result = send_config_commands(r1, commands)

In [10]: result
Out[10]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#logging 10.255.255.1\n
R1(config)#logging buffered 20010\nR1(config)#no logging console\nR1(config)#end\nR1#'

In [11]: print(result)
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.255.255.1
R1(config)#logging buffered 20010
R1(config)#no logging console
R1(config)#end
R1#


Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_config_commands.
"""
import yaml
from netmiko import ConnectHandler


commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]


def send_config_commands(device, config_commands):
    """
    The Function connects to the device by ssh and runs command in enable
    :param device:  dictionary with parameters of connections to device
    :param config_commands: list of commands for run
    :return: string with results of run command
    """
    print('\nconnection to device {} ...'.format(device['ip']))

    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
        print(result)

    return result


if __name__ == "__main__":
    with open('devices.yaml') as f:
        data = yaml.safe_load(f)
        for device in data:
            send_config_commands(device, commands)