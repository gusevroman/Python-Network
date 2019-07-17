# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
import yaml
from netmiko import ConnectHandler


command = 'sh ip int br'


def send_show_command(device, command):
    '''
    Function connects to the device by ssh and runs command.
    :param device: It's a dict with parameters of connection.
    :param command:
    :return: - String with command.
    '''
    print('\nconnection to device {}'.format(device['ip']))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        print(result)
    return result


if __name__ == "__main__":
    with open('devices.yaml') as f:
        data = yaml.safe_load(f)
        for device in data:
            send_show_command(device, command)
