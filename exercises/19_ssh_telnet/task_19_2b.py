# -*- coding: utf-8 -*-
'''
Задание 19.2b
Скопировать функцию send_config_commands из задания 19.2a и добавить проверку на ошибки.
При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command
Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве, например:
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Ошибки должны выводиться всегда, независимо от значения параметра verbose.
При этом, verbose по-прежнему должен контролировать будет ли выводиться сообщение:
Подключаюсь к 192.168.100.1...
Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками
Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд
Проверить работу функции можно на одном устройстве.
Пример работы функции send_config_commands:
In [16]: commands
Out[16]:
['logging 0255.255.1',
 'logging',
 'a',
 'logging buffered 20010',
 'ip http server']
In [17]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Команда "a" выполнилась с ошибкой "Ambiguous command:  "a"" на устройстве 192.168.100.1
In [18]: pprint(result, width=120)
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                    'R1(config)#ip http server\n'
                    'R1(config)#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                            'R1(config)#logging buffered 20010\n'
                            'R1(config)#'},
 {'a': 'config term\n'
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
       'R1(config)#a\n'
       '% Ambiguous command:  "a"\n'
       'R1(config)#',
  'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})
In [19]: good, bad = result
In [20]: good.keys()
Out[20]: dict_keys(['logging buffered 20010', 'ip http server'])
In [21]: bad.keys()
Out[21]: dict_keys(['logging 0255.255.1', 'logging', 'a'])
Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.
R1(config)#logging
% Incomplete command.
R1(config)#a
% Ambiguous command:  "a"
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
    :return: tuple of two dictionaries: ({good}, {bad}). keys - command, values - result of running command
    """
    regex = re.compile('\% (?P<error>\w.+)\n')
    no_errors = {}
    with_errors = {}
    if verbose == True:
        print('\nconnection to device {} ...'.format(device['ip']))

    with ConnectHandler(**device) as ssh:
        ssh.enable()
        for command in config_commands:
            cli_output = ssh.send_config_set(command)
            # Looking for string with error
            match = re.search(regex, cli_output)
            if match:
                # if error is in output CLI, then print message and update dictionary - command:error
                print('\nКоманда "{}" выполнилась с ошибкой "{}" на устройстве {}'.format(command,match.group('error'), device['ip']))
                with_errors[command] = cli_output
            else:
                # update dictionary - command: output from CLI
                no_errors[command] = cli_output
                if verbose == True:
                    print('\n', cli_output)
    result = (no_errors, with_errors)

    return result


if __name__ == "__main__":
    with open('devices.yaml') as f:
        data = yaml.safe_load(f)
        for device in data:
            pprint(send_config_commands(device, commands))

