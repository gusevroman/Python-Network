# -*- coding: utf-8 -*-
'''
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
'''
import textfsm
from textfsm import clitable
from pprint import pprint


def parse_command_dynamic(command_output, attributes_dict, index_file='index', templ_path='templates'):
    """
    The function converts the result of the output of the command into a dictionary
    :param command_output: output from command (string)
    :param attributes_dict: dictionaries of attributes with key-value:
         * 'Command': command
         * 'Vendor': vendor
    :param index_file: name of the file where the correspondence between commands and templates is stored.
        The default value is "index"
    :param templ_path: directory where templates is stored/ The default "templates"
    :return: is list of dictionaries output from command (ex. task_22_1a):
        * keys - name of the variables in templates TextFSM
        * values - are parts of the output from command that correspond to variables
    """
    result = []
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    print('CLI Table output:\n', cli_table)

    print('Formatted Table:\n', cli_table.FormattedTable())

    data_rows = [list(row) for row in cli_table]
    header = list(cli_table.header)

    print('-' * 79)
    print('List of lists:\n', header)
    for row in data_rows:
        print(row)
    print('-' * 79)

    for item in cli_table:
        result_dict = dict(zip(header, item))
        result.append(result_dict)

    return result


if __name__ == '__main__':
    with open("output/sh_ip_int_br.txt") as f:
        command_output = f.read()
    attributes = {'Command': 'show ip int br', 'Vendor': 'cisco_ios'}
    pprint(parse_command_dynamic(command_output, attributes))
