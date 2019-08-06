# -*- coding: utf-8 -*-
'''
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
'''
from textfsm import clitable
from pprint import pprint
from datetime import datetime
import yaml
from netmiko import ConnectHandler
import logging

logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_and_parse_show_command(device_dict, command, templates_path='templates'):
    """
    The function connects to device, than sent command show with netmiko, then  parsed command output with TextFSM
    :param device_dict: list of dictionaries with parameters of connections to devices (from *.yaml)
    :param command: the command to be executed
    :param templates_path: path to templates TextFSM. The default "templates"
    :return: result is list of dictionaries from command output (ex. task_22_1a):
        * keys - name of the variables in templates TextFSM
        * values - are parts of the command output that correspond to variables
    """
    start_msg = '===> {} Connection TO: {}'
    received_msg = '<=== {} Received FROM:  {}'
    time_of_parse_msg = 'The time of parsing the command from the device {} was: {}'

    result = []
    ip = device_dict['ip']
    vendor = device_dict['device_type']

    start_time = datetime.now()
    logging.info(start_msg.format(datetime.now().time(), ip))

    # Connect to device and return command output
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        # host_name = ssh.find_prompt()
        command_output = ssh.send_command(command)
        # print('command_output: \n', command_output)
        logging.info(received_msg.format(datetime.now().time(), ip))

    # parsing result of command_output (with TextFSM)
    attributes = {'Command': command, 'Vendor': vendor}
    cli_table = clitable.CliTable('index', templates_path)
    cli_table.ParseCmd(command_output, attributes)

    # Some variants for print parsed command output
    # print('CLI Table output:\n', cli_table)

    print('Formatted Table:\n', cli_table.FormattedTable())

    # Lists of strings parsed command output
    # data_rows = [list(row) for row in cli_table]
    header = list(cli_table.header)

    # print('-' * 79)
    # print('List of lists:\n', header)
    # for row in data_rows:
    #     print(row)
    # print('-' * 79)

    # Make result - list of dictionaries parsed command output
    for item in cli_table:
        result_dict = dict(zip(header, item))
        result.append(result_dict)
    logging.info(time_of_parse_msg.format(ip, (datetime.now() - start_time)))
    return result


if __name__ == '__main__':
    send_command = 'sh ip int br'
    start_time = datetime.now()
    with open('devices.yaml') as devices_for_parse:
        devices = yaml.safe_load(devices_for_parse)
        for device in devices:
            send_and_parse_show_command(device, send_command)
    print('ALL time of running all command: ', datetime.now() - start_time, end='\n\n')
