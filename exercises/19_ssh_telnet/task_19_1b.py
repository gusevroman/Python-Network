# -*- coding: utf-8 -*-
'''
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''
import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException, NetMikoTimeoutException


command = 'sh ip int br'


def send_show_command(device, command):
    '''
    Function connects to the device by ssh and runs command.
    :param device: It's a dict with parameters of connection.
    :param command:
    :return: - String with command.
    '''
    print('\nconnection to device {} ...'.format(device['ip']))
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
    except AuthenticationException:
        result = 'Authentication failure: unable to connect {} {}'.format(device['device_type'], device['ip'])
    except NetMikoTimeoutException:
        result = 'Connection to device timed-out: {} {}'.format(device['device_type'], device['ip'])

    print(result)
    return result


if __name__ == "__main__":
    with open('devices.yaml') as f:
        data = yaml.safe_load(f)
        for device in data:
            send_show_command(device, command)

"""
import yaml
import sys
from netmiko import (ConnectHandler, NetMikoAuthenticationException,
                     NetMikoTimeoutException)


def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as error:
        print(error)


if __name__ == '__main__':
    command = 'sh ip int br'
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    result = send_show_command(r1, command)
    print(result)
"""