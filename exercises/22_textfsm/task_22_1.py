# -*- coding: utf-8 -*-
'''
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

'''
import textfsm


def parse_command_output(template, command_output):
    """
    The function processes the output of the command and returns the string
    :param template: name of file with template TextFSM
    :param command_output: output from command show (string)
    :return: is list: first element this is column names and other elements is lists with result from
     output processing
    """
    result = []
    with open(template) as template_file:
        re_table = textfsm.TextFSM(template_file)
        header = re_table.header
        output_parsed = re_table.ParseText(command_output)
        result.append(header)
        result.extend(output_parsed)
        return result


if __name__ == '__main__':
    with open("output/sh_ip_int_br.txt") as f:
        sh_ip_int_br = f.read()
    template_command = 'templates/sh_ip_int_br.template'
    parse_command_output(template_command, sh_ip_int_br)
