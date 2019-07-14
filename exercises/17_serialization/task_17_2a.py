# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов
и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли
 топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
import glob
import re
import yaml
from pprint import pprint

sh_cdp_files = glob.glob('sh_cdp_n_*')

def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    '''
    The function edits command show cdp neighbor from several files.
    :param list_of_files:
    :param save_to_filename: Default is None
    :return: dict and if save_to_filename is set, dict is writen to filename.YAML
    '''

    regex = re.compile(r'(?P<r_dev>\w+)  +(?P<l_intf>\S+ \S+)'
                       r'  +\d+  +[\w ]+  +\S+ +(?P<r_intf>\S+ \S+)')
    topology_dict = {}
    for file in list_of_files:
        with open(file) as f:
            command_output = f.read()
            connect_dict = {}
            l_dev = re.search(r'(\S+)[>#]', command_output).group(1)
            connect_dict[l_dev] = {}
            for match in regex.finditer(command_output):
                r_dev, l_intf, r_intf = match.group('r_dev', 'l_intf', 'r_intf')
                connect_dict[l_dev][l_intf] = {r_dev: r_intf}
            topology_dict.update(connect_dict)

    if save_to_filename == None:
        pass
    else:
        with open(save_to_filename, 'w') as dest:
            yaml.dump(topology_dict, dest)


    return topology_dict


if __name__ == "__main__":
    pprint(generate_topology_from_cdp(sh_cdp_files, 'topology.yaml'))