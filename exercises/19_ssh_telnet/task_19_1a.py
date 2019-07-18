# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''
import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException


command = 'sh ip int br'


def send_show_command(device, command):
    '''
    Function connects to the device by ssh and runs command.
    :param device: It's a dict with parameters of connection.
    :param command:
    :return: - String with command.
    '''
    print('connection to device {}'.format(device['ip']))
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            print(result)
    except AuthenticationException:
        result = 'Authentication failure: unable to connect {} {}'.format(device['device_type'],device['ip'])
        print(result)

    return result


if __name__ == "__main__":
    with open('devices.yaml') as f:
        data = yaml.safe_load(f)
        for device in data:
            send_show_command(device, command)
