# -*- coding: utf-8 -*-
'''
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

'''
import re
from pprint import pprint
import yaml
from netmiko import ConnectHandler

# списки команд с ошибками и без:
commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands


def send_config_commands(device, config_commands, verbose=True):
    """
    The Function connects to the device by ssh and runs command in enable. The function tests for errors:
        - Invalid input detected, Incomplete command, Ambiguous command
    Function prints messages about errors:
        - Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
    :param device:  dictionary with parameters of connections to device
    :param config_commands: list of commands for running
    :param verbose: if True then print result of running commands
    :return: tuple of two dictionary: ({good}, {bad}). keys - command, values - result of running command
    """
    regex = re.compile('% (?P<error>.+)')
    no_errors = {}
    with_errors = {}
    if verbose is True:
        print('\nconnection to device {} ...'.format(device['ip']))

    with ConnectHandler(**device) as ssh:
        ssh.enable()
        for command in config_commands:
            cli_output = ssh.send_config_set(command)
            # Find for string of error
            match = re.search(regex, cli_output)
            if match:
                # if error in output CLI, then print message and update dictionary - command:error
                print('\nКоманда "{}" выполнилась с ошибкой "{}" на устройстве {}'.format(command,
                                                                                          match.group('error'),
                                                                                          device['ip']))
                with_errors[command] = cli_output
                answer = input('Продолжать выполнять команды? [y]/n: ')
                if answer in ['n', 'no']:
                    break
            else:
                # update dictionary - command: output from CLI
                no_errors[command] = cli_output
                if verbose is True:
                    print('\n', cli_output)
    result = (no_errors, with_errors)

    return result


if __name__ == "__main__":
    with open('devices.yaml') as f:
        data = yaml.safe_load(f)
        for dev in data:
            pprint(send_config_commands(dev, commands))
