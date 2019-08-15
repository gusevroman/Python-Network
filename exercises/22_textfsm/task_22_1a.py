# -*- coding: utf-8 -*-
'''
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
'''

import textfsm


def parse_output_to_dict(template, command_output):
    """
    The function processes the output of the command and returns the string
    :param template: name of file with template TextFSM
    :param command_output: output from command show (string)
    :return: list of dictionaries: keys are names of variables, values are output
    """
    result = []
    with open(template) as template_file:
        re_table = textfsm.TextFSM(template_file)
        header = re_table.header
        output_parsed = re_table.ParseText(command_output)
        for item in output_parsed:
            result_dict = dict(zip(header, item))
            result.append(result_dict)
    return result


if __name__ == '__main__':
    with open("output/sh_ip_int_br.txt") as f:
        sh_ip_int_br = f.read()
    template_command = 'templates/sh_ip_int_br.template'
    print(parse_output_to_dict(template_command, sh_ip_int_br))
