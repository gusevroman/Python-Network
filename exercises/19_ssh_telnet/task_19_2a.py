# -*- coding: utf-8 -*-
'''
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

verbose - это параметр функции send_config_commands, не параметр ConnectHandler!

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
'''
import yaml
from netmiko import ConnectHandler


commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]


def send_config_commands(device, config_commands, verbose=True):
    """
    The Function connects to the device by ssh and runs command in enable
    :param device:  dictionary with parameters of connections to device
    :param config_commands: list of commands for run
    :return: string with results of run command
    """
    if verbose == True:
        print('\nconnection to device {} ...'.format(device['ip']))

    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
        if verbose == True:
            print(result)

    return result


if __name__ == "__main__":
    with open('devices.yaml') as f:
        data = yaml.safe_load(f)
        for device in data:
            send_config_commands(device, commands)
