# -*- coding: utf-8 -*-
'''
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command
из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
'''
from task_22_4 import send_and_parse_show_command
import yaml
from datetime import datetime
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint


def send_and_parse_command_parallel(devices, command, templates_path='templates', limit=3):
    """
    The function runs in parallel threads function send_and_parse_show_command from task 22.4.
    :param devices: list of dictionaries with parameters of connections to devices (from *.yaml)
    :param command: the command to be executed
    :param templates_path: path to templates TextFSM. The default "templates"
    :param limit: maximum count parallel threads (default 3)
    :return: result is lists of list of dictionaries from command output:
        * keys - name of the variables in templates TextFSM
        * values - are parts of the command output that correspond to variables
    """
    result = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        output_thread = executor.map(send_and_parse_show_command, devices, repeat(command))
        for device, command_output in zip(devices, output_thread):
            result.append(command_output)
    return result


if __name__ == '__main__':
    send_command = 'sh ip int br'
    with open('devices.yaml') as devices_for_parse:
        devices = yaml.safe_load(devices_for_parse)
        start_time_all = datetime.now()
        pprint(send_and_parse_command_parallel(devices, send_command, templates_path='templates', limit=2))
        print('All time of running all commands in threads: ... ', datetime.now() - start_time_all)
